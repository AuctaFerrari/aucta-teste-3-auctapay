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

Arquivo de estado do Aucta Dev Init. Registra **progresso**, não conteúdo: respostas e decisões vivem nos artefatos canônicos (PROJECT.md, TRUTHS.md, GLOSSARY.md, ACCEPTANCE.md, OWNERS.md, DATA_CATALOG.md). Atualizado e commitado pelo agente a cada avanço material. **Com a main protegida, atualizações de estado passam por PR.**

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | concluida | 2026-09-03 | Artefatos canônicos (a8b6183): PROJECT, TRUTHS (14), GLOSSARY, ACCEPTANCE (ACC-001..008), OWNERS; tier 3 |
| init-repo | concluida | 2026-09-03 | Governança validada NA PRÁTICA: push direto 409; PR-armadilha #1 com check `checks` FAILURE e merge "blocked"; tag baseline-v0 → 6895c92 |
| init-data | pendente | | ZIP extraído e lido na sessão; catálogo formal é o próximo passo |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-repo — checklist

| Item | Status | Evidência / pendência |
| --- | --- | --- |
| 1. Repo privado do template | concluida | bootstrap assistido (2 cliques), private=true, arquivos do template presentes |
| 2. Estrutura de pastas | concluida | legacy/ (snapshot read-only, 14 arquivos), tests/regression/ — commit 6895c92; nada apagado |
| 3. Baseline (branch + tag) | concluida | branch `baseline/v0` (AUTO) + tag/release `baseline-v0` (ASSISTED) — ambos → 6895c92, diff vs ZIP vazio |
| 4. Templates + CODEOWNERS | concluida | CODEOWNERS gerado do OWNERS.md (@AuctaFerrari); issue/PR templates do template |
| 5. Labels de governança | concluida | Action bootstrap-labels; validado por amostragem (muda-numero, risco-3) |
| 6. Proteção da main | concluida | Ruleset `protecao-main` ACTIVE (consultor), bypass vazia, approvals=0 (consultor solo); **validado por push direto REJEITADO (409 "Changes must be made through a pull request")** |
| 7. GitHub Project | pendente | OPCIONAL — consultor cria se quiser board (Projects → New project → Board) |
| 8. CI + validação (T2.4) | concluida | PR-armadilha #1 (tolerância 5,00→3,00): check `checks` rodou e REPROVOU em 4s; merge "blocked"; PR fechado sem merge. O harness pegou a mudança silenciosa de número |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido; Router aguarda init-plugin |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | PROJECT.md; v1 replica matching fielmente; reutilização de código/deps suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = aprovação conjunta Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md; aceite por comentário de aprovação no PR (TRUTH-009) |
| E. Dados e fontes (inventário) | concluida | ZIP legado + ERP (a nomear) + API provedor (a nomear) + webhooks; detalhamento no init-data |
| F. Segurança e privacidade | concluida | Entra ID (TRUTH-007); homolog só mascarado/sintético (TRUTH-008); saneamento de histórico (TRUTH-014) |
| G. IP e licenças | bloqueada | titularidade não confirmada; reutilização suspensa — blocker ativo (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado a aprovação formal (TRUTH-012); PostgreSQL previsto |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO seguem como blockers |
| J. Repositório e governança | concluida | checklist init-repo acima; proteção validada na prática |
| K. Estratégia de testes | concluida | ACCEPTANCE.md; harness ACC-001 rodando no CI e provado pelo PR #1 |
| L. Conhecimento canônico | concluida | TRUTHS.md (14) + GLOSSARY.md com taxonomia de evidência |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | concluida | backups/ por release no OneDrive (TRUTH-013); sustentação A DEFINIR (OWNERS.md) |
| O. Baseline | concluida | snapshot commitado + branch baseline/v0 + tag baseline-v0 + harness verde (local e CI); comportamento preservado sem refactor |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.
- Snapshot do legado versionado no repo PRIVADO como preservação interna de baseline; publicação/redistribuição externa PROIBIDA (TRUTH-005).

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 resultados de `baseline_expected.json` com Python padrão; harness em `tests/regression/baseline_check.py` (verde local e no CI).
- **Regra de matching observada**: mesmo `documento` E dif. valor ≤ R$ 5,00 → APPROVED. Tolerância R$ 5,00 = número mágico sem fonte. **T002 (dif. R$ 4,00, pago após vencimento) aprovado — defeito candidato** (known_concern).
- **Dependências declaradas mas NÃO usadas**: `requests`, `fuzzywuzzy`, `legacy-match-sdk` não importadas; baseline não depende do SDK sem licença.
- **Higiene de segredos**: snapshot atual só com placeholders (grep limpo); histórico do repo original do fornecedor exige saneamento antes de eventual importação (TRUTH-014).
- **Fragilidades**: sem autenticação, `debug=True`, secret demo hardcoded, SQLite ao lado do código, ambiente não pinado, sem testes.
- **Spec da API do provedor parcial**: auth, assinatura, paginação, rate limits e erros pendentes.

## Premissas

- Massa de dados no ZIP é 100% sintética (declaração do consultor + README do ZIP).
- Proteção da main reportada como ACTIVE pelo consultor e confirmada por push-teste rejeitado — sem exceção formal necessária nesta configuração.
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

- Conector GitHub: NÃO cria repositórios (403); cria branches/pushes/PRs e fecha PRs OK; **leitura de check runs FUNCIONOU nesta sessão** (AUTO* ok — PR #1); secret scanning API indisponível (sem Advanced Security) — grep local aplicado.
- Conector M365: operacional; NÃO lê ZIP (MIME) — ZIP recebido por anexo na conversa.
- Proteção ACTIVE em repo privado nesta conta — plano permite enforcement (diferente do observado nos Testes 1/2).

## Itens manuais/administrativos pendentes

- GitHub Project (board Backlog→Done) — opcional, a critério do consultor.
- Apagar branches de teste após o /init: `test/armadilha-ci`.
- Preencher contatos/contas GitHub de Rafael Costa e SI em OWNERS.md quando existirem (cenário fictício).

## Retomada

- Próximo passo: Etapa 3 de 5 — init-data (DATA_CATALOG.md com as fontes: legado, massa sintética, ERP, API do provedor, webhooks; classificação de sensibilidade e fixtures).
