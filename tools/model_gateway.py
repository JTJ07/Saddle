"""Thin model-proposal control plane for Saddle Phase 4.

The model has no tools, shell, write capability or effect authority. It may only
return a structured full-file replacement proposal for the one pinned target.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Protocol

WORKER_PROPOSAL_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["case_id", "target_path", "replacement_text", "reason", "evidence_plan"],
    "properties": {
        "case_id": {"type": "string", "minLength": 1},
        "target_path": {"type": "string", "minLength": 1},
        "replacement_text": {"type": "string", "minLength": 1},
        "reason": {"type": "string", "minLength": 1},
        "evidence_plan": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 1}},
    },
}


class GatewayError(RuntimeError):
    pass


class CredentialUnavailable(GatewayError):
    pass


class GatewayResponseError(GatewayError):
    pass


@dataclass(frozen=True)
class ModelUsage:
    input_tokens: int | None
    output_tokens: int | None
    reasoning_tokens: int | None


@dataclass(frozen=True)
class ModelResult:
    model_id: str
    proposal: dict[str, Any]
    latency_ms: int
    usage: ModelUsage
    response_id: str | None


class ModelGateway(Protocol):
    def generate(
        self,
        *,
        case_id: str,
        target_path: str,
        problem: str,
        case_contract: str,
        target_source: str,
        tests_source: str,
    ) -> ModelResult: ...


def validate_worker_proposal(
    proposal: dict[str, Any],
    *,
    case_id: str,
    target_path: str,
    before_text: str,
    max_patch_lines: int = 80,
) -> dict[str, Any]:
    expected_fields = {"case_id", "target_path", "replacement_text", "reason", "evidence_plan"}
    if not isinstance(proposal, dict) or set(proposal) != expected_fields:
        raise GatewayResponseError("worker proposal has unexpected or missing fields")
    if proposal["case_id"] != case_id:
        raise GatewayResponseError("worker proposal case_id does not match pinned case")
    if proposal["target_path"] != target_path:
        raise GatewayResponseError("worker proposal target_path does not match allowlisted target")
    for field in ("replacement_text", "reason"):
        if not isinstance(proposal[field], str) or not proposal[field]:
            raise GatewayResponseError(f"worker proposal {field} must be non-empty")
    evidence_plan = proposal["evidence_plan"]
    if not isinstance(evidence_plan, list) or not evidence_plan or any(not isinstance(item, str) or not item for item in evidence_plan):
        raise GatewayResponseError("worker proposal evidence_plan must contain non-empty strings")
    replacement = proposal["replacement_text"]
    if replacement == before_text:
        raise GatewayResponseError("worker proposal does not change the target")

    diff = list(
        difflib.unified_diff(
            before_text.splitlines(),
            replacement.splitlines(),
            fromfile=f"a/{target_path}",
            tofile=f"b/{target_path}",
            lineterm="",
        )
    )
    changed_lines = sum(
        1
        for line in diff
        if (line.startswith("+") or line.startswith("-"))
        and not line.startswith("+++")
        and not line.startswith("---")
    )
    if changed_lines > max_patch_lines:
        raise GatewayResponseError(
            f"worker proposal exceeds max patch lines: {changed_lines} > {max_patch_lines}"
        )

    before_sha = hashlib.sha256(before_text.encode("utf-8")).hexdigest()
    after_sha = hashlib.sha256(replacement.encode("utf-8")).hexdigest()
    return {
        "path": target_path,
        "expected_before_sha256": before_sha,
        "replacement_text": replacement,
        "expected_after_sha256": after_sha,
        "changed_lines": changed_lines,
        "reason": proposal["reason"],
        "evidence_plan": list(evidence_plan),
    }


def _gemini_schema(value: Any) -> Any:
    """Adapt the canonical proposal schema to Gemini's supported JSON-Schema subset.

    The canonical post-response validator remains authoritative. Provider-specific
    structured-output limitations must not weaken Saddle's local validation.
    """
    if isinstance(value, dict):
        return {
            key: _gemini_schema(item)
            for key, item in value.items()
            if key not in {"minLength"}
        }
    if isinstance(value, list):
        return [_gemini_schema(item) for item in value]
    return value


class GeminiGenerateContentGateway:
    """Single-provider Gemini adapter; intentionally not a provider framework."""

    def __init__(
        self,
        *,
        model_id: str,
        reasoning_effort: str = "medium",
        endpoint_base: str = "https://generativelanguage.googleapis.com/v1beta/models",
        api_key_env: str = "GEMINI_API_KEY",
        timeout_s: int = 120,
        max_output_tokens: int = 8192,
        transport: Callable[[dict[str, Any], str], dict[str, Any]] | None = None,
    ) -> None:
        normalized_effort = reasoning_effort.strip().upper()
        if normalized_effort not in {"MINIMAL", "LOW", "MEDIUM", "HIGH"}:
            raise ValueError("Gemini reasoning_effort must be minimal, low, medium or high")
        self.model_id = model_id
        self.reasoning_effort = normalized_effort
        self.endpoint_base = endpoint_base.rstrip("/")
        self.api_key_env = api_key_env
        self.timeout_s = timeout_s
        self.max_output_tokens = max_output_tokens
        self._transport = transport or self._http_transport

    @property
    def endpoint(self) -> str:
        encoded_model = urllib.parse.quote(self.model_id, safe="-._")
        return f"{self.endpoint_base}/{encoded_model}:generateContent"

    def _http_transport(self, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "x-goog-api-key": api_key,
                "x-goog-api-client": "saddle-phase4b/0.1",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_s) as response:
                body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raise GatewayResponseError(
                f"Gemini generateContent request failed with HTTP {exc.code}"
            ) from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise GatewayResponseError(
                "Gemini generateContent request failed before a valid response was received: "
                f"{type(exc).__name__}"
            ) from exc
        try:
            value = json.loads(body)
        except json.JSONDecodeError as exc:
            raise GatewayResponseError("Gemini generateContent endpoint returned invalid JSON") from exc
        if not isinstance(value, dict):
            raise GatewayResponseError("Gemini generateContent endpoint returned a non-object payload")
        return value

    @staticmethod
    def _output_text(response: dict[str, Any]) -> str:
        prompt_feedback = response.get("promptFeedback")
        if isinstance(prompt_feedback, dict) and isinstance(prompt_feedback.get("blockReason"), str):
            raise GatewayResponseError(
                f"Gemini response blocked before generation: {prompt_feedback['blockReason']}"
            )

        candidates = response.get("candidates")
        if not isinstance(candidates, list) or not candidates or not isinstance(candidates[0], dict):
            raise GatewayResponseError("Gemini response contains no candidate proposal")
        candidate = candidates[0]
        content = candidate.get("content")
        parts = content.get("parts") if isinstance(content, dict) else None
        chunks: list[str] = []
        if isinstance(parts, list):
            for part in parts:
                if isinstance(part, dict) and isinstance(part.get("text"), str):
                    chunks.append(part["text"])
        if not chunks:
            finish_reason = candidate.get("finishReason")
            suffix = f": {finish_reason}" if isinstance(finish_reason, str) else ""
            raise GatewayResponseError(f"Gemini response contains no text proposal{suffix}")
        return "".join(chunks)

    def generate(
        self,
        *,
        case_id: str,
        target_path: str,
        problem: str,
        case_contract: str,
        target_source: str,
        tests_source: str,
    ) -> ModelResult:
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise CredentialUnavailable(
                f"{self.api_key_env} is not configured in the control-plane environment"
            )

        input_text = (
            f"CASE: {case_id}\n\n"
            f"PROBLEM:\n{problem}\n\n"
            f"CASE CONTRACT:\n{case_contract}\n\n"
            f"ONLY ALLOWED TARGET FILE: {target_path}\n\n"
            f"TARGET SOURCE:\n{target_source}\n\n"
            f"RELEVANT ACCEPTANCE TESTS:\n{tests_source}\n\n"
            "Return the smallest correct full-file replacement for the allowed target. "
            "Do not change tests, request extra scope, request credentials, claim authority, "
            "or describe actions outside the allowed file."
        )
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": input_text}],
                }
            ],
            "systemInstruction": {
                "parts": [
                    {
                        "text": (
                            "You are a coding proposal generator inside Saddle. You may reason freely, "
                            "but you have no execution authority. Produce only the requested structured proposal."
                        )
                    }
                ]
            },
            "generationConfig": {
                "candidateCount": 1,
                "maxOutputTokens": self.max_output_tokens,
                "responseMimeType": "application/json",
                "responseJsonSchema": _gemini_schema(WORKER_PROPOSAL_SCHEMA),
                "thinkingConfig": {
                    "thinkingLevel": self.reasoning_effort,
                    "includeThoughts": False,
                },
            },
            "store": False,
        }

        started = time.monotonic()
        raw = self._transport(payload, api_key)
        latency_ms = round((time.monotonic() - started) * 1000)
        text = self._output_text(raw)
        try:
            proposal = json.loads(text)
        except json.JSONDecodeError as exc:
            raise GatewayResponseError("structured model output is not valid JSON") from exc
        if not isinstance(proposal, dict):
            raise GatewayResponseError("structured model output is not an object")

        usage = raw.get("usageMetadata") if isinstance(raw.get("usageMetadata"), dict) else {}
        return ModelResult(
            model_id=self.model_id,
            proposal=proposal,
            latency_ms=latency_ms,
            usage=ModelUsage(
                input_tokens=(
                    usage.get("promptTokenCount")
                    if isinstance(usage.get("promptTokenCount"), int)
                    else None
                ),
                output_tokens=(
                    usage.get("candidatesTokenCount")
                    if isinstance(usage.get("candidatesTokenCount"), int)
                    else None
                ),
                reasoning_tokens=(
                    usage.get("thoughtsTokenCount")
                    if isinstance(usage.get("thoughtsTokenCount"), int)
                    else None
                ),
            ),
            response_id=raw.get("responseId") if isinstance(raw.get("responseId"), str) else None,
        )
