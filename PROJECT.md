# AuctaPay Concilia — PROJECT.md

> Memória canônica compacta (blueprint 6.1). Contém objetivo, escopo, estado atual, risk tier, arquitetura em uma página e o mapa de navegação. Não é diário de trabalho: detalhes de features vivem em Issues/PRs; fatos e regras vigentes em TRUTHS.md. Atualizado por PR quando o entendimento do projeto muda.

## Objetivo

Substituir o protótipo local Concilia (Flask, criado por fornecedor anterior) por uma aplicação web interna de conciliação de recebimentos: títulos do ERP × transações do provedor de pagamentos, com fila de divergências, aprovação manual de matches, histórico em banco e relatórios. Uso simultâneo por Financeiro, Cobrança e Auditoria, com login corporativo.

**Decisão apoiada:** aprovar ou rejeitar matches de conciliação, tratar divergências e priorizar ações de cobrança, com trilha completa para auditoria.
**KPI de sucesso:** menos tempo para conciliar; menos divergências sem tratamento; rastreabilidade para auditoria; fim do trabalho manual em planilha.

## Usuários

- **Financeiro** — conciliação do dia a dia e aprovação de matches.
- **Cobrança** — tratamento da fila de divergências (títulos sem pagamento, diferenças de valor).
- **Auditoria** — leitura e trilha de quem aprovou o quê e quando.

## Escopo

**In scope (v1):** importação de títulos do ERP; consulta à API do provedor; recepção de webhooks; histórico em banco de dados (PostgreSQL previsto); aprovação manual de matches; relatórios de conciliação; login corporativo (Entra ID); ambientes de homologação e produção.
**Out of scope (v1):** alterar as regras de matching (a v1 replica fielmente o comportamento observado do legado); corrigir defeitos do legado sem aprovação do dono do número; redistribuir ou publicar o código legado.
**Premissas e restrições (inegociáveis):**
- Baseline reproduzível do legado ANTES de qualquer alteração; comportamento observado ≠ regra aprovada (taxonomia: comportamento observado / regra confirmada / hipótese / defeito conhecido).
- Reutilização de código e dependências do legado SUSPENSA até verificação de titularidade e licenças.
- Dado real de cliente (CNPJ, nomes, e-mails, telefones) NUNCA entra no Git; homologação só com dados mascarados/sintéticos.
- Arquitetura em Azure condicionada a aprovação formal (gate de release).

## Risk tier

| Tier | Gatilhos | Justificativa |
| --- | --- | --- |
| 3 | autenticação + múltiplos perfis (3); integrações ERP/API/webhooks (2); números de conciliação para decisão + dados de cliente (2); deploy homolog/prod (1) | Login corporativo com perfis distintos e integrações centrais colocam o projeto no tier máximo; mudanças individuais são reclassificadas pelo router do plugin. |

## Arquitetura em uma página

**Legado (Concilia 0.8, observado):** Flask local com um endpoint (`POST /reconcile`), matching por documento igual + tolerância de R$ 5,00, SQLite ao lado do código, sem autenticação, modo debug, sem testes. Ambiente original não documentado de forma reproduzível.

**Alvo (v1):** aplicação web interna em Azure da AuctaPay (aprovação formal de arquitetura pendente) com: SSO Microsoft Entra ID e perfis Financeiro/Cobrança/Auditoria; ingestão de títulos do ERP (sistema a nomear); cliente da API do provedor de pagamentos + receptor de webhooks com assinatura validada (spec parcial — pendências formais); banco PostgreSQL com histórico e trilha de aprovação; motor de matching em modo replicação fiel do legado; fila de divergências com aprovação manual; relatórios de conciliação. Estratégia de backup operacional (app + PostgreSQL) depende de RPO/RTO aprovados com a arquitetura.

## Estado atual

Em iniciação (/init em andamento) — 2026-09-03.

## Owners (resumo)

Sponsor: Mariana Torres (CFO) · Dono do número: Rafael Costa (Controladoria) · Produção: aprovação conjunta Rafael Costa + Segurança da Informação · Owner técnico: Aucta (Caio Ferrari). Detalhe em OWNERS.md.

## Mapa de navegação

| Artefato | Onde | O que contém |
| --- | --- | --- |
| TRUTHS.md | raiz | Fatos e regras vigentes |
| GLOSSARY.md | raiz | Vocabulário canônico |
| ACCEPTANCE.md | raiz | Aceite, definição de pronto e estratégia de provas |
| OWNERS.md | raiz | Papéis e responsáveis |
| DATA_CATALOG.md | .project/ | Fontes de dados (gerado no init-data) |
| init-state.md | .project/ | Estado do /init |
