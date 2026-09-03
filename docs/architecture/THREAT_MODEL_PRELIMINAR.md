# Threat model preliminar — AuctaPay Concilia (tier 3)

**Versão:** preliminar 0.1 · **Data:** 2026-09-03 · **Produzido em:** iniciação (/init)
**Status:** NÃO aprovado — insumo obrigatório do primeiro `/architecture`, que aprofunda e aprova.

> Por que existe agora: o `/init` classificou o projeto como tier 3 (autenticação com perfis, integrações centrais, PII, números entregues). Um threat model que só nasce no `/architecture` faria a arquitetura começar sem entender os riscos que precisa resolver. Este documento registra ativos, atores, fronteiras, ameaças, controles já exigidos e **decisões abertas com owner decisor** — sem propor controles técnicos definitivos.

## 1. Ativos

| # | Ativo | Por que importa | Onde vive |
| --- | --- | --- | --- |
| A1 | Títulos do ERP (com PII: CNPJ, nome, e-mail, telefone, valores, vencimentos) | Base da conciliação; dado pessoal e comercial de cliente | ERP (a nomear) → banco da solução |
| A2 | Transações do provedor de pagamentos | Contraparte do matching; dado financeiro | API do provedor → banco da solução |
| A3 | Resultado da conciliação (matches, status, fila de divergências) | **Número entregue** que sustenta decisão de cobrança e auditoria | Banco + relatórios |
| A4 | Trilha de aprovação (quem aprovou o quê, quando, por quê) | Prova para auditoria; alvo de repúdio/adulteração | Banco (histórico) |
| A5 | Credenciais e segredos (API do provedor, assinatura de webhook, banco, Entra ID) | Comprometimento dá acesso a dado financeiro e à identidade da aplicação | Cofre/variáveis de ambiente (a definir) |
| A6 | Observações de cobrança (texto livre) | Pode conter dado pessoal sensível não estruturado | Banco + telas |
| A7 | Baseline do legado (`legacy/` @ `baseline-v0`) | Referência de comportamento; se corrompida, perde-se a prova do estado original | Repositório (privado) |
| A8 | Regras e parâmetros de conciliação (ex.: tolerância de R$ 5,00) | Alterar muda número entregue ao cliente | Código + TRUTHS + golden cases |

## 2. Atores

| Ator | Tipo | Interesse legítimo | Risco associado |
| --- | --- | --- | --- |
| Financeiro | interno, autenticado | Conciliar e aprovar matches | Aprovação indevida; excesso de permissão |
| Cobrança | interno, autenticado | Tratar divergências | Acesso a PII além do necessário |
| Auditoria | interno, autenticado | Ler e auditar trilha | Deveria ser somente leitura — escrita indevida quebra a prova |
| Rafael Costa (dono do número) | interno, decisor | Aprovar regras e mudanças de número | Mudança de número sem sua aprovação |
| Segurança da Informação | interno, decisor | Identidade, segredos, políticas de dado | — |
| ERP | sistema interno | Fornecer títulos | Dado inconsistente ou extração excessiva (mais campos que o necessário) |
| Provedor de pagamentos | **terceiro externo** | Enviar/expor pagamentos | Webhook forjado, replay, indisponibilidade, mudança de contrato |
| Fornecedor anterior | terceiro, sem acesso | — | Código de titularidade não confirmada; histórico com segredo revogado |
| Agente de IA (Aucta) | automação com acesso ao repo | Desenvolver sob os workflows | Vazar dado real para o Git; alterar número sem gate |
| Atacante externo não autenticado | adversário | — | Alcançar o endpoint de webhook, que é necessariamente exposto |

## 3. Trust boundaries

| # | Fronteira | O que atravessa | Confiança |
| --- | --- | --- | --- |
| B1 | Internet → receptor de webhook | Eventos de pagamento do provedor | **NÃO confiável** — único ponto exposto a não autenticado; exige assinatura válida e idempotência |
| B2 | Solução → API do provedor (saída) | Consultas autenticadas | Confiança condicionada a credencial e TLS; resposta é dado externo, não instrução |
| B3 | ERP → solução | Extração de títulos com PII | Interno, mas exige minimização de campos |
| B4 | Entra ID → solução | Identidade e perfis | Confiável se a validação de token e o mapeamento de perfis estiverem corretos |
| B5 | Usuário (navegador) → solução | Aprovações e consultas | Autenticado, porém autorização por perfil é obrigatória (A4 é adulterável) |
| B6 | Homologação ↔ produção | Dados, credenciais, bancos | **Devem ser separados** — homologação só com massa mascarada (TRUTH-008) |
| B7 | Solução → repositório Git / logs / relatórios | PII pode escapar por engano | Nenhum dado real no Git (TRUTH-008); política de PII em logs a definir |
| B8 | Código do fornecedor anterior → nova solução | Código e dependências | **Bloqueada** até liberação de IP/licenças (TRUTH-005) |

## 4. Ameaças principais

| # | Ameaça | Ativo / fronteira | Impacto | Severidade preliminar |
| --- | --- | --- | --- | --- |
| T1 | Webhook forjado por terceiro não autenticado cria pagamento inexistente | B1 / A2, A3 | Conciliação e cobrança baseadas em pagamento falso | **Alta** |
| T2 | Replay do mesmo evento duplica pagamento ou baixa em duplicidade | B1 / A3 | Número entregue errado | **Alta** |
| T3 | Perfil com permissão excessiva aprova match ou altera trilha (Auditoria escrevendo, Cobrança aprovando) | B5 / A3, A4 | Perda da segregação de funções e da prova de auditoria | **Alta** |
| T4 | PII vazando por log, mensagem de erro, exportação de relatório ou fixture | B7 / A1, A6 | Incidente de dado pessoal (LGPD) | **Alta** |
| T5 | Segredo em código, log, documento ou histórico importado do fornecedor | A5 | Acesso indevido à API e ao banco | **Alta** (parcialmente mitigada: TRUTH-014) |
| T6 | Mudança silenciosa de regra ou parâmetro altera número sem aprovação | A8 / A3 | Cliente decide sobre número não aprovado | **Alta** (mitigada hoje: golden + gate Muda-numero + CI, provado no PR #1) |
| T7 | Dado real de cliente entrando em homologação ou no Git | B6, B7 / A1 | Exposição de PII em ambiente de menor controle | **Alta** (mitigada por TRUTH-008; segregação de ambientes a definir) |
| T8 | Adulteração ou perda da trilha de aprovação | A4 | Auditoria sem prova | Média-alta |
| T9 | Indisponibilidade ou mudança de contrato da API do provedor | B2 / A2 | Conciliação para; falhas silenciosas | Média |
| T10 | Perda de dados sem RPO/RTO definidos | A3, A4 | Reconstrução impossível ou lenta | Média-alta |
| T11 | Migração do histórico do legado (SQLite) corrompendo ou expondo dados | A1, A4 | Base inconsistente na largada | Média (decisão de migrar ou não em aberto) |
| T12 | Reuso inadvertido de código/dependência do legado sem licença | A7 / B8 | Risco jurídico | Média (mitigada por TRUTH-005 e pela regra do plugin) |
| T13 | Retenção indevida de PII por prazo indefinido | A1, A6 | Exposição desnecessária; não conformidade | Média (política em aberto) |

## 5. Controles já exigidos (decididos na iniciação)

| Controle | Origem | Cobre |
| --- | --- | --- |
| Assinatura válida obrigatória no webhook; inválido rejeitado e logado | ACC-004 | T1 |
| Idempotência por `event_id`; replay não duplica efeito | ACC-004, TEST_STRATEGY | T2 |
| Acesso somente via Entra ID; cada perfil vê apenas suas funções | TRUTH-007, ACC-007 | T3 |
| Aprovação manual registra usuário, data/hora e justificativa, visível à Auditoria | ACC-006 | T3, T8 |
| Dado real nunca no Git; homologação só mascarada/sintética | TRUTH-008 | T4, T7 |
| Segredos fora do código (cofre/variáveis) | client-rules item 8 | T5 |
| Saneamento obrigatório antes de importar histórico do fornecedor | TRUTH-014 | T5 |
| Golden cases + gate Muda-numero em três camadas + CI bloqueando merge | ACC-002, /pre-pr, PR #1 | T6 |
| Reuso do legado suspenso até liberação de IP/licenças | TRUTH-005 | T12 |
| Snapshot por release em `backups/` (não substitui backup operacional) | TRUTH-013 | T10 (parcial) |
| Baseline congelada em tag e verificada por harness no CI | ACC-001 | A7 |

## 6. Decisões abertas — com owner decisor e condição de desbloqueio

| # | Decisão | Ameaças | Owner decisor (autoridade) | Workflow de resolução | Condição objetiva de desbloqueio |
| --- | --- | --- | --- | --- | --- |
| D-01 | Matriz RBAC: o que cada perfil pode ler, criar, aprovar e exportar (Auditoria = somente leitura?) | T3 | **Negócio (Rafael Costa) + Segurança da Informação**, com apoio de arquitetura | `/architecture` orquestra; decisão é dos owners | Matriz aprovada por Rafael + SI, anexada à Issue de M8 |
| D-02 | Política de PII em logs, mensagens de erro, telas e exportações | T4 | **Segurança da Informação / LGPD + operação** | `/architecture` documenta; decisão da SI | Política escrita, aprovada pela SI, com regra de mascaramento por campo |
| D-03 | Retenção de dados: prazo de guarda de conciliações, trilha e logs | T13, T4 | **Jurídico/LGPD + negócio (Rafael Costa)** — não é decisão de arquitetura | Decisão de negócio registrada em Issue; ADR só documenta | Prazos definidos por classe de dado, com base legal citada |
| D-04 | Segregação de ambientes: credenciais, bancos, cofres e quem acessa homolog × produção | T7, T5 | **Segurança da Informação + arquitetura** | `/architecture` + aprovação da SI | Desenho de ambientes aprovado, sem credencial compartilhada |
| D-05 | RPO/RTO e estratégia de backup operacional (app + PostgreSQL) | T10 | **Negócio (Mariana/Rafael) + operação + arquitetura** | Decisão de negócio + `/architecture` | RPO e RTO numéricos aprovados; plano de backup correspondente |
| D-06 | Migrar ou não o histórico do SQLite do legado | T11 | **Rafael Costa (dono do dado) + arquitetura** | `/architecture` (plano de migração) | Decisão registrada; se migrar, plano com validação e rollback |
| D-07 | Procedimento de rollback por release | T8, T10 | **Arquitetura + operação** | `/architecture` | Procedimento testado em homologação |
| D-08 | Contrato definitivo do webhook: mecanismo de assinatura, retries, janela de replay | T1, T2, T9 | **Arquitetura técnica + provedor (externo)** | `/architecture` após spec completa | Spec completa recebida + implementação com teste de assinatura inválida e replay |
| D-09 | Minimização de campos na extração do ERP (só o necessário) | T4 | **Rafael Costa + Segurança da Informação** | `/architecture` (desenho da ingestão) | Lista de campos aprovada |
| D-10 | Aprovação formal da arquitetura Azure | T7, T10 | **Segurança da Informação + Rafael Costa** | Aprovação formal fora do repo, registrada em Issue | Registro de aprovação anexado antes do primeiro deploy |
| D-11 | Observabilidade: o que é logado, alertado e monitorado (sem PII) | T4, T8, T9 | **Operação + Segurança da Informação** | `/architecture` | Plano de logs/alertas aprovado, coerente com D-02 |

**Regra de alçada:** o `/architecture` **orquestra e documenta** (ADR), mas não tem autoridade para decidir retenção, RPO/RTO, política de dados ou RBAC. Cada linha acima só fecha com o registro da decisão do owner indicado.

## 7. O que este documento NÃO faz

Não escolhe tecnologia, não define esquema de banco, não especifica mecanismo de autenticação nem desenha o pipeline. Isso é `/architecture` (com ADR e segundo revisor). Aqui está apenas o mapa de risco que a arquitetura precisa resolver — e quem decide o quê.
