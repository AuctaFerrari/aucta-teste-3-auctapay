---
init_version: 0.3.0
projeto: "AuctaPay Concilia — Modernização"
repo: "AuctaFerrari/aucta-teste-3-auctapay"
risk_tier: null
status_geral: em_andamento
iniciado_em: 2026-09-03
atualizado_em: 2026-09-03
---

# Estado do /init — AuctaPay Concilia — Modernização

Arquivo de estado do Aucta Dev Init. Registra **progresso**, não conteúdo: respostas e decisões vivem nos artefatos canônicos (PROJECT.md, TRUTHS.md, GLOSSARY.md, ACCEPTANCE.md, OWNERS.md, DATA_CATALOG.md). Atualizado e commitado pelo agente a cada avanço material.

## Sub-skills

| Sub-skill | Status | Última atualização | Evidência |
| --- | --- | --- | --- |
| init-interview | em_andamento | 2026-09-03 | A, B, C fechados; ZIP do legado recebido e inventariado; rodada F/H em andamento |
| init-repo | pendente | | repo criado via template (bootstrap assistido 2026-09-03) |
| init-data | pendente | | ZIP extraído e lido na sessão; catálogo formal pendente |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | confirmado 2026-09-03; KPIs: tempo de conciliação, divergências tratadas, rastreabilidade p/ auditoria, fim do manual em planilha |
| B. Escopo e fronteiras | concluida | v1 replica regras de matching fielmente; correção de regras fora da v1; reutilização de código/deps NÃO autorizada até verificação de IP/licenças; sem implementação/refactor durante o /init |
| C. Stakeholders e decisão | concluida | Sponsor: Mariana Torres (CFO); dono do número: Rafael Costa (Controladoria); produção: aprovação conjunta Rafael Costa + Segurança da Informação |
| D. Entregáveis e aceite | em_andamento | web interna, homolog+prod; mecanismo de aprovação pendente |
| E. Dados e fontes (inventário) | em_andamento | ZIP inventariado (14 arquivos); nomes do ERP e do provedor pendentes |
| F. Segurança e privacidade | em_andamento | GATILHO: PII real; login corporativo = Microsoft Entra ID (achado no .env.example, a confirmar); política de dados em homolog pendente |
| G. IP e licenças | em_andamento | LICENSE_STATUS.md do legado CONFIRMA: titularidade não confirmada, `legacy-match-sdk` sem licença/fonte, redistribuição NÃO autorizada — blocker mantido |
| H. Arquitetura inicial | em_andamento | legado: Flask 1-endpoint + SQLite local, sem auth; infra de homolog/prod pendente |
| I. Ambientes e acessos | em_andamento | homolog e prod previstos; sandbox API e SSO pendentes (blockers) |
| J. Repositório e governança | pendente | executado no init-repo |
| K. Estratégia de testes | em_andamento | baseline característica JÁ REPRODUZIDA na sessão (ver Achados do legado) — formalização no init-repo |
| L. Conhecimento canônico | pendente | taxonomia de evidência definida (Decisões de método) |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | pendente | |
| O. Baseline | em_andamento | snapshot limpo do ZIP validado; commit da baseline no init-repo |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido**.
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.

## Achados do legado (diagnóstico read-only, 2026-09-03)

- **Baseline reproduzida com exatidão**: `reconcile_records` sobre a massa sintética reproduz 3/3 resultados de `baseline/baseline_expected.json` (T001 APPROVED, T002 APPROVED, T003 OPEN) usando apenas Python padrão — sem instalar dependências.
- **Regra de matching observada**: mesmo `documento` E diferença de valor ≤ R$ 5,00 → APPROVED automático. Tolerância de R$ 5,00 é número mágico sem fonte. **T002 (dif. R$ 4,00, pago após o vencimento) é aprovado automaticamente — comportamento observado, defeito candidato, NÃO regra aprovada** (known_concern do próprio ZIP).
- **Dependências declaradas mas NÃO usadas no código**: `requests`, `fuzzywuzzy` e `legacy-match-sdk` não são importadas por nenhum módulo. A baseline NÃO depende do SDK sem licença.
- **Higiene de segredos**: snapshot atual contém apenas placeholders (grep local limpo). `production_notes.txt` alerta que o HISTÓRICO do repo original do fornecedor teve token de homologação (revogado, não saneado) — se o histórico original for recebido algum dia, sanear antes de importar; acionar Segurança da Informação.
- **Fragilidades do legado**: sem autenticação, `debug=True`, secret hardcoded de demonstração, SQLite ao lado do código, ambiente não pinado (Windows/Py 3.10, versões não capturadas), sem testes automatizados.
- **Login corporativo**: `.env.example` referencia ENTRA_TENANT_ID/ENTRA_CLIENT_ID → Microsoft Entra ID (a confirmar com o consultor).
- **Spec da API do provedor é parcial**: autenticação, assinatura de webhook, paginação, rate limits e erros pendentes.

## Premissas

- Massa de dados no ZIP é 100% sintética (declaração do consultor + README do ZIP); dado real de cliente NUNCA entra no Git.
- Repo privado no plano Free: proteção de main "Not enforced" — premissa de risco dos Testes 1 e 2; produção real exige org + plano Team.

## Blockers

- **Credenciais do sandbox da API do provedor** — não recebidas. Bloqueia: integração de consulta e webhooks. Ação: AuctaPay solicitar ao provedor. Owner: Mariana Torres (sponsor) / a detalhar.
- **Configuração do login corporativo (Entra ID)** — não recebida. Bloqueia: autenticação e release em homologação. Ação: TI AuctaPay fornecer tenant/client. Owner: Segurança da Informação.
- **Titularidade e licenças do código legado não verificadas** — LICENSE_STATUS.md confirma; `legacy-match-sdk` sem licença/fonte. Bloqueia: reutilização de qualquer trecho/dependência do legado (não bloqueia baseline nem diagnóstico — baseline não usa o SDK). Ação: AuctaPay localizar contrato do fornecedor; revisão jurídica das dependências. Owner: Mariana Torres.
- **Spec da API do provedor incompleta** — auth/assinatura/paginação/erros pendentes. Bloqueia: desenho final da integração. Ação: AuctaPay obter spec completa do provedor.

## Achados de ambiente

- Conector GitHub desta sessão NÃO cria repositórios (403); secret scanning via API indisponível (sem Advanced Security no plano Free) — varredura local por grep aplicada.
- Conector M365 operacional; NÃO lê arquivos ZIP (validação de MIME) — ZIP recebido por anexo na conversa.

## Retomada

- Próximo passo: fechar F (dados em homolog), H (infra alvo), confirmar Entra ID; depois D (mecanismo de aceite), E (nomes ERP/provedor), N (sustentação); consolidar artefatos canônicos.
