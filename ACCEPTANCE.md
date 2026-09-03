# AuctaPay Concilia — ACCEPTANCE.md

> Critérios de aceite, definição de pronto e estratégia de provas (blocos D e K). Critérios são testáveis; cada um pode virar caso de teste.

## Entrega

**Formato:** aplicação web interna (multiusuário)
**Ambiente alvo:** homologação e produção na nuvem Azure da AuctaPay (condicionado a aprovação formal de arquitetura — TRUTH-012)
**Mecanismo de aprovação:** comentário de aprovação no PR (aceite por entrega); produção exige aprovação conjunta Rafael Costa + Segurança da Informação (TRUTH-009)

## Critérios de aceite

| # | Critério (testável) | Como provar |
| --- | --- | --- |
| ACC-001 | A baseline do legado é preservada e reproduzível a partir do repositório (tag + harness) | Execução do harness reproduz 3/3 resultados de baseline_expected.json |
| ACC-002 | O motor de matching da nova solução, em modo replicação, reproduz 100% dos golden cases da baseline sobre a massa sintética | Suite de regressão golden (before/after) — **GATE: aprovação funcional das regras (M3)** |
| ACC-003 | Títulos do ERP são importados e registrados no banco com trilha (quem, quando, origem) | Teste E2E de ingestão com massa sintética (GATE: estrutura/extração do ERP) |
| ACC-004 | Webhooks do provedor são recebidos apenas com assinatura válida; inválidos são rejeitados e logados; reenvio do mesmo evento não duplica efeito (idempotência por `event_id`) | Teste de integração (GATE: spec completa + credenciais sandbox) |
| ACC-005 | Consulta à API do provedor funciona no sandbox com tratamento de erros e paginação | Teste de integração (GATE: credenciais sandbox) |
| ACC-006 | Aprovação manual de match registra usuário, data/hora e justificativa, visíveis para Auditoria | Teste E2E por perfil |
| ACC-007 | Acesso somente via Entra ID; cada perfil (Financeiro, Cobrança, Auditoria) vê apenas suas funções | Teste de autorização por perfil (GATE: configuração SSO + matriz RBAC aprovada) |
| ACC-008 | Relatórios de conciliação batem com os golden cases; nenhuma publicação com divergência não explicada e não aprovada | Golden + validação do dono do número |
| ACC-009 | O mapa de regras do legado classifica cada comportamento observado como regra confirmada, hipótese ou defeito conhecido, com decisão registrada de quem valida número | Documento de caracterização aprovado por Rafael Costa (marco M2 → gate M3) |

## Definição de pronto

- Critérios de aceite do escopo entregue atendidos e demonstrados.
- Testes proporcionais ao risco executados e verdes; golden cases re-verificados no mesmo ciclo de qualquer refactor do motor.
- Gate Muda-numero aplicado a toda mudança que altere matching, tolerâncias ou relatórios.
- Documentação que ficaria incorreta atualizada no mesmo ciclo.
- Entregável gerado sempre com a MESMA configuração validada nos golden cases.

## Marcos

Sequência corrigida em 2026-09-03: **caracterizar não é especificar, e especificar não é reescrever.** A caracterização (M2) descreve o que o legado faz; a especificação (M4) e a reescrita (M5) só começam depois da aprovação funcional das regras, golden cases, exceções e tolerâncias (M3).

| Marco | Conteúdo | Situação | Data alvo |
| --- | --- | --- | --- |
| M1 — Baseline preservada | Snapshot do legado versionado (`legacy/`), tag `baseline-v0`, harness de reprodução verde | **CONCLUÍDO no /init** | 2026-09-03 |
| M2 — Caracterização das regras do legado | Mapa das regras observadas com evidência, proposta de classificação (confirmada / hipótese / defeito), lista de lacunas e perguntas ao dono do número. **Sem código, sem especificação de solução.** | **LIBERADO** | a definir |
| M3 — Aprovação funcional das regras | Rafael Costa decide, item a item: classificação de cada comportamento, golden cases, exceções esperadas e tolerâncias. Registro na Issue + TRUTHS. | **GATE** — bloqueia M4 e M5 | a definir |
| M4 — Especificação do motor | Comportamento-alvo e critérios de aceite do motor em modo replicação, derivados das regras APROVADAS em M3 | Depende de M3 | a definir |
| M5 — Reescrita limpa do motor (modo replicação) | Implementação nova (sem herdar código do legado) reproduzindo 100% dos golden aprovados — ACC-002 | Depende de M4 | a definir |
| M6 — Ingestão do ERP | Importação de títulos com trilha em PostgreSQL — ACC-003 | GATE: estrutura/extração do ERP | a definir |
| M7 — Integrações com o provedor | API + webhooks com assinatura e idempotência — ACC-004/005 | GATE: sandbox + spec completa | a definir |
| M8 — SSO e perfis | Entra ID + autorização por perfil — ACC-007 | GATE: configuração Entra ID + matriz RBAC | a definir |
| M9 — Relatórios e aceite | Relatórios validados pelo dono do número — ACC-006/008 | Depende de M5–M8 | a definir |
| M10 — Deploy em homologação/produção | Publicação com aprovação conjunta | GATE: arquitetura Azure aprovada + RPO/RTO definidos | a definir |

## Como vamos provar (estratégia de testes — bloco K)

**Risk tier do projeto:** 3

| Tipo | Aplicação neste projeto |
| --- | --- |
| Golden cases | Obrigatórios ANTES de qualquer mudança no motor: partem dos 3 casos da baseline, que preservam o comportamento OBSERVADO da `baseline-v0` (T002 aprovado por aproximação e P003 órfão ignorado) e são ratificados/ampliados em M3; referência externa = baseline_expected.json + decisão de Rafael Costa |
| Regressão | Golden re-executados em todo PR que toque motor, parâmetros ou relatórios (camada 3 do Muda-numero); golden vigente re-verificado no mesmo ciclo de refactors |
| Smoke / E2E | Fluxos principais por perfil: importar → casar → tratar divergência → aprovar → relatório |
| Dados | Schema, duplicidade (`event_id`), mascaramento de PII em fixtures e homologação, retenção conforme política a definir |
| Integração | API do provedor e webhooks no sandbox, incluindo replay do mesmo `event_id` (GATE: credenciais + spec completa) |
| Segurança | Threat model (tier 3, a produzir em `/architecture`): validação de assinatura de webhook, RBAC por perfil, PII em logs, secrets fora do código, saneamento antes de importar histórico do fornecedor (TRUTH-014) |
| Migração e rollback | Plano de migração de dados do legado (se houver) e rollback por release — a definir no primeiro `/architecture` |

Cobertura consolidada dos temas de tier 3: `.project/CHECKLIST_TIER3.md`.
