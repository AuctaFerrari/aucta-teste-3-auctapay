---
name: router
description: Control plane do projeto AuctaPay Concilia. Use ao receber qualquer pedido de mudança neste repositório para classificar a demanda (tipo + tier) e encaminhar ao workflow mínimo suficiente. Também usar quando o consultor pedir "o que fazer agora" ou não souber qual rotina aplicar.
---

# Router — AuctaPay Concilia (tier 3)

Classify first, then route. Load only what the chosen step needs (progressive disclosure). Expose to the consultant ONLY judgment questions; every mechanical action — including all Git (branch/commit/push/PR/merge) — is executed by the agent (D6).

**Language rule:** consultant dialogue in pt-BR per `linguagem-consultor` (concept translation on first use, didactic stage opening, `Etapa N de X`, one decision per question). Instructions here in English.

## Step 1 — read the minimum context

`PROJECT.md` + `TRUTHS.md` + the active Issue/Spec. Nothing else by default. Paths in `../../references/pointers.md`.

## Step 2 — classify the demand

| Tipo | Sinais | Tier de partida |
| --- | --- | --- |
| Editorial/doc | texto, rótulo, README, comentário | 0 |
| Visual/UI | tela, layout, usabilidade, acessibilidade | 0–1 |
| Funcional | fluxo, filtro, importação, relatório sem mudar número | 1 |
| **Resultado (Muda-numero)** | regra de matching, tolerância, critério de aprovação, número em relatório | **2** |
| Estrutural | autenticação/Entra ID, perfis, banco, integração ERP/API/webhook, deploy, migração | **3** |

**Sentinelas deste projeto — qualquer toque nestes pontos força tier ≥ 2 e o gate Muda-numero:**
`legacy/reconcile.py` (regra observada) · tolerância de R$ 5,00 · critério de aprovação automática · tratamento de pagamento órfão · `tests/fixtures/golden_cases.csv` · `tests/fixtures/expected_exceptions.csv` · `tests/regression/baseline_check.py` · qualquer módulo futuro de matching, parâmetros ou relatórios.

## Step 3 — route

| Tier / tipo | Caminho |
| --- | --- |
| 0 | Caminho leve: branch → mudança → inspeção → /pre-pr → PR |
| 1 funcional | `/start-work` → `/build-feature` → `/pre-pr` |
| 1 visual | `/start-work` → `/ui-change` → `/pre-pr` |
| bug reproduzível | `/start-work` → `/fix-bug` → `/pre-pr` |
| 2 (resultado) | `/start-work` → **`/change-number`** → `/pre-pr` (aprovação de Rafael Costa antes do merge) |
| 3 (estrutural) | `/start-work` → **`/architecture`** (ADR + threat model + segundo revisor) → `/pre-pr` |
| entrega | `/release` |
| troca de sessão/pessoa | `/handoff` |

`/pre-pr` roda SEMPRE antes de abrir ou atualizar PR. `/start-work` abre qualquer demanda.

## Step 4 — project guardrails (check before acting)

1. **`legacy/` é read-only** — snapshot de caracterização. Nenhum refactor, correção ou reuso do seu código/dependências até liberação de IP/licenças (TRUTH-005). Alterar `legacy/` só para preservar baseline, nunca para "melhorar".
2. **Comportamento observado ≠ regra aprovada.** Ao tocar qualquer regra, declarar a classificação (observado / confirmada / hipótese / defeito) — taxonomia no GLOSSARY.
3. **Dado real nunca no Git**; homologação só com massa mascarada/sintética (TRUTH-008).
4. **Gates bloqueados hoje** (ver `.project/init-state.md`): integração com a API do provedor (sem sandbox nem spec completa), SSO/perfis (sem configuração Entra ID), deploy (arquitetura sem aprovação formal). Uma demanda que caia nesses gates para e reporta o blocker — não improvisa credencial nem implementa às cegas.
5. **Primeiro /change-number exige** validação formal de Rafael Costa sobre golden cases, exceções esperadas e a tolerância de R$ 5,00.
