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

**Iniciação encerrada em 2026-09-03 com veredito SEGMENTADO.** Duas correções aplicadas no mesmo dia, ambas a partir da avaliação do consultor:

1. **Consistência de fases** (PR #5): a única fase liberada é a **caracterização das regras (M2)**; especificação (M4) e reescrita (M5) dependem da aprovação funcional (M3). O veredito anterior ("pronto para caracterização e reescrita limpa") contrariava TRUTH-004/016.
2. **Cobertura tier 3 e alçadas** (PR #6): threat model preliminar produzido como artefato de iniciação; checklist tier 3 ampliado de 11 para 17 temas, cada um com **owner decisor, workflow de resolução e condição objetiva de desbloqueio**. Achado material sobre a própria `aucta-init` registrado no núcleo (issues #14, #15, #16 do `aucta-dev-core`): o init encerrou tier 3 sem auditar cobertura estrutural por conta própria.

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | concluida | 2026-09-03 | Artefatos canônicos (a8b6183): PROJECT, TRUTHS, GLOSSARY, ACCEPTANCE, OWNERS; tier 3 |
| init-repo | concluida | 2026-09-03 | Governança validada NA PRÁTICA: push direto 409; PR-armadilha #1 reprovada e bloqueada; tag baseline-v0 → 6895c92 |
| init-data | concluida | 2026-09-03 | PR #3: DATA_CATALOG (7 fontes) + golden_cases.csv (GC-01..03, recomputação independente 3/3) + expected_exceptions.csv (EX-01..05) + TEST_STRATEGY + TRUTH-015 |
| init-plugin | concluida | 2026-09-03 | PR #4: project-plugin/ com router + 9 workflows + pointers + client-rules + MANIFEST D3 (aponta ao core @ 007a7d3, sem duplicação); CLAUDE.md Router preenchido |
| init-check | concluida | 2026-09-03 | PR #4: P1–P12; harness verde; drift check (1 divergência, não bloqueia); dry run de /start-work. Re-check de consistência no PR #5; cobertura tier 3 fechada no PR #6 |

## init-repo — checklist

| Item | Status | Evidência / pendência |
| --- | --- | --- |
| 1. Repo privado do template | concluida | bootstrap assistido (2 cliques), private=true, arquivos do template presentes |
| 2. Estrutura de pastas | concluida | legacy/ (snapshot read-only, 14 arquivos), tests/regression/, tests/fixtures/, docs/architecture/ — nada apagado |
| 3. Baseline (branch + tag) | concluida | branch `baseline/v0` + tag/release `baseline-v0` → 6895c92; diff vs ZIP vazio |
| 4. Templates + CODEOWNERS | concluida | CODEOWNERS do OWNERS.md (@AuctaFerrari); issue/PR templates do template |
| 5. Labels de governança | concluida | Action bootstrap-labels; validado por amostragem (muda-numero, risco-3) |
| 6. Proteção da main | concluida | Ruleset `protecao-main` ACTIVE, bypass vazia, approvals=0 (consultor solo); push direto REJEITADO (409) |
| 7. GitHub Project | pendente | OPCIONAL — item administrativo |
| 8. CI + validação (T2.4) | concluida | PR-armadilha #1 reprovada em 4s, merge "blocked", fechada sem merge; PRs #2–#6 verdes |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido; Router completo (sem placeholders) |

## init-check — preflight P1–P12 (2026-09-03)

| # | Check | Resultado |
| --- | --- | --- |
| P1 | Conector GitHub autenticado | PASS |
| P2 | Leitura + escrita no repo | PASS — criação de repo = 403 (assistido) |
| P3 | Permissão Workflows | PASS por herança (repo do template já traz ci.yml) |
| P4 | Governança do repo | PASS — proteção validada por push-teste REJEITADO (409); bypass vazia; enforcement ACTIVE |
| P5 | Artefatos canônicos + CLAUDE.md | PASS — sem placeholders; Router preenchido |
| P6 | Catálogo de dados | PASS — 7 fontes; nenhuma base real no repo; grep de segredos limpo |
| P7 | Plugin do projeto | PASS — plugin.json válido; router + 9 workflows; pointers resolvem |
| P8 | CI | PASS — execuções verdes; leitura de check runs OK nesta sessão (AUTO*) |
| P9 | Pasta do projeto / backup | PARCIAL — pasta oficial localizada; `04_Releases/` e `backups/` não existem → administrativo |
| P10 | Contas do time | PARCIAL — owner técnico confirmado; personas do cenário sem conta GitHub → administrativo |
| P11 | Drift check D3 | EXECUTADO, não bloqueia — 1 divergência de conteúdo (`security-and-hardening`) |
| P12 | Golden cases materializados (tier ≥ 2) | PASS — golden + exceções + TEST_STRATEGY, com recomputação independente |
| **P13 (novo, aplicado retroativamente)** | **Cobertura estrutural tier 3** | **PASS após PR #6** — 17 temas em `.project/CHECKLIST_TIER3.md` com status, owner decisor, workflow e condição de desbloqueio; threat model preliminar em `docs/architecture/THREAT_MODEL_PRELIMINAR.md`. FALHOU na primeira passagem do /init (achado do consultor → issue #14 do core) |

### Health check

- Harness do CI (`bash .github/ci/run-checks.sh`): **verde** — baseline `legacy-0.8-observed` 3/3 casos.
- Pointers de `project-plugin/references/pointers.md`: todos resolvem.

### Drift check D3 (2026-09-03) — sinaliza, nunca bloqueia

| Skill | Registrado no core | Upstream HEAD | Resultado |
| --- | --- | --- | --- |
| context-engineering | `be99110` | `be99110` | OK |
| test-driven-development | `0cfd2f3` | `0cfd2f3` | OK |
| diagnosing-bugs | `061c25a` | `061c25a` (caminho novo) | OK — drift de PATH, conteúdo idêntico |
| **security-and-hardening** | `c00236e` | `cf093e9` | **UPSTREAM ALTERADO — auditar e atualizar?** Operação segue na cópia do core |

### Dry run de /start-work (simulação)

*"ajustar rótulo da fila de divergências"* → tier 0, Muda-numero = nao → caminho leve. Contraprova: *"alterar a tolerância de R$ 5,00"* → sentinela → **tier 2 + /change-number** com aprovação de Rafael Costa. Ambos corretos.

## Cobertura tier 3 (PR #6)

Matriz completa em `.project/CHECKLIST_TIER3.md` — 17 temas: threat model, RBAC, PII em logs, secret histórico, segregação de ambientes, retenção, idempotência de webhook, migração, rollback, RPO/RTO, observabilidade, identidade, integrações, persistência, sustentação, IP/licenças e ADRs. Cada linha tem status (definido / premissa / pendência não bloqueante / blocker), **owner decisor**, workflow de resolução e condição objetiva de desbloqueio.

**Threat model preliminar** (`docs/architecture/THREAT_MODEL_PRELIMINAR.md`): 8 ativos, 10 atores, 8 trust boundaries, 13 ameaças, 11 controles já exigidos e 11 decisões abertas com owner decisor. Status: preliminar, **não aprovado** — o `/architecture` aprofunda e aprova, não cria do zero.

**Regra de alçada registrada:** `/architecture` orquestra, desenha e documenta (ADR), mas **não decide** retenção de dados, RPO/RTO, política de PII nem RBAC. Autoridade por tema no checklist.

## Re-check de consistência (2026-09-03, pós-correções)

| Verificação | Resultado |
| --- | --- |
| Sequência das fases coerente entre artefatos | PASS — ACCEPTANCE (M1–M10), TRUTH-016, PROJECT e este estado com a mesma dependência M2 → M3 → M4 → M5 |
| T002 e P003 como comportamento observado da `baseline-v0`, não regra aprovada | PASS — TRUTH-003/015 com status de evidência e tag citada; GC-02, EX-01/EX-02; `evidence_status: observed_not_approved` |
| Nenhum artefato promove observado a requisito | PASS — ACC-002 cita o gate M3; ACC-009 cobre a caracterização |
| Cobertura tier 3 rastreável | PASS — 17 temas com owner decisor e condição de desbloqueio; threat model preliminar produzido |
| Alçada de decisão explícita | PASS — regra registrada no checklist e no threat model; `/architecture` deixa de aparecer como resolvedor universal |
| Pilha de skills = capacidades sob demanda | PASS — MANIFEST com carga real por tipo de demanda (2 a 4 skills por workflow) |
| Harness da baseline | PASS — verde; `legacy/` intocado em todos os PRs |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | replicação APÓS aprovação (TRUTH-004/016); reutilização suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md (ACC-001..009, marcos M1–M10) |
| E. Dados e fontes | concluida | DATA_CATALOG.md, 7 fontes (2 não validadas) |
| F. Segurança e privacidade | concluida | Entra ID, homolog mascarado, saneamento; cobertura em CHECKLIST_TIER3 + threat model preliminar |
| G. IP e licenças | bloqueada | titularidade não confirmada (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado; temas estruturais mapeados |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox e SSO como blockers |
| J. Repositório e governança | concluida | proteção validada na prática |
| K. Estratégia de testes | concluida | TEST_STRATEGY.md + golden materializados |
| L. Conhecimento canônico | concluida | TRUTHS.md (16) + GLOSSARY.md |
| M. Plugin e skill stack | concluida | 19 capacidades roteadas sob demanda + 3 pendentes com fallback |
| N. Release e sustentação | concluida | backups/ por release (TRUTH-013); sustentação A DEFINIR |
| O. Baseline | concluida | snapshot + branch + tag + harness verde |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; observado NÃO é regra aprovada.
- Classificação obrigatória: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: inventariar, diagnosticar, preservar baseline, classificar riscos, produzir artefatos. Sem implementação, refactor ou correção do legado.
- Snapshot do legado no repo PRIVADO como preservação de baseline; publicação externa PROIBIDA (TRUTH-005).
- Skills de terceiros apontadas ao núcleo, sem duplicação local.
- **Sequência obrigatória (TRUTH-016): caracterizar (M2) → aprovar (M3) → especificar (M4) → reescrever (M5).**
- **Tier 3 exige threat model preliminar na iniciação** e matriz de cobertura estrutural antes do encerramento; `/architecture` aprofunda, não cria.
- **Todo blocker carrega owner decisor, workflow de resolução e condição objetiva de desbloqueio.**

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 pelo harness e 3/3 por recomputação independente.
- **Regra observada**: mesmo `documento` E dif. ≤ R$ 5,00 → APPROVED; tolerância sem fonte (EX-04). T002 (dif. R$ 4,00, pago após vencimento) aprovado — defeito candidato (TRUTH-003).
- **P003 órfão IGNORADO** pela baseline (TRUTH-015; EX-01) — tratamento como divergência é hipótese a ratificar.
- **Dependências declaradas e não usadas**: requests, fuzzywuzzy, legacy-match-sdk (TRUTH-006).
- **Higiene de segredos**: snapshot limpo; histórico do fornecedor exige saneamento (TRUTH-014).
- **Fragilidades**: sem autenticação, debug=True, secret demo, SQLite ao lado do código, ambiente não pinado, sem testes.
- **Spec da API do provedor parcial**.

## Premissas

- Massa do ZIP é 100% sintética.
- Proteção da main ACTIVE confirmada por push-teste rejeitado.
- Owner funcional = Rafael Costa — por inferência; confirmar com o sponsor.
- Nomes do ERP e do provedor pendentes (Fontes 6 e 7 do DATA_CATALOG).
- Estrutura do ERP presumida compatível com titles.json — não validada.
- Skills de UI e camada de comportamento pendentes de vendorização no núcleo — fallback documentado.
- Severidades do threat model preliminar são preliminares — a SI pode reclassificá-las na aprovação.

## Blockers

Formato (a partir do achado do Teste 3): **item — o que bloqueia · owner decisor · workflow de resolução · condição objetiva de desbloqueio.**

- **Aprovação funcional das regras (M3)** — bloqueia M4, M5, ACC-002 e todo /change-number; NÃO bloqueia M2. Owner decisor: **Rafael Costa**. Workflow: sessão de aprovação sobre o mapa do M2, registrada na Issue. Desbloqueio: cada comportamento classificado (confirmada/defeito), golden e exceções ratificados, tolerância decidida e parametrizada.
- **Credenciais do sandbox da API** — bloqueia M7, ACC-004/005. Owner decisor: **Mariana Torres** (junto ao provedor). Workflow: solicitação formal. Desbloqueio: credenciais ativas testadas.
- **Spec completa da API** (auth, assinatura, paginação, erros, retries) — bloqueia M7. Owner decisor: **AuctaPay + provedor**. Workflow: `/architecture` após recebimento. Desbloqueio: spec recebida e contrato de webhook fechado (D-08 do threat model).
- **Configuração Entra ID** — bloqueia M8, ACC-007. Owner decisor: **Segurança da Informação**. Workflow: fornecimento de tenant/client. Desbloqueio: validação de token testada.
- **Matriz RBAC** — bloqueia M8, ACC-007. Owner decisor: **Rafael Costa + SI**. Workflow: `/architecture` orquestra; decisão dos owners. Desbloqueio: matriz ler/criar/aprovar/exportar aprovada e anexada.
- **Política de PII em logs, erros, telas e exportações** — bloqueia M6, M8, M10. Owner decisor: **SI/LGPD + operação**. Workflow: `/architecture` documenta. Desbloqueio: política com regra de mascaramento por campo aprovada.
- **Retenção de dados** — bloqueia M6, M9, M10. Owner decisor: **Jurídico/LGPD + Rafael Costa** (não é decisão de arquitetura). Workflow: decisão de negócio em Issue. Desbloqueio: prazos por classe de dado com base legal.
- **Segregação de ambientes** — bloqueia M10. Owner decisor: **SI + arquitetura**. Workflow: `/architecture`. Desbloqueio: desenho aprovado com bancos, cofres e credenciais separados.
- **RPO/RTO + backup operacional** — bloqueia M10 e sustentação. Owner decisor: **Negócio (Mariana/Rafael) + operação + arquitetura**. Workflow: decisão de negócio + `/architecture`. Desbloqueio: RPO e RTO numéricos aprovados com plano correspondente.
- **Observabilidade (logs, alertas, monitoramento)** — bloqueia M9, M10, sustentação. Owner decisor: **Operação + SI**. Workflow: `/architecture`. Desbloqueio: plano aprovado, coerente com a política de PII.
- **Migração do histórico do legado (SQLite)** — bloqueia M6, M10. Owner decisor: **Rafael Costa + arquitetura**. Workflow: `/architecture`. Desbloqueio: decisão migrar/não migrar; se migrar, plano com validação e rollback.
- **Rollback por release** — bloqueia M10. Owner decisor: **Arquitetura + operação**. Workflow: `/architecture`. Desbloqueio: procedimento testado em homologação.
- **Aprovação formal da arquitetura Azure** — bloqueia M10. Owner decisor: **SI + Rafael Costa**. Workflow: aprovação formal fora do repo, registrada em Issue. Desbloqueio: registro anexado antes do primeiro deploy.
- **Estrutura e extração do ERP** — bloqueia M6. Owner decisor: **Financeiro AuctaPay + consultor**. Workflow: `/architecture` (desenho da ingestão). Desbloqueio: mecanismo definido e lista de campos mínimos aprovada (D-09).
- **Titularidade e licenças do legado** — bloqueia reuso de código/dependências; NÃO bloqueia baseline, caracterização nem reescrita limpa. Owner decisor: **Mariana Torres** + revisão jurídica. Desbloqueio: contrato localizado e parecer sobre dependências.
- **Sustentação pós-entrega** — bloqueia release final e sustentação. Owner decisor: **Mariana Torres**. Workflow: decisão de negócio. Desbloqueio: owner operacional nomeado com canal de suporte.
- **Aprovação do threat model** — bloqueia M6–M10 (o documento preliminar existe; falta aprovar). Owner decisor: **SI + owner técnico**. Workflow: `/architecture`. Desbloqueio: versão aprovada + ADRs das decisões duráveis.

## Achados de ambiente

- Conector GitHub: NÃO cria repositórios (403); branches/pushes/PRs/merge/issues OK; leitura de check runs OK nesta sessão (AUTO*); secret scanning por API indisponível — grep local aplicado.
- Conector M365: busca/leitura OK; **NÃO lê arquivos ZIP** (validação de MIME) — relevante para casos brownfield.
- Proteção de branch ACTIVE em repo privado nesta conta (≠ Testes 1 e 2).
- Baseline reproduzível só com Python padrão — caracterização sem tocar no SDK sem licença.

## Itens manuais/administrativos pendentes

- Criar `04_Releases/` e `backups/` na pasta do projeto no OneDrive (conector não escreve).
- GitHub Project (board) — opcional.
- Apagar branches de trabalho/teste: `test/armadilha-ci`, `chore/fechamento-init-repo`, `chore/init-data-catalogo`, `chore/init-plugin`, `chore/consistencia-final-init`, `docs/threat-model-preliminar-e-alcadas`.
- Preencher contatos/contas GitHub de Rafael Costa e SI em OWNERS.md.
- Definir com o sponsor quem sustenta a aplicação após a entrega.
- Auditar/atualizar `security-and-hardening` no núcleo (drift P11).
- Agendar a sessão de aprovação funcional (M3) com Rafael Costa — gate de maior alcance.
- Acompanhar no núcleo as issues #14, #15 e #16 do `aucta-dev-core` (melhorias da aucta-init geradas por este teste).

## Retomada

- Próximo passo: `/start-work` no marco **M2 — Caracterização das regras do legado** (única fase liberada; análise documental sobre a `baseline-v0`, sem código e sem especificação de solução). Produto: mapa de regras observadas com evidência, proposta de classificação e perguntas ao dono do número (ACC-009).
- Em seguida: **M3 — aprovação funcional** com Rafael Costa. Só depois M4 (especificação) e M5 (reescrita).
