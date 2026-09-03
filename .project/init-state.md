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

**Iniciação encerrada em 2026-09-03 com veredito SEGMENTADO** (ver DoR abaixo). **Correção de consistência aplicada em 2026-09-03** (este PR): a única fase liberada é a **caracterização das regras (M2)**; especificação (M4) e reescrita do motor (M5) passam a depender da aprovação funcional (M3). Veredito anterior ("pronto para caracterização e reescrita limpa") estava incorreto — reescrever sem regras aprovadas contraria TRUTH-004/TRUTH-016.

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | concluida | 2026-09-03 | Artefatos canônicos (a8b6183): PROJECT, TRUTHS, GLOSSARY, ACCEPTANCE, OWNERS; tier 3 |
| init-repo | concluida | 2026-09-03 | Governança validada NA PRÁTICA: push direto 409; PR-armadilha #1 reprovada e bloqueada; tag baseline-v0 → 6895c92 |
| init-data | concluida | 2026-09-03 | PR #3: DATA_CATALOG (7 fontes) + golden_cases.csv (GC-01..03, recomputação independente 3/3) + expected_exceptions.csv (EX-01..05) + TEST_STRATEGY + TRUTH-015 |
| init-plugin | concluida | 2026-09-03 | PR #4: project-plugin/ com router + 9 workflows + pointers + client-rules + MANIFEST D3 (aponta ao core @ 007a7d3, sem duplicação); CLAUDE.md Router preenchido |
| init-check | concluida | 2026-09-03 | PR #4: P1–P12; harness verde; drift check (1 divergência, não bloqueia); dry run de /start-work. **Re-executado neste PR** — ver "Re-check de consistência" |

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
| 8. CI + validação (T2.4) | concluida | PR-armadilha #1 reprovada em 4s, merge "blocked", fechada sem merge; PRs #2/#3/#4 verdes |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido; Router completo (sem placeholders) |

## init-check — preflight P1–P12 (2026-09-03)

| # | Check | Resultado |
| --- | --- | --- |
| P1 | Conector GitHub autenticado | PASS — leituras e escritas OK como AuctaFerrari |
| P2 | Leitura + escrita no repo | PASS — commits do agente em main e branches; criação de repo = 403 (assistido) |
| P3 | Permissão Workflows | PASS por herança — repo do template já nasce com `.github/workflows/ci.yml` |
| P4 | Governança do repo | PASS — templates, CODEOWNERS, labels; proteção validada por push-teste REJEITADO (409); bypass vazia; enforcement ACTIVE |
| P5 | Artefatos canônicos + CLAUDE.md | PASS — artefatos presentes, sem placeholders `<...>`; CLAUDE.md com Router preenchido |
| P6 | Catálogo de dados | PASS — DATA_CATALOG.md com 7 fontes; nenhuma base real no repo (TRUTH-011); grep de segredos limpo |
| P7 | Plugin do projeto | PASS — plugin.json válido; 10 pastas de skills (router + 9 workflows); pointers resolvem |
| P8 | CI | PASS — última execução verde; leitura de check runs funcionou nesta sessão (AUTO* ok) |
| P9 | Pasta do projeto / backup | PARCIAL — pasta oficial localizada no OneDrive (contém o ZIP do legado); `04_Releases/` e `backups/` ainda NÃO existem → item administrativo (conector M365 é read-only) |
| P10 | Contas do time | PARCIAL — owner técnico (@AuctaFerrari) confirmado; Rafael Costa e SI são personas do cenário, sem conta GitHub → item administrativo |
| P11 | Drift check D3 | EXECUTADO, não bloqueia — 1 divergência de conteúdo em `security-and-hardening` |
| P12 | Golden cases materializados (tier ≥ 2) | PASS — golden_cases.csv + expected_exceptions.csv + TEST_STRATEGY.md, referenciados pelo ACCEPTANCE, com conferência por recomputação independente |

### Health check

- Harness do CI executado localmente (`bash .github/ci/run-checks.sh`): **verde** — baseline `legacy-0.8-observed` 3/3 casos.
- Pointers de `project-plugin/references/pointers.md`: todos resolvem para arquivos existentes.

### Drift check D3 (2026-09-03) — sinaliza, nunca bloqueia

| Skill | Registrado no core | Upstream HEAD | Resultado |
| --- | --- | --- | --- |
| context-engineering | `be99110` | `be99110` | OK |
| test-driven-development | `0cfd2f3` | `0cfd2f3` | OK |
| diagnosing-bugs | `061c25a` | `061c25a` (caminho novo) | OK — drift de PATH documentado no core, conteúdo idêntico |
| **security-and-hardening** | `c00236e` | `cf093e9` | **UPSTREAM ALTERADO — auditar e atualizar?** Operação segue na cópia auditada do core; atualização = novo PR no `aucta-dev-core` |

### Dry run de /start-work (modo simulação, sem efeitos reais)

Demanda simulada: *"ajustar o texto do rótulo da fila de divergências"* → tier 0, Muda-numero = nao → caminho leve; rascunho de Issue e nome de branch produzidos sem criar nada. Contraprova (T4.4): *"alterar a tolerância de R$ 5,00"* → sentinela acionada → **tier 2 + /change-number** com Muda-numero obrigatório e aprovação de Rafael Costa. Ambos os caminhos disparam como esperado.

## Re-check de consistência (2026-09-03, pós-correção)

| Verificação | Resultado |
| --- | --- |
| Sequência das fases coerente entre artefatos | PASS — ACCEPTANCE (marcos M1–M10), TRUTH-016 e este estado usam a mesma numeração e a mesma dependência M2 → M3 → M4 → M5 |
| T002 e P003 registrados como comportamento observado da `baseline-v0`, não como regra aprovada | PASS — TRUTH-003 e TRUTH-015 explicitam status de evidência, apontam a tag `baseline-v0` e atribuem a classificação definitiva a Rafael Costa em M3; `golden_cases.csv` (GC-02) e `expected_exceptions.csv` (EX-01/EX-02) idem; `baseline_expected.json` carrega `evidence_status: observed_not_approved` |
| Nenhum artefato promove comportamento observado a requisito | PASS — ACC-002 passa a citar o gate M3; ACC-009 criado para a caracterização |
| Cobertura tier 3 rastreável | PASS — `.project/CHECKLIST_TIER3.md` com 11 temas, local de registro, status e o que cada um bloqueia; 3 lacunas antes não registradas (PII em logs, segregação de ambientes, retenção) e 1 decisão ausente (migração do histórico) passam a estar registradas |
| Pilha de skills = capacidades sob demanda | PASS — MANIFEST do projeto ganhou a seção de carregamento progressivo com a carga real por tipo de demanda (2 a 4 skills por workflow); router permanece o único ponto de decisão |
| Harness da baseline | PASS — verde após as mudanças (somente documentação alterada; `legacy/` intocado) |
| Referências cruzadas dos marcos nos blockers | PASS — blockers renumerados para M6–M10 conforme ACCEPTANCE corrigido |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | v1 replica matching fielmente APÓS aprovação (TRUTH-004/016); reutilização suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md (ACC-001..009, marcos M1–M10) |
| E. Dados e fontes | concluida | DATA_CATALOG.md, 7 fontes (2 não validadas: ERP e API do provedor) |
| F. Segurança e privacidade | concluida | Entra ID (TRUTH-007); homolog mascarado (TRUTH-008); saneamento (TRUTH-014); cobertura detalhada em CHECKLIST_TIER3 |
| G. IP e licenças | bloqueada | titularidade não confirmada; reutilização suspensa (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado (TRUTH-012); PostgreSQL previsto; temas estruturais mapeados no CHECKLIST_TIER3 |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO como blockers |
| J. Repositório e governança | concluida | proteção validada na prática |
| K. Estratégia de testes | concluida | TEST_STRATEGY.md + golden materializados; harness no CI |
| L. Conhecimento canônico | concluida | TRUTHS.md (16) + GLOSSARY.md |
| M. Plugin e skill stack | concluida | project-plugin/ (19 capacidades roteadas sob demanda + 3 pendentes com fallback) |
| N. Release e sustentação | concluida | backups/ por release (TRUTH-013); sustentação A DEFINIR |
| O. Baseline | concluida | snapshot + branch + tag + harness verde (local e CI) |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.
- Snapshot do legado versionado no repo PRIVADO como preservação interna de baseline; publicação/redistribuição externa PROIBIDA (TRUTH-005).
- Skills de terceiros: apontadas ao núcleo, sem duplicação local.
- **Sequência obrigatória (TRUTH-016): caracterizar (M2) → aprovar funcionalmente (M3) → especificar (M4) → reescrever (M5).** Caracterização não autoriza especificação nem reescrita.

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 pelo harness (CI) e 3/3 por recomputação manual independente da regra documentada.
- **Regra de matching observada**: mesmo `documento` E dif. valor ≤ R$ 5,00 → APPROVED. Tolerância R$ 5,00 = número mágico sem fonte (EX-04). **T002 aprovado com dif. R$ 4,00, pago após vencimento — comportamento observado / defeito candidato** (TRUTH-003).
- **Pagamento órfão P003 é IGNORADO pela baseline-v0** — não aparece em nenhuma saída (TRUTH-015; EX-01). Tratamento como divergência visível é hipótese a ratificar em M3.
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

- **Validação/aprovação funcional das regras (marco M3)** — Rafael Costa decide classificação de cada comportamento observado, golden cases, exceções e tolerâncias. Bloqueia: **especificação do motor (M4), reescrita (M5), ACC-002 e todo /change-number**. NÃO bloqueia a caracterização (M2). Owner: Rafael Costa.
- **Credenciais do sandbox da API do provedor** — bloqueia: integrações (M7), ACC-004/005. Owner: Mariana Torres.
- **Spec da API do provedor incompleta** (auth, assinatura, paginação, erros, idempotência) — bloqueia: desenho final da integração (M7). Owner: AuctaPay.
- **Configuração do login corporativo (Entra ID) + matriz RBAC** — bloqueia: SSO/perfis (M8), ACC-007, release em homologação. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado** — bloqueia: reutilização de código/dependências do legado. NÃO bloqueia baseline, caracterização nem reescrita limpa. Owner: Mariana Torres.
- **Estrutura e mecanismo de extração do ERP não definidos** — bloqueia: desenho e implementação da ingestão (M6). Owner: Financeiro AuctaPay + consultor.
- **Threat model, RBAC, PII em logs, segregação de ambientes, retenção, migração, rollback e ADRs não produzidos** — bloqueiam: M6 a M10 (implementação de integração, autenticação, persistência e deploy). Detalhamento por tema em `.project/CHECKLIST_TIER3.md`. Owner: Aucta (owner técnico) + Segurança da Informação.
- **Aprovação formal da arquitetura Azure + RPO/RTO** — bloqueia: primeiro deploy (M10) e definição do backup operacional. Owner: SI + Rafael Costa.
- **Sustentação pós-entrega sem dono** — bloqueia: release final e sustentação. Owner da decisão: Mariana Torres.

## Achados de ambiente

- Conector GitHub: NÃO cria repositórios (403); branches/pushes/PRs/merge OK; **leitura de check runs OK nesta sessão** (AUTO*); secret scanning por API indisponível (sem Advanced Security) — grep local aplicado.
- Conector M365: operacional para busca/leitura; **NÃO lê arquivos ZIP** (validação de MIME) — ZIP do legado recebido por anexo na conversa. Achado novo, relevante para casos brownfield.
- Proteção de branch ACTIVE em repo privado nesta conta — o plano permite enforcement (≠ Testes 1 e 2).
- Baseline reproduzível sem instalar dependências (só Python padrão) — permitiu caracterizar o legado sem tocar no `legacy-match-sdk` sem licença.

## Itens manuais/administrativos pendentes

- Criar `04_Releases/` e `backups/` na pasta do projeto no OneDrive (conector M365 não escreve) — primeiro uso na primeira release.
- GitHub Project (board Backlog→Done) — opcional.
- Apagar branches de trabalho/teste: `test/armadilha-ci`, `chore/fechamento-init-repo`, `chore/init-data-catalogo`, `chore/init-plugin`, `chore/consistencia-final-init`.
- Preencher contatos/contas GitHub de Rafael Costa e Segurança da Informação em OWNERS.md.
- Definir com o sponsor quem sustenta a aplicação após a entrega.
- Auditar/atualizar `security-and-hardening` no núcleo (upstream alterado — drift check P11).
- Agendar a sessão de aprovação funcional (M3) com Rafael Costa — é o gate de maior alcance do projeto.

## Retomada

- Próximo passo: `/start-work` no marco **M2 — Caracterização das regras do legado** (única fase liberada; análise documental sobre a `baseline-v0`, sem código, sem especificação de solução). Produto: mapa de regras observadas com evidência, proposta de classificação e lista de perguntas ao dono do número (ACC-009).
- Em seguida: **M3 — aprovação funcional** com Rafael Costa. Só depois M4 (especificação) e M5 (reescrita).
