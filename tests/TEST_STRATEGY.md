# AuctaPay Concilia — TEST_STRATEGY.md

> Detalha o "Como vamos provar" do ACCEPTANCE.md (bloco K). Tier 3.

## Golden cases (referência externa)

Fonte da verdade: `legacy/baseline/baseline_expected.json` (evidence_status: observed_not_approved) → materializados em `tests/fixtures/golden_cases.csv` com colunas intermediárias (dif_valor, datas) — um caso falha em qualquer etapa divergente, não só no total.

Conferência independente (2026-09-03): regra documentada (TRUTH-001) aplicada à mão sobre os insumos, FORA do código legado → 3/3 casos reproduzidos. O harness do CI (`tests/regression/baseline_check.py`) executa o código legado contra a mesma referência externa.

**Tolerância proposta: R$ 0,00 / igualdade exata** — a baseline é determinística. Toda tolerância diferente precisa de aprovação explícita do dono do número (nunca adotada em silêncio).

**GATE (1º /change-number):** validação formal de Rafael Costa sobre golden_cases.csv + expected_exceptions.csv + classificação do T002 (regra confirmada × defeito conhecido) + ratificação/parametrização da tolerância de R$ 5,00.

## Exceções esperadas

`tests/fixtures/expected_exceptions.csv` (EX-01..05). Destaques: EX-01 (pagamento órfão invisível no legado — TRUTH-015) e EX-04 (tolerância sem fonte) BLOQUEIAM publicação/mudança até tratamento.

## Suites por fase

| Fase | Provas |
| --- | --- |
| Baseline (M1 — concluída no /init) | Harness ACC-001 no CI: legado × referência externa; provado pelo PR-armadilha #1 (mudança silenciosa reprovada) |
| Motor novo em modo replicação (M4) | Golden 1:1 contra golden_cases.csv (tolerância R$ 0,00) + exceções de expected_exceptions.csv tratadas |
| Ingestão ERP (M3) | E2E de importação com fixtures; testes de dados (schema, dedupe por event_id/documento, nulls bloqueantes) |
| Integrações provedor (M5 — GATED) | Testes de integração no sandbox; assinatura de webhook válida/inválida |
| SSO e perfis (M6 — GATED) | Autorização por perfil (Financeiro/Cobrança/Auditoria); acesso negado sem Entra ID |
| Relatórios (M7) | Números dos relatórios = golden; aprovação do dono do número |
| Segurança (tier 3, contínuo) | Threat model; secrets fora do código; saneamento antes de importar histórico do fornecedor (TRUTH-014) |

## Regras permanentes

- Golden vigente re-verificado no MESMO ciclo de qualquer refactor do motor.
- Entregável gerado sempre com a MESMA configuração validada nos golden.
- Muda-numero em 3 camadas no /pre-pr: caminho (módulos de regra), conteúdo (constantes/fórmulas), golden before/after.
