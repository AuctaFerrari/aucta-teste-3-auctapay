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
| init-interview | concluida | 2026-09-03 | Artefatos canônicos (a8b6183): PROJECT, TRUTHS, GLOSSARY, ACCEPTANCE (ACC-001..008), OWNERS; tier 3 |
| init-repo | concluida | 2026-09-03 | Governança validada NA PRÁTICA: push direto 409; PR-armadilha #1 reprovada e bloqueada; tag baseline-v0 → 6895c92 |
| init-data | concluida | 2026-09-03 | DATA_CATALOG (7 fontes) + golden_cases.csv (GC-01..03, recomputação independente 3/3) + expected_exceptions.csv (EX-01..05) + TEST_STRATEGY + TRUTH-015 — este PR |
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
| 6. Proteção da main | concluida | Ruleset `protecao-main` ACTIVE, bypass vazia, approvals=0 (consultor solo); validado por push direto REJEITADO (409) |
| 7. GitHub Project | pendente | OPCIONAL — consultor cria se quiser board |
| 8. CI + validação (T2.4) | concluida | PR-armadilha #1: check reprovou em 4s; merge "blocked"; fechado sem merge |
| 9. Política de versão | concluida | VERSION 0.1.0 + CHANGELOG; tag/release = referência oficial |
| 10. CLAUDE.md | concluida | preenchido; Router aguarda init-plugin |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | PROJECT.md |
| B. Escopo e fronteiras | concluida | PROJECT.md; v1 replica matching fielmente; reutilização suspensa (TRUTH-005) |
| C. Stakeholders e decisão | concluida | OWNERS.md; produção = Rafael Costa + SI |
| D. Entregáveis e aceite | concluida | ACCEPTANCE.md; aceite por comentário no PR (TRUTH-009) |
| E. Dados e fontes | concluida | DATA_CATALOG.md com 7 fontes (2 não validadas: ERP e API do provedor — nomes pendentes) |
| F. Segurança e privacidade | concluida | Entra ID (TRUTH-007); homolog só mascarado (TRUTH-008); saneamento de histórico (TRUTH-014) |
| G. IP e licenças | bloqueada | titularidade não confirmada; reutilização suspensa — blocker ativo (TRUTH-005) |
| H. Arquitetura inicial | concluida | PROJECT.md; Azure condicionado (TRUTH-012); PostgreSQL previsto |
| I. Ambientes e acessos | concluida | homolog+prod; sandbox API e SSO seguem como blockers |
| J. Repositório e governança | concluida | proteção validada na prática |
| K. Estratégia de testes | concluida | TEST_STRATEGY.md + golden materializados; harness ACC-001 no CI |
| L. Conhecimento canônico | concluida | TRUTHS.md (15) + GLOSSARY.md |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | concluida | backups/ por release (TRUTH-013); sustentação A DEFINIR |
| O. Baseline | concluida | snapshot + branch + tag + harness verde (local e CI) |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.
- Snapshot do legado versionado no repo PRIVADO como preservação interna de baseline; publicação/redistribuição externa PROIBIDA (TRUTH-005).

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: 3/3 pelo harness (CI) e 3/3 por recomputação manual independente da regra documentada.
- **Regra de matching observada**: mesmo `documento` E dif. valor ≤ R$ 5,00 → APPROVED. Tolerância R$ 5,00 = número mágico sem fonte (EX-04). **T002 aprovado com dif. R$ 4,00, pago após vencimento — defeito candidato** (TRUTH-003).
- **Pagamento órfão P003 é IGNORADO pelo legado** — não aparece em nenhuma saída (TRUTH-015; EX-01, bloqueia publicação na nova solução).
- **Dependências declaradas e não usadas**: requests, fuzzywuzzy, legacy-match-sdk (TRUTH-006).
- **Higiene de segredos**: snapshot limpo; histórico do fornecedor exige saneamento antes de importação (TRUTH-014).
- **Fragilidades**: sem autenticação, debug=True, secret demo, SQLite ao lado do código, ambiente não pinado, sem testes.
- **Spec da API do provedor parcial**: auth, assinatura, paginação, rate limits e erros pendentes.

## Premissas

- Massa do ZIP é 100% sintética (declaração + README do ZIP).
- Proteção da main ACTIVE confirmada por push-teste rejeitado — sem exceção formal necessária.
- Owner funcional = Rafael Costa (Controladoria) — por inferência; confirmar com o sponsor.
- Nomes do ERP e do provedor de pagamentos pendentes — Fontes 6 e 7 do DATA_CATALOG marcadas "a nomear".
- Estrutura do ERP presumida compatível com titles.json — não validada.

## Blockers

- **Credenciais do sandbox da API do provedor** — bloqueia: integrações (M5), ACC-004/005. Owner: Mariana Torres.
- **Configuração do login corporativo (Entra ID)** — bloqueia: SSO/perfis (M6), ACC-007, release em homolog. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado** — bloqueia: reutilização do legado (não bloqueia baseline/diagnóstico/reescrita limpa). Owner: Mariana Torres.
- **Spec da API do provedor incompleta** — bloqueia: desenho final da integração (M5). Owner: AuctaPay.
- **Aprovação formal da arquitetura Azure** — bloqueia: primeiro deploy e backup operacional (RPO/RTO). Owner: SI + Rafael Costa.
- **Validação formal do dono do número sobre golden/exceções/tolerância** — bloqueia: primeiro /change-number e classificação definitiva do T002 e do EX-01. Owner: Rafael Costa. (Materialização feita; validação é o gate.)
- **Sustentação pós-entrega sem dono** — bloqueia: release final/sustentação. Owner da decisão: Mariana Torres.
- **Estrutura/extração do ERP não definida** — bloqueia: desenho da ingestão (M3). Owner: Financeiro AuctaPay + consultor.

## Achados de ambiente

- Conector GitHub: NÃO cria repositórios (403); branches/pushes/PRs/merge OK; leitura de check runs OK nesta sessão (AUTO*); secret scanning API indisponível — grep local aplicado.
- Conector M365: operacional; NÃO lê ZIP (MIME) — ZIP recebido por anexo.
- Proteção ACTIVE em repo privado nesta conta — plano permite enforcement (≠ Testes 1/2).

## Itens manuais/administrativos pendentes

- GitHub Project (board) — opcional.
- Apagar branches de teste/trabalho após o /init: `test/armadilha-ci`, `chore/fechamento-init-repo`, `chore/init-data-catalogo`.
- Preencher contatos/contas de Rafael Costa e SI em OWNERS.md (cenário fictício).
- Criar pasta `backups/` no OneDrive do projeto (primeiro uso na primeira release).

## Retomada

- Próximo passo: Etapa 4 de 5 — init-plugin (plugin do projeto: router, workflows do blueprint 7.3, stack de skills com justificativa, manifesto D3 apontando ao core).
