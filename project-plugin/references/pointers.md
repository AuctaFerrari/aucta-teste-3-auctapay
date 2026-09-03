# Pointers — artefatos canônicos do AuctaPay Concilia

Ordem de leitura na abertura de sessão: **PROJECT.md → TRUTHS.md → Issue/Spec ativa**. Nada além disso por padrão (progressive disclosure, blueprint 6.5); o resto entra quando a tarefa pedir.

| Artefato | Caminho | Para quê |
| --- | --- | --- |
| PROJECT.md | `PROJECT.md` | Objetivo, escopo, tier 3, arquitetura em uma página (legado → alvo) |
| TRUTHS.md | `TRUTHS.md` | Fatos e regras vigentes (15) — inclui regra observada de matching e limites de reuso do legado |
| GLOSSARY.md | `GLOSSARY.md` | Vocabulário + taxonomia de evidência (observado / confirmada / hipótese / defeito) |
| ACCEPTANCE.md | `ACCEPTANCE.md` | ACC-001..008, marcos M1–M7, estratégia de provas |
| OWNERS.md | `OWNERS.md` | Quem valida número (Rafael Costa), quem autoriza produção (Rafael + SI) |
| DATA_CATALOG.md | `.project/DATA_CATALOG.md` | 7 fontes, sensibilidade, o que está `não validado` |
| Estado do /init | `.project/init-state.md` | O que está fechado, premissas, blockers segmentados, retomada |
| Golden cases | `tests/fixtures/golden_cases.csv` | GC-01..03 com colunas intermediárias; tolerância R$ 0,00 |
| Exceções esperadas | `tests/fixtures/expected_exceptions.csv` | EX-01..05 (EX-01 e EX-04 bloqueiam publicação) |
| Estratégia de testes | `tests/TEST_STRATEGY.md` | Suites por fase e gates |
| Harness da baseline | `tests/regression/baseline_check.py` | ACC-001 — roda no CI a cada PR |
| Snapshot do legado | `legacy/` (tag `baseline-v0`) | Referência de comportamento — **read-only** |
| Checks do CI | `.github/ci/run-checks.sh` | O que a conferência automática executa |

## Módulos-sentinela (Muda-numero, camada de caminho — D4)

`legacy/reconcile.py` · `tests/fixtures/golden_cases.csv` · `tests/fixtures/expected_exceptions.csv` · `tests/regression/baseline_check.py` · qualquer módulo futuro de matching, parâmetros de conciliação ou geração de relatórios.
