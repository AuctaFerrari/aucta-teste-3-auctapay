---
init_version: 0.3.0
projeto: "AuctaPay Concilia — Modernização"
repo: "AuctaFerrari/aucta-teste-3-auctapay"
risk_tier: 3
status_geral: concluida
iniciado_em: 2026-09-03
atualizado_em: 2026-09-03
---

# Estado do /init — AuctaPay Concilia — Modernização

Arquivo de estado do Aucta Dev Init. Registra **progresso**, não conteúdo: respostas e decisões vivem nos artefatos canônicos (PROJECT.md, TRUTHS.md, GLOSSARY.md, ACCEPTANCE.md, OWNERS.md, DATA_CATALOG.md). Atualizado e commitado pelo agente a cada avanço material. **Com a main protegida, atualizações de estado passam por PR.**

**Iniciação encerrada em 2026-09-03 com veredito SEGMENTADO** (ver DoR abaixo): pronta a fase de caracterização e reescrita limpa do motor; gates registrados para integrações, autenticação, deploy e primeiro /change-number.

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | concluida | 2026-09-03 | Artefatos canônicos (a8b6183): PROJECT, TRUTHS, GLOSSARY, ACCEPTANCE (ACC-001..008), OWNERS; tier 3 |
| init-repo | concluida | 2026-09-03 | Governança validada NA PRÁTICA: push direto 409; PR-armadilha #1 reprovada e bloqueada; tag baseline-v0 → 6895c92 |
| init-data | concluida | 2026-09-03 | PR #3: DATA_CATALOG (7 fontes) + golden_cases.csv (GC-01..03, recomputação independente 3/3) + expected_exceptions.csv (EX-01..05) + TEST_STRATEGY + TRUTH-015 |
| init-plugin | concluida | 2026-09-03 | project-plugin/ com router + 8 workflows + pointers + client-rules + MANIFEST D3 (aponta ao core @ 007a7d3, sem duplicação); CLAUDE.md Router preenchido — este PR |
| init-check | concluida | 2026-09-03 | P1–P12 executados; harness verde; drift check com 1 divergência de conteúdo (não bloqueia); dry run de /start-work em simulação — este PR |

## init-repo — checklist

| Item | Status | Evidência / pendência |
| --- | --- | --- |
| 1. Repo privado do template | concluida | bootstrap assistido (2 cliques), private=true, arquivos do template presentes |
| 2. Estrutura de pastas | concluida | legacy/ (snapshot read-only, 14 arquivos), tests/regression/, tests/fixtures/ — nada apagado |
| 3. Baseline (branch + tag) | concluida | branch `baseline/v0` + tag/release `baseline-v0` → 6895c92; diff vs ZIP vazio |
| 4. Templates + CODEOWNERS | concluida | CODEOWNERS do OWNERS.md (@AuctaFerrari); issue/PR templates do template |
| 5. Labels de governança | concluida | Action bootstrap-labels; validado por amostragem (muda-numero, risco-3) |
| 6. Proteção da main | concluida | Ruleset `protecao-main` ACTIVE, bypass vazia, approvals=0 (consultor solo); push direto REJEITADO (409) |
| 7. GitHub Project | pendente | OPCIONAL — item administrativo |
| 8. CI + validação (T2.4) | concluida | PR-armadilha #1 reprovada em 4s, merge "blocked", fechada sem merge; PRs #2/#3 verdes |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido; Router completo (sem placeholders) |

## init-check — preflight P1–P12 (2026-09-03)

| # | Check | Resultado |
| --- | --- | --- |
| P1 | Conector GitHub autenticado | PASS — leituras e escritas OK como AuctaFerrari |
| P2 | Leitura + escrita no repo | PASS — commits do agente em main e branches; criação de repo = 403 (assistido) |
| P3 | Permissão Workflows | PASS por herança — repo criado do template já nasce com `.github/workflows/ci.yml`; não foi necessário criar workflow via API |
| P4 | Governança do repo | PASS — templates, CODEOWNERS, labels; proteção validada por push-teste REJEITADO (409); bypass list vazia; enforcement ACTIVE |
| P5 | Artefatos canônicos + CLAUDE.md | PASS — 5 artefatos presentes, sem placeholders `<...>`; CLAUDE.md com Router preenchido |
| P6 | Catálogo de dados | PASS — DATA_CATALOG.md com 7 fontes; nenhuma base real no repo (massa 100% sintética, TRUTH-011); grep de segredos limpo (só placeholders) |
| P7 | Plugin do projeto | PASS — plugin.json válido; 10 pastas de skills (router + 9 workflows); pointers resolvem |
| P8 | CI | PASS — última execução verde (PR #3); leitura de check runs funcionou nesta sessão (AUTO* ok) |
| P9 | Pasta do projeto / backup | PARCIAL — pasta oficial localizada no OneDrive (`Aucta Blueprint Dev AI/inputs/teste 3`, contém o ZIP do legado); subpastas `04_Releases/` e `backups/` ainda NÃO existem → item administrativo, primeiro uso na primeira release (conector M365 é read-only) |
| P10 | Contas do time | PARCIAL — owner técnico (@AuctaFerrari) confirmado; Rafael Costa e SI são personas do cenário, sem conta GitHub → item administrativo |
| P11 | Drift check D3 | EXECUTADO, não bloqueia — ver seção abaixo (1 divergência de conteúdo em `security-and-hardening`) |
| P12 | Golden cases materializados (tier ≥ 2) | PASS — golden_cases.csv + expected_exceptions.csv + TEST_STRATEGY.md existem, referenciados pelo ACCEPTANCE, com conferência por recomputação independente registrada |

### Health check

- Harness do CI executado localmente (`bash .github/ci/run-checks.sh`): **verde** — baseline `legacy-0.8-observed` 3/3 casos.
- Pointers de `project-plugin/references/pointers.md`: todos resolvem para arquivos existentes.

### Drift check D3 (2026-09-03) — sinaliza, nunca bloqueia

Amostra verificada contra o upstream em HEAD (blob SHA):

| Skill | Registrado no core | Upstream HEAD | Resultado |
| --- | --- | --- | --- |
| context-engineering | `be99110` | `be99110` (skills/context-engineering/SKILL.md) | OK |
| test-driven-development | `0cfd2f3` | `0cfd2f3` | OK |
| diagnosing-bugs | `061c25a` | `061c25a` (skills/engineering/diagnosing-bugs/SKILL.md) | OK — drift de PATH já documentado no core, conteúdo idêntico |
| **security-and-hardening** | `c00236e` | `cf093e9` | **UPSTREAM ALTERADO — auditar e atualizar?** Operação segue na cópia auditada do core; atualização = novo PR com nova auditoria no `aucta-dev-core` |

### Dry run de /start-work (modo simulação, sem efeitos reais)

Demanda simulada: *"ajustar o texto do rótulo da fila de divergências"*.
1. Contexto mínimo carregado (PROJECT + TRUTHS) — OK.
2. Classificação: tipo editorial/UI, nenhuma sentinela tocada → **tier 0**, Muda-numero = nao → caminho leve. Router correto.
3. Rascunho de Issue produzido (resultado desejado, aceite, tier 0, label `risco-0`) — não criada.
4. Nome de branch proposto: `docs/rotulo-fila-divergencias` — não criada.
5. Plano de validação: inspeção visual + harness verde; sem golden adicional.
Contraprova de roteamento (T4.4): demanda *"alterar a tolerância de R$ 5,00"* → sentinela acionada → **tier 2 + /change-number com Muda-numero obrigatório** e gate de aprovação de Rafael Costa. Ambos os caminhos disparam como esperado.

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | v1 replica matching fielmente; reutilização suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md; aceite por comentário no PR (TRUTH-009) |
| E. Dados e fontes | concluida | DATA_CATALOG.md, 7 fontes (2 não validadas: ERP e API do provedor) |
| F. Segurança e privacidade | concluida | Entra ID (TRUTH-007); homolog mascarado (TRUTH-008); saneamento (TRUTH-014) |
| G. IP e licenças | bloqueada | titularidade não confirmada; reutilização suspensa (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado (TRUTH-012); PostgreSQL previsto |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO como blockers |
| J. Repositório e governança | concluida | proteção validada na prática |
| K. Estratégia de testes | concluida | TEST_STRATEGY.md + golden materializados; harness no CI |
| L. Conhecimento canônico | concluida | TRUTHS.md (15) + GLOSSARY.md |
| M. Plugin e skill stack | concluida | project-plugin/ (19 skills apontadas ao core + 3 pendentes com fallback) |
| N. Release e sustentação | concluida | backups/ por release (TRUTH-013); sustentação A DEFINIR |
| O. Baseline | concluida | snapshot + branch + tag + harness verde (local e CI) |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.
- Snapshot do legado versionado no repo PRIVADO como preservação interna de baseline; publicação/redistribuição externa PROIBIDA (TRUTH-005).
- Skills de terceiros: apontadas ao núcleo, sem duplicação local (escolha do consultor, 2026-09-03).

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 pelo harness (CI) e 3/3 por recomputação manual independente da regra documentada.
- **Regra de matching observada**: mesmo `documento` E dif. valor ≤ R$ 5,00 → APPROVED. Tolerância R$ 5,00 = número mágico sem fonte (EX-04). **T002 aprovado com dif. R$ 4,00, pago após vencimento — defeito candidato** (TRUTH-003).
- **Pagamento órfão P003 é IGNORADO pelo legado** — não aparece em nenhuma saída (TRUTH-015; EX-01, bloqueia publicação na nova solução).
- **Dependências declaradas e não usadas**: requests, fuzzywuzzy, legacy-match-sdk (TRUTH-006) — a baseline não depende do SDK sem licença.
- **Higiene de segredos**: snapshot limpo; histórico do fornecedor exige saneamento antes de importação (TRUTH-014).
- **Fragilidades**: sem autenticação, debug=True, secret demo, SQLite ao lado do código, ambiente não pinado, sem testes.
- **Spec da API do provedor parcial**: auth, assinatura, paginação, rate limits e erros pendentes.

## Premissas

- Massa do ZIP é 100% sintética (declaração + README do ZIP).
- Proteção da main ACTIVE confirmada por push-teste rejeitado — sem exceção formal necessária.
- Owner funcional = Rafael Costa (Controladoria) — por inferência; confirmar com o sponsor.
- Nomes do ERP e do provedor de pagamentos pendentes — Fontes 6 e 7 do DATA_CATALOG marcadas "a nomear".
- Estrutura do ERP presumida compatível com titles.json — não validada.
- Skills de UI (frontend-design, impeccable) e camada de comportamento pendentes de vendorização no núcleo — fallback documentado no MANIFEST do projeto.

## Blockers

- **Credenciais do sandbox da API do provedor** — bloqueia: integrações (M5), ACC-004/005. Owner: Mariana Torres.
- **Spec da API do provedor incompleta** (auth, assinatura, paginação, erros) — bloqueia: desenho final da integração (M5). Owner: AuctaPay.
- **Configuração do login corporativo (Entra ID)** — bloqueia: SSO/perfis (M6), ACC-007, release em homologação. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado** — bloqueia: reutilização de código/dependências do legado. NÃO bloqueia baseline, diagnóstico nem reescrita limpa. Owner: Mariana Torres.
- **Aprovação formal da arquitetura Azure** — bloqueia: primeiro deploy (homolog/prod) e definição do backup operacional (RPO/RTO). Owner: SI + Rafael Costa.
- **Validação formal do dono do número sobre golden cases, exceções e tolerância de R$ 5,00** — bloqueia: primeiro /change-number e a classificação definitiva do T002 (defeito × regra) e do EX-01. Owner: Rafael Costa. (Materialização já feita; falta a validação.)
- **Estrutura e mecanismo de extração do ERP não definidos** — bloqueia: desenho da ingestão (M3). Owner: Financeiro AuctaPay + consultor.
- **Sustentação pós-entrega sem dono** — bloqueia: release final e sustentação. Owner da decisão: Mariana Torres.

## Achados de ambiente

- Conector GitHub: NÃO cria repositórios (403); branches/pushes/PRs/merge OK; **leitura de check runs OK nesta sessão** (AUTO*); secret scanning por API indisponível (sem Advanced Security) — grep local aplicado.
- Conector M365: operacional para busca/leitura; **NÃO lê arquivos ZIP** (validação de MIME) — ZIP do legado recebido por anexo na conversa. Achado novo, relevante para casos brownfield.
- Proteção de branch ACTIVE em repo privado nesta conta — o plano permite enforcement (≠ Testes 1 e 2).
- Baseline reproduzível sem instalar dependências (só Python padrão) — permitiu caracterizar o legado sem tocar no `legacy-match-sdk` sem licença.

## Itens manuais/administrativos pendentes

- Criar `04_Releases/` e `backups/` na pasta do projeto no OneDrive (conector M365 não escreve) — primeiro uso na primeira release.
- GitHub Project (board Backlog→Done) — opcional.
- Apagar branches de trabalho/teste: `test/armadilha-ci`, `chore/fechamento-init-repo`, `chore/init-data-catalogo`, `chore/init-plugin`.
- Preencher contatos/contas GitHub de Rafael Costa e Segurança da Informação em OWNERS.md.
- Definir com o sponsor quem sustenta a aplicação após a entrega.
- Auditar/atualizar `security-and-hardening` no núcleo (upstream alterado — drift check P11).

## Retomada

- Próximo passo: `/start-work` na primeira mudança — **"Caracterização das regras do legado com o dono do número"** (fase sem gate): transformar os comportamentos observados em regras classificadas com Rafael Costa, validando golden cases, exceções e a tolerância de R$ 5,00. Esse é o insumo do primeiro `/change-number` e desbloqueia a reescrita do motor.
