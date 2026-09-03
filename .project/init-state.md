---
init_version: 0.3.0
projeto: "AuctaPay Concilia — Modernização"
repo: "AuctaFerrari/aucta-teste-3-auctapay"
risk_tier: 3
status_geral: em_andamento
iniciado_em: 2026-09-03
atualizado_em: 2026-09-03
---

# Estado do /init — AuctaPay Concilia — Modernização

Arquivo de estado do Aucta Dev Init. Registra **progresso**, não conteúdo: respostas e decisões vivem nos artefatos canônicos (PROJECT.md, TRUTHS.md, GLOSSARY.md, ACCEPTANCE.md, OWNERS.md, DATA_CATALOG.md). Atualizado e commitado pelo agente a cada avanço material.

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | concluida | 2026-09-03 | Artefatos canônicos commitados (a8b6183): PROJECT, TRUTHS (14), GLOSSARY, ACCEPTANCE (ACC-001..008), OWNERS; tier 3 |
| init-repo | pendente | | repo criado via template (bootstrap assistido 2026-09-03) |
| init-data | pendente | | ZIP extraído e lido na sessão; catálogo formal pendente |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | PROJECT.md; v1 replica matching fielmente; reutilização de código/deps suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = aprovação conjunta Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md; aceite por comentário de aprovação no PR (TRUTH-009) |
| E. Dados e fontes (inventário) | concluida | inventário: ZIP legado (código+massa+docs), ERP (sistema a nomear), API provedor (a nomear), webhooks; detalhamento no init-data |
| F. Segurança e privacidade | concluida | Entra ID confirmado (TRUTH-007); homolog só mascarado/sintético (TRUTH-008); saneamento de histórico do fornecedor (TRUTH-014) |
| G. IP e licenças | bloqueada | LICENSE_STATUS.md: titularidade não confirmada; reutilização suspensa — blocker ativo (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md (arquitetura em uma página); Azure condicionado a aprovação formal (TRUTH-012); PostgreSQL previsto |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO seguem como blockers |
| J. Repositório e governança | pendente | executado no init-repo |
| K. Estratégia de testes | concluida | ACCEPTANCE.md "Como vamos provar": golden desde a baseline, regressão, E2E por perfil, threat model tier 3 |
| L. Conhecimento canônico | concluida | TRUTHS.md (14) + GLOSSARY.md com taxonomia de evidência |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | concluida | backups/ por release no OneDrive (TRUTH-013); sustentação pós-entrega A DEFINIR (pendência em OWNERS.md) |
| O. Baseline | em_andamento | snapshot limpo validado e harness reproduzido na sessão; commit da baseline + tag no init-repo |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: `reconcile_records` sobre a massa sintética reproduz 3/3 resultados de `baseline/baseline_expected.json` (T001 APPROVED, T002 APPROVED, T003 OPEN) usando apenas Python padrão — sem instalar dependências.
- **Regra de matching observada**: mesmo `documento` E diferença de valor ≤ R$ 5,00 → APPROVED automático. Tolerância de R$ 5,00 é número mágico sem fonte. **T002 (dif. R$ 4,00, pago após o vencimento) é aprovado automaticamente — comportamento observado, defeito candidato, NÃO regra aprovada** (known_concern do próprio ZIP).
- **Dependências declaradas mas NÃO usadas no código**: `requests`, `fuzzywuzzy` e `legacy-match-sdk` não são importadas por nenhum módulo. A baseline NÃO depende do SDK sem licença.
- **Higiene de segredos**: snapshot atual contém apenas placeholders (grep local limpo). `production_notes.txt` alerta que o HISTÓRICO do repo original do fornecedor teve token de homologação (revogado, não saneado) — se recebido, sanear antes de importar; acionar SI (TRUTH-014).
- **Fragilidades do legado**: sem autenticação, `debug=True`, secret hardcoded de demonstração, SQLite ao lado do código, ambiente não pinado, sem testes automatizados.
- **Spec da API do provedor é parcial**: autenticação, assinatura de webhook, paginação, rate limits e erros pendentes.

## Premissas

- Massa de dados no ZIP é 100% sintética (declaração do consultor + README do ZIP).
- Repo privado no plano Free: proteção de main "Not enforced" — premissa de risco dos Testes 1 e 2; produção real exige org + plano Team.
- Owner funcional = Rafael Costa (Controladoria) — adotado por inferência; confirmar com o consultor/sponsor.
- Nomes do ERP e do provedor de pagamentos ainda não informados — catálogo do init-data registrará como "a nomear" até resposta.

## Blockers

- **Credenciais do sandbox da API do provedor** — não recebidas. Bloqueia: integrações (M5) e ACC-004/005. Ação: AuctaPay solicitar ao provedor. Owner: Mariana Torres.
- **Configuração do login corporativo (Entra ID)** — não recebida. Bloqueia: SSO/perfis (M6), ACC-007 e release em homologação. Ação: TI AuctaPay fornecer tenant/client. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado não verificadas** — bloqueia: reutilização de qualquer trecho/dependência do legado (NÃO bloqueia baseline, diagnóstico nem reescrita limpa). Ação: localizar contrato do fornecedor; revisão jurídica. Owner: Mariana Torres.
- **Spec da API do provedor incompleta** — bloqueia: desenho final da integração (M5). Ação: AuctaPay obter spec completa.
- **Aprovação formal da arquitetura Azure** — pendente. Bloqueia: primeiro deploy em homolog/prod e estratégia de backup operacional (RPO/RTO). Owner: Segurança da Informação + Rafael Costa.
- **Sustentação pós-entrega sem dono** — bloqueia: release final/sustentação (não bloqueia desenvolvimento). Owner da decisão: Mariana Torres.

## Achados de ambiente

- Conector GitHub desta sessão NÃO cria repositórios (403); secret scanning via API indisponível (sem Advanced Security no plano Free) — varredura local por grep aplicada.
- Conector M365 operacional; NÃO lê arquivos ZIP (validação de MIME) — ZIP recebido por anexo na conversa.

## Retomada

- Próximo passo: Etapa 2 de 5 — init-repo (governança do repositório, proteção da main, CODEOWNERS, CI; commit do snapshot do legado + tag baseline + harness — bloco O).
