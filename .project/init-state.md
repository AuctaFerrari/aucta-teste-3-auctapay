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
| init-interview | em_andamento | 2026-09-03 | blocos A e B fechados; rodada C/D/H em andamento |
| init-repo | pendente | | repo criado via template (bootstrap assistido 2026-09-03) |
| init-data | pendente | | |
| init-plugin | pendente | | |
| init-check | pendente | | |

## init-interview — blocos

| Bloco | Status | Notas |
| --- | --- | --- |
| A. Problema e objetivo | concluida | confirmado pelo consultor 2026-09-03; KPIs: tempo de conciliação, divergências tratadas, rastreabilidade p/ auditoria, fim do manual em planilha |
| B. Escopo e fronteiras | concluida | v1 replica regras de matching fielmente; correção de regras = fora da v1; reutilização de código/deps NÃO autorizada até verificação de IP/licenças; sem implementação/refactor durante o /init |
| C. Stakeholders e decisão | em_andamento | usuários: Financeiro, Cobrança, Auditoria; nomes de sponsor/valida-número/autoriza-release pendentes |
| D. Entregáveis e aceite | em_andamento | web interna, homolog+prod; critérios de aceite a consolidar |
| E. Dados e fontes (inventário) | em_andamento | ZIP legado + ERP + API provedor + webhooks; nomes dos sistemas pendentes |
| F. Segurança e privacidade | pendente | GATILHO: PII real (CNPJ, nome, e-mail, telefone), login corporativo — aprofundar |
| G. IP e licenças | em_andamento | GATILHO CONFIRMADO: código de fornecedor anterior; reutilização suspensa até verificação de titularidade/licenças (decisão do consultor 2026-09-03) — blocker registrado |
| H. Arquitetura inicial | pendente | GATILHO: integrações (ERP, API, webhooks), banco, homolog/prod — aprofundar |
| I. Ambientes e acessos | pendente | homologação e produção previstos |
| J. Repositório e governança | pendente | executado no init-repo |
| K. Estratégia de testes | pendente | GATILHO: baseline reproduzível do legado (incluindo comportamentos incorretos) antes de qualquer alteração |
| L. Conhecimento canônico | pendente | taxonomia de evidência definida (ver Decisões de método) |
| M. Plugin e skill stack | pendente | executado no init-plugin |
| N. Release e sustentação | pendente | |
| O. Baseline | pendente | executado no init-repo; baseline preserva comportamento OBSERVADO, inclusive defeitos — observado ≠ regra aprovada |

## Decisões de método (consultor, 2026-09-03)

- Baseline reproduz o comportamento observado do legado, inclusive incorreto; comportamento observado NÃO é regra aprovada da nova solução.
- Toda regra do legado será classificada em: **comportamento observado / regra confirmada / hipótese / defeito conhecido** (extensão da taxonomia de evidência do blueprint 4.2).
- Durante o /init: apenas inventariar, diagnosticar, preservar baseline, classificar riscos e produzir artefatos. Nenhuma implementação, refactor ou correção do legado.

## Premissas

- Massa de dados no ZIP é 100% sintética (declaração do consultor); dado real de cliente NUNCA entra no Git.
- Repo privado no plano Free: proteção de main "Not enforced" — mesma premissa de risco dos Testes 1 e 2; produção real exige org + plano Team.

## Blockers

- **Credenciais do sandbox da API do provedor de pagamentos** — não recebidas. Bloqueia: implementação/teste da integração de consulta e webhooks (não bloqueia iniciação, baseline nem ingestão do ERP). Ação: AuctaPay solicitar ao provedor. Owner: a definir no bloco C.
- **Configuração do login corporativo (SSO)** — não recebida. Bloqueia: implementação da autenticação e release em homologação (não bloqueia iniciação nem desenvolvimento local). Ação: AuctaPay/TI fornecer parâmetros. Owner: a definir no bloco C.
- **Titularidade e licenças do código legado não verificadas** — código de fornecedor anterior. Bloqueia: reutilização de qualquer trecho/dependência do legado na nova solução (não bloqueia baseline, leitura nem diagnóstico). Ação: AuctaPay verificar contrato com fornecedor; Aucta auditar licenças das bibliotecas no init-data. Owner: a definir no bloco C.
- **ZIP do legado ainda não recebido pelo agente** — conector M365 não lê ZIP (mime bloqueado — confirmado 2026-09-03). Bloqueia: init-data e baseline (bloco O). Ação: consultor anexar o ZIP na conversa (informou que está anexando; arquivo ainda não chegou à sessão).

## Achados de ambiente

- Conector GitHub desta sessão NÃO cria repositórios (403) — bootstrap via template "Use this template" (2 cliques do consultor), consistente com Testes 1 e 2 (capacidade AUTO*).
- Conector M365 operacional (conta caio.ferrari@aucta.capital); NÃO lê arquivos ZIP (validação de MIME type — só documentos Office/PDF/texto/imagem).

## Retomada

- Próximo passo: fechar bloco C (nomes de sponsor, quem valida número, quem autoriza release) e D/H (aceite, stack e infra de homolog/prod); receber o ZIP para liberar init-data/baseline.
