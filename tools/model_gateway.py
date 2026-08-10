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


class OpenAIResponsesGateway:
    """Single-provider adapter, intentionally not a generalized provider framework."""

    def __init__(
        self,
        *,
        model_id: str,
        reasoning_effort: str = "medium",
        endpoint: str = "https://api.openai.com/v1/responses",
        api_key_env: str = "OPENAI_API_KEY",
        timeout_s: int = 120,
        max_output_tokens: int = 8192,
        transport: Callable[[dict[str, Any], str], dict[str, Any]] | None = None,
    ) -> None:
        self.model_id = model_id
        self.reasoning_effort = reasoning_effort
        self.endpoint = endpoint
        self.api_key_env = api_key_env
        self.timeout_s = timeout_s
        self.max_output_tokens = max_output_tokens
        self._transport = transport or self._http_transport

    def _http_transport(self, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_s) as response:
                body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raise GatewayResponseError(f"OpenAI Responses request failed with HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise GatewayResponseError(
                f"OpenAI Responses request failed before a valid response was received: {type(exc).__name__}"
            ) from exc
        try:
            value = json.loads(body)
        except json.JSONDecodeError as exc:
            raise GatewayResponseError("OpenAI Responses endpoint returned invalid JSON") from exc
        if not isinstance(value, dict):
            raise GatewayResponseError("OpenAI Responses endpoint returned a non-object payload")
        return value

    @staticmethod
    def _output_text(response: dict[str, Any]) -> str:
        chunks: list[str] = []
        for item in response.get("output", []):
            if not isinstance(item, dict) or item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if (
                    isinstance(content, dict)
                    and content.get("type") == "output_text"
                    and isinstance(content.get("text"), str)
                ):
                    chunks.append(content["text"])
        if not chunks:
            raise GatewayResponseError("OpenAI response contains no output_text proposal")
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
            "model": self.model_id,
            "store": False,
            "reasoning": {"effort": self.reasoning_effort},
            "max_output_tokens": self.max_output_tokens,
            "instructions": (
                "You are a coding proposal generator inside Saddle. You may reason freely, "
                "but you have no execution authority. Produce only the requested structured proposal."
            ),
            "input": input_text,
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "saddle_worker_proposal",
                    "strict": True,
                    "schema": WORKER_PROPOSAL_SCHEMA,
                }
            },
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

        usage = raw.get("usage") if isinstance(raw.get("usage"), dict) else {}
        output_details = (
            usage.get("output_tokens_details")
            if isinstance(usage.get("output_tokens_details"), dict)
            else {}
        )
        return ModelResult(
            model_id=self.model_id,
            proposal=proposal,
            latency_ms=latency_ms,
            usage=ModelUsage(
                input_tokens=usage.get("input_tokens") if isinstance(usage.get("input_tokens"), int) else None,
                output_tokens=usage.get("output_tokens") if isinstance(usage.get("output_tokens"), int) else None,
                reasoning_tokens=(
                    output_details.get("reasoning_tokens")
                    if isinstance(output_details.get("reasoning_tokens"), int)
                    else None
                ),
            ),
            response_id=raw.get("id") if isinstance(raw.get("id"), str) else None,
        )
