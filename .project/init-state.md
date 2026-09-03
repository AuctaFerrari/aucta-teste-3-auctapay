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
| init-repo | em_andamento | 2026-09-03 | itens 1,2,4,5,9 concluídos; snapshot do legado + harness + CLAUDE.md (6895c92); branch baseline/v0 criada; pendentes: tag (ASSISTED), proteção main (ASSISTED), PR-armadilha do CI, Project (opcional) |
| init-data | pendente | | ZIP extraído e lido na sessão; catálogo formal pendente |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-repo — checklist

| Item | Status | Evidência / pendência |
| --- | --- | --- |
| 1. Repo privado do template | concluida | bootstrap assistido "Use this template" (2 cliques), private=true, arquivos do template presentes |
| 2. Estrutura de pastas | concluida | legacy/ (snapshot read-only, 14 arquivos), tests/regression/ — commit 6895c92; nada apagado |
| 3. Baseline (branch + tag) | em_andamento | branch `baseline/v0` criada (AUTO) apontando p/ 6895c92; TAG `baseline-v0` = ASSISTED, aguardando consultor |
| 4. Templates + CODEOWNERS | concluida | CODEOWNERS gerado do OWNERS.md (@AuctaFerrari); issue/PR templates vieram do template |
| 5. Labels de governança | concluida | Action bootstrap-labels rodou; validado por amostragem (muda-numero, risco-3) |
| 6. Proteção da main | em_andamento | ASSISTED, aguardando consultor; validação = push direto rejeitado; protocolo de exceção do plano Free se "Not enforced" |
| 7. GitHub Project | pendente | opcional; ASSISTED |
| 8. CI + validação | em_andamento | run-checks.sh adaptado (harness ACC-001, invocado com bash); PR-armadilha após proteção |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG do template; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido (regra de ouro TRUTH-010, tier 3, infra, legacy read-only); Router aguarda init-plugin |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | PROJECT.md; v1 replica matching fielmente; reutilização de código/deps suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = aprovação conjunta Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md; aceite por comentário de aprovação no PR (TRUTH-009) |
| E. Dados e fontes (inventário) | concluida | inventário: ZIP legado (código+massa+docs), ERP (a nomear), API provedor (a nomear), webhooks; detalhamento no init-data |
| F. Segurança e privacidade | concluida | Entra ID (TRUTH-007); homolog só mascarado/sintético (TRUTH-008); saneamento de histórico (TRUTH-014) |
| G. IP e licenças | bloqueada | titularidade não confirmada; reutilização suspensa — blocker ativo (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado a aprovação formal (TRUTH-012); PostgreSQL previsto |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO seguem como blockers |
| J. Repositório e governança | em_andamento | ver checklist init-repo acima |
| K. Estratégia de testes | concluida | ACCEPTANCE.md; harness ACC-001 já roda no CI |
| L. Conhecimento canônico | concluida | TRUTHS.md (14) + GLOSSARY.md com taxonomia de evidência |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | concluida | backups/ por release no OneDrive (TRUTH-013); sustentação A DEFINIR (OWNERS.md) |
| O. Baseline | em_andamento | snapshot commitado (6895c92) + branch baseline/v0 + harness verde local; falta tag baseline-v0 (ASSISTED) |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.
- Snapshot do legado versionado no repo PRIVADO como preservação interna de baseline (exigência do consultor); publicação/redistribuição externa segue PROIBIDA (TRUTH-005).

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 resultados de `baseline_expected.json` com Python padrão; harness em `tests/regression/baseline_check.py` (verde local).
- **Regra de matching observada**: mesmo `documento` E dif. valor ≤ R$ 5,00 → APPROVED. Tolerância R$ 5,00 = número mágico sem fonte. **T002 (dif. R$ 4,00, pago após vencimento) aprovado — defeito candidato** (known_concern).
- **Dependências declaradas mas NÃO usadas**: `requests`, `fuzzywuzzy`, `legacy-match-sdk` não importadas; baseline não depende do SDK sem licença.
- **Higiene de segredos**: snapshot atual só com placeholders (grep limpo); histórico do repo original do fornecedor exige saneamento antes de eventual importação (TRUTH-014).
- **Fragilidades**: sem autenticação, `debug=True`, secret demo hardcoded, SQLite ao lado do código, ambiente não pinado, sem testes.
- **Spec da API do provedor parcial**: auth, assinatura, paginação, rate limits e erros pendentes.

## Premissas

- Massa de dados no ZIP é 100% sintética (declaração do consultor + README do ZIP).
- Repo privado no plano Free: proteção de main possivelmente "Not enforced" — decisão formal na configuração do item 6; produção real exige org + plano Team.
- Owner funcional = Rafael Costa (Controladoria) — adotado por inferência; confirmar com o sponsor.
- Nomes do ERP e do provedor de pagamentos ainda não informados — DATA_CATALOG registrará "a nomear".

## Blockers

- **Credenciais do sandbox da API do provedor** — bloqueia: integrações (M5), ACC-004/005. Ação: AuctaPay solicitar. Owner: Mariana Torres.
- **Configuração do login corporativo (Entra ID)** — bloqueia: SSO/perfis (M6), ACC-007, release em homolog. Ação: TI AuctaPay. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado** — bloqueia: reutilização do legado (NÃO bloqueia baseline, diagnóstico, reescrita limpa). Ação: contrato + revisão jurídica. Owner: Mariana Torres.
- **Spec da API do provedor incompleta** — bloqueia: desenho final da integração (M5). Ação: AuctaPay obter spec completa.
- **Aprovação formal da arquitetura Azure** — bloqueia: primeiro deploy e backup operacional (RPO/RTO). Owner: SI + Rafael Costa.
- **Sustentação pós-entrega sem dono** — bloqueia: release final/sustentação. Owner da decisão: Mariana Torres.

## Achados de ambiente

- Conector GitHub: NÃO cria repositórios (403); cria branches, pushes e labels-via-Action OK; secret scanning API indisponível (sem Advanced Security) — grep local aplicado.
- Conector M365: operacional; NÃO lê ZIP (MIME) — ZIP recebido por anexo na conversa.

## Retomada

- Próximo passo: consultor cria a tag `baseline-v0` e a proteção da main (instruções na conversa); agente valida com push-teste e PR-armadilha do CI; depois init-data.
