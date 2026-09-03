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
| init-interview | pendente | | |
| init-repo | pendente | | repo criado via template (bootstrap assistido 2026-09-03) |
| init-data | pendente | | |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | pendente | briefing inicial do consultor já cobre parte — confirmar, não re-perguntar |
| B. Escopo e fronteiras | pendente | idem |
| C. Stakeholders e decisão | pendente | usuários: Financeiro, Cobrança, Auditoria |
| D. Entregáveis e aceite | pendente | |
| E. Dados e fontes (inventário) | pendente | detalhamento no init-data; ZIP legado + ERP + API provedor + webhooks |
| F. Segurança e privacidade | pendente | GATILHO DE RISCO: PII real (CNPJ, nome, e-mail, telefone), login corporativo — aprofundar |
| G. IP e licenças | pendente | GATILHO: código de fornecedor anterior; reutilização de bibliotecas incerta — aprofundar |
| H. Arquitetura inicial | pendente | GATILHO: integrações (ERP, API, webhooks), banco, homolog/prod — aprofundar |
| I. Ambientes e acessos | pendente | homologação e produção previstos |
| J. Repositório e governança | pendente | executado no init-repo |
| K. Estratégia de testes | pendente | GATILHO: baseline do legado obrigatória antes de alterar — aprofundar |
| L. Conhecimento canônico | pendente | |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | pendente | |
| O. Baseline | pendente | executado no init-repo; comportamento atual não pode ser perdido (exigência do consultor) |

## Premissas

- Massa de dados anexada é 100% sintética (declaração do consultor); dado real de cliente NUNCA entra no Git.
- Repo privado no plano Free: proteção de main "Not enforced" — mesma premissa de risco dos Testes 1 e 2; produção real exige org + plano Team.

## Blockers

- **Credenciais do sandbox da API do provedor de pagamentos** — não recebidas. Bloqueia: implementação/teste da integração de consulta e webhooks (não bloqueia iniciação, baseline nem fase de ingestão do ERP). Ação: AuctaPay solicitar ao provedor. Owner: a definir no bloco C.
- **Configuração do login corporativo (SSO)** — não recebida. Bloqueia: implementação da autenticação e release em homologação (não bloqueia iniciação nem desenvolvimento local). Ação: AuctaPay/TI fornecer parâmetros. Owner: a definir no bloco C.
- **ZIP do legado ainda não lido pelo agente** — arquivo em OneDrive (`Aucta Blueprint Dev AI/inputs/teste 3/01_Projeto_Legado_Concilia.zip`); conector M365 pode não extrair binário ZIP. Bloqueia: init-data (inventário do código/dados) e baseline (bloco O). Ação em andamento: tentativa de leitura via conector; fallback = anexar o ZIP na conversa.

## Achados de ambiente

- Conector GitHub desta sessão NÃO cria repositórios (403) — bootstrap via template "Use this template" (2 cliques do consultor), consistente com Testes 1 e 2 (capacidade AUTO*).
- Conector M365 operacional (conta caio.ferrari@aucta.capital).

## Retomada

- Próximo passo: localizar/ler o ZIP do legado; em paralelo, iniciar init-interview (bloco A) confirmando o briefing já fornecido.
