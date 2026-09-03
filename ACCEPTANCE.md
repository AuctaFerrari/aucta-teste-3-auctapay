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
| ACC-002 | O motor de matching da nova solução, em modo replicação, reproduz 100% dos golden cases da baseline sobre a massa sintética | Suite de regressão golden (before/after) |
| ACC-003 | Títulos do ERP são importados e registrados no banco com trilha (quem, quando, origem) | Teste E2E de ingestão com massa sintética |
| ACC-004 | Webhooks do provedor são recebidos apenas com assinatura válida; inválidos são rejeitados e logados | Teste de integração (GATE: spec completa + credenciais sandbox) |
| ACC-005 | Consulta à API do provedor funciona no sandbox com tratamento de erros e paginação | Teste de integração (GATE: credenciais sandbox) |
| ACC-006 | Aprovação manual de match registra usuário, data/hora e justificativa, visíveis para Auditoria | Teste E2E por perfil |
| ACC-007 | Acesso somente via Entra ID; cada perfil (Financeiro, Cobrança, Auditoria) vê apenas suas funções | Teste de autorização por perfil (GATE: configuração SSO) |
| ACC-008 | Relatórios de conciliação batem com os golden cases; nenhuma publicação com divergência não explicada e não aprovada | Golden + validação do dono do número |

## Definição de pronto

- Critérios de aceite do escopo entregue atendidos e demonstrados.
- Testes proporcionais ao risco executados e verdes; golden cases re-verificados no mesmo ciclo de qualquer refactor do motor.
- Gate Muda-numero aplicado a toda mudança que altere matching, tolerâncias ou relatórios.
- Documentação que ficaria incorreta atualizada no mesmo ciclo.
- Entregável gerado sempre com a MESMA configuração validada nos golden cases.

## Marcos

| Marco | Conteúdo | Data alvo |
| --- | --- | --- |
| M1 — Baseline preservada | Snapshot do legado versionado, tag baseline, harness de reprodução verde | a definir |
| M2 — Regras classificadas | Regras do legado classificadas (observado/confirmada/hipótese/defeito) com Rafael Costa; golden cases ampliados | a definir |
| M3 — Ingestão ERP | Importação de títulos com trilha em PostgreSQL | a definir |
| M4 — Motor em modo replicação | Matching novo reproduz golden 100% | a definir |
| M5 — Integrações provedor | API + webhooks (GATE: sandbox + spec) | a definir |
| M6 — SSO e perfis | Entra ID + autorização por perfil (GATE: configuração SSO) | a definir |
| M7 — Relatórios e aceite | Relatórios validados pelo dono do número | a definir |

## Como vamos provar (estratégia de testes — bloco K)

**Risk tier do projeto:** 3

| Tipo | Aplicação neste projeto |
| --- | --- |
| Golden cases | Obrigatórios ANTES de qualquer mudança no motor: partem dos 3 casos da baseline (incluindo T002 como caracterização de defeito candidato) e são ampliados com o dono do número no M2; referência externa = baseline_expected.json + validação de Rafael Costa |
| Regressão | Golden re-executados em todo PR que toque motor, parâmetros ou relatórios (camada 3 do Muda-numero); golden vigente re-verificado no mesmo ciclo de refactors |
| Smoke / E2E | Fluxos principais por perfil: importar → casar → tratar divergência → aprovar → relatório |
| Dados | Schema, duplicidade (event_id), mascaramento de PII em fixtures e homologação |
| Integração | API do provedor e webhooks no sandbox (GATE: credenciais + spec completa) |
| Segurança | Threat model (tier 3): validação de assinatura de webhook, autorização por perfil, secrets fora do código, saneamento antes de importar histórico do fornecedor (TRUTH-014) |
