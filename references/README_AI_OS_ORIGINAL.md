# AI Engineering OS

Repo-agnostyczna warstwa konfiguracji dla projektu, w którym AI ma działać jak
Senior AI Engineer / AI Systems Architect, a nie tylko generator kodu.

## Cel

System ma:
- najpierw zrozumieć projekt i intencję produktu,
- dobrać właściwy poziom automatyzacji: kod -> model+tools -> agent -> multi-agent,
- dobierać modele per workload, a nie "jeden model do wszystkiego",
- wyszukiwać aktualne narzędzia i integracje w oficjalnych źródłach,
- wykorzystywać MCP tam, gdzie upraszcza integracje,
- wersjonować decyzje, prompty i konfigurację,
- mierzyć jakość przez evale zamiast subiektywnego "wydaje się lepiej",
- kontrolować koszt, latency, bezpieczeństwo i autonomię.

## Jak wdrożyć

1. Skopiuj zawartość tego pakietu do katalogu głównego repozytorium.
2. Uruchom:
   `python tools/ai_os_check.py`
3. Wygeneruj pierwszy deterministyczny audyt repo:
   `python tools/ai_project_audit.py --root . --out docs/AI_AUDIT.generated.md`
4. Uruchom wybranego coding agenta z promptem:
   `prompts/BOOTSTRAP_AUDIT.md`
5. Agent powinien zaktualizować:
   - `docs/AI_ARCHITECTURE.md`
   - `docs/AI_TOOLING.md`
   - `docs/AI_DECISIONS.md`
   - `config/model-routing.json`
   - `config/tool-registry.json`
   - `evals/cases.jsonl`
6. Przed wdrażaniem większych zmian uruchamiaj evale i zapisuj baseline.

## Najważniejsza zasada

Nie maksymalizujemy ilości AI. Maksymalizujemy skuteczność produktu.

Preferowana drabina:
1. deterministyczny kod,
2. pojedynczy model,
3. model + narzędzia,
4. pojedynczy agent,
5. multi-agent,

i przechodzimy wyżej tylko wtedy, gdy niższy poziom nie wystarcza.
