# CLAUDE.md — AuctaPay Concilia (Modernização)

Padrão Aucta (repo criado do template; preenchido pelo /init em 2026-09-03). Minimal context for ANY agent session opened in this repo — read before acting.

## Read first (in order)

1. `.project/init-state.md` — orchestration state: what is closed, blocked, and where to resume. Never re-ask what it marks closed.
2. `PROJECT.md` · `TRUTHS.md` · `GLOSSARY.md` · `ACCEPTANCE.md` · `OWNERS.md` — canonical artifacts (problem, current facts/rules, terms, acceptance + golden cases, who decides what).
3. `.project/DATA_CATALOG.md` — every data source: where it lives, sensitivity, freshness.
4. `project-plugin/` — router and workflows. Route requests through it; a change that alters a delivered number goes through /change-number (Muda-numero gate).

## Non-negotiable rules

- **REGRA DE OURO:** the agent only uses/alters files inside the project's OneDrive folder (`Aucta Blueprint Dev AI/inputs/teste 3`) and this repository — exclusively (TRUTH-010).
- Real client data NEVER enters Git; homologação only with masked/synthetic data (TRUTH-008). The bundled mass is 100% synthetic (TRUTH-011).
- `legacy/` is a READ-ONLY characterization snapshot: no refactor, no fixes, no reuse of its code/dependencies until IP/licenças are cleared (TRUTH-005). Observed behavior ≠ approved rule — taxonomy in GLOSSARY.md; T002 is a candidate defect (TRUTH-003).
- The agent executes ALL Git (branch/commit/push/PR/merge) — the consultant never types commands (D6).
- Business approval before merging any Muda-numero change: Rafael Costa (OWNERS.md). Production needs Rafael + Segurança da Informação (TRUTH-009).
- If the vendor's original repo history is ever received: secret-sanitize BEFORE import (TRUTH-014).
- Consultant dialogue in pt-BR per linguagem-consultor (conceitos traduzidos, abertura didática, progresso "Etapa N de X", 1 decisão por pergunta).

## Project facts

- Risk tier: 3 — login corporativo com perfis + integrações centrais (ERP, API, webhooks) + números de conciliação para decisão sobre dados de cliente.
- Ambiente/infra: alvo = Azure da AuctaPay, CONDICIONADO a aprovação formal de arquitetura (TRUTH-012); PostgreSQL previsto; homolog + prod.
- Backup: snapshot do repo em `backups/` na pasta do projeto no OneDrive a cada release; NÃO substitui backup operacional (app+DB), que depende de RPO/RTO (TRUTH-013).

## Router

Entry point: `project-plugin/skills/router/SKILL.md` — classify the demand (type + tier), then run the minimal workflow. Never implement straight from a request: `/start-work` opens every demand and `/pre-pr` closes every one before a PR.

| Demanda | Workflow | Skill |
| --- | --- | --- |
| Abrir qualquer mudança | `/start-work` | `project-plugin/skills/start-work/SKILL.md` |
| Feature funcional (tier 1+) | `/build-feature` | `project-plugin/skills/build-feature/SKILL.md` |
| Bug reproduzível / regressão | `/fix-bug` | `project-plugin/skills/fix-bug/SKILL.md` |
| Mudança de tela / usabilidade | `/ui-change` | `project-plugin/skills/ui-change/SKILL.md` |
| **Mudança de resultado (tier 2+)** | `/change-number` | `project-plugin/skills/change-number/SKILL.md` |
| **Estrutural: SSO, perfis, banco, integrações, deploy (tier 3)** | `/architecture` | `project-plugin/skills/architecture/SKILL.md` |
| Antes de abrir/atualizar PR (sempre) | `/pre-pr` | `project-plugin/skills/pre-pr/SKILL.md` |
| Versão entregue | `/release` | `project-plugin/skills/release/SKILL.md` |
| Troca de sessão/pessoa | `/handoff` | `project-plugin/skills/handoff/SKILL.md` |

Supporting references: `project-plugin/references/pointers.md` (canonical paths + Muda-numero sentinel modules), `project-plugin/references/client-rules.md` (regras inegociáveis), `project-plugin/vendored/MANIFEST.md` (skill stack pointing at the audited copies in `AuctaFerrari/aucta-dev-core` @ `007a7d3` — no local duplication).

**Sentinelas Muda-numero:** `legacy/reconcile.py` · tolerância de R$ 5,00 · critério de aprovação automática · tratamento de pagamento órfão · `tests/fixtures/golden_cases.csv` · `tests/fixtures/expected_exceptions.csv` · `tests/regression/baseline_check.py` · qualquer módulo futuro de matching, parâmetros ou relatórios.

**Gates bloqueados hoje** (detalhe em `.project/init-state.md`): integração com a API do provedor (sem sandbox e spec incompleta) · SSO/perfis (sem configuração Entra ID) · deploy (arquitetura Azure sem aprovação formal) · primeiro `/change-number` (validação formal de Rafael Costa sobre golden, exceções e tolerância).
