# AuctaPay Concilia — DATA_CATALOG.md

> Inventário e avaliação das fontes de dados (blueprint 2.4). Uma seção por fonte, com os 8 campos mínimos. O catálogo é um mapa — não contém cópias das bases. Aprofundamento acontece na tarefa que precisar; o que não foi verificado fica marcado `não validado`.

## Fonte 1 — Código legado Concilia 0.8 (snapshot)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | ZIP `01_Projeto_Legado_Concilia.zip` na pasta oficial (OneDrive `Aucta Blueprint Dev AI/inputs/teste 3`); snapshot read-only versionado em `legacy/` (tag `baseline-v0`) |
| Owner | AuctaPay (titularidade jurídica NÃO confirmada — fornecedor anterior; ver TRUTH-005) |
| Uso na solução | Referência de comportamento (baseline de caracterização); NÃO é insumo de reutilização até liberação de IP/licenças |
| Estrutura | app.py (Flask, 1 endpoint POST /reconcile), reconcile.py (regra de matching), storage.py (SQLite), requirements.txt, docs/, baseline/, synthetic/ |
| Qualidade | Sem autenticação, debug=True, secret demo hardcoded, SQLite ao lado do código, sem testes, ambiente original não pinado; 3 dependências declaradas e não usadas (requests, fuzzywuzzy, legacy-match-sdk) |
| Status de evidência | observado (leitura integral dos 14 arquivos, 2026-09-03) |
| Sensibilidade | Interno; SEM dados reais; publicação/redistribuição PROIBIDA (pendência de IP) |
| Atualização | Congelado (snapshot); qualquer nova entrega do fornecedor exige saneamento de segredos antes de importar (TRUTH-014) |

## Fonte 2 — Massa sintética de títulos (titles.json)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | `legacy/synthetic/titles.json` (3 registros) |
| Owner | Aucta (massa criada para o teste; declaração + README do ZIP) |
| Uso na solução | Insumo dos golden cases e das fixtures de desenvolvimento |
| Estrutura | title_id (chave), documento, cnpj, cliente, email, telefone, valor, moeda, vencimento |
| Qualidade | 3 registros consistentes; sem nulls; datas ago/2026 |
| Status de evidência | observado |
| Sensibilidade | Sintética (TRUTH-011) — MAS o formato contém campos de PII (CNPJ, nome, e-mail, telefone): a versão REAL será PII/confidencial e NUNCA entra no Git (TRUTH-008) |
| Atualização | Estática (massa de teste) |

## Fonte 3 — Massa sintética de pagamentos (payments.json)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | `legacy/synthetic/payments.json` (3 registros) |
| Owner | Aucta (massa de teste) |
| Uso na solução | Insumo dos golden cases; simula retorno da API do provedor |
| Estrutura | payment_id (chave), event_id, documento, cnpj, valor, moeda, data_pagamento |
| Qualidade | ARMADILHAS INTENCIONAIS mapeadas: P002 com valor 504,00 vs título 500,00 (aproximado); P003 com documento NF-9999 sem título correspondente (órfão — o legado o IGNORA silenciosamente) |
| Status de evidência | observado |
| Sensibilidade | Sintética; formato real terá PII — mesma regra da Fonte 2 |
| Atualização | Estática (massa de teste) |

## Fonte 4 — Amostra de webhook (webhook_sample.json)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | `legacy/synthetic/webhook_sample.json` |
| Owner | Aucta (massa de teste, formato presumido do provedor) |
| Uso na solução | Referência inicial do payload de webhook (payment.updated) |
| Estrutura | event_id, event_type, occurred_at, payment{payment_id, documento, valor, moeda} |
| Qualidade | 1 exemplo; SEM campo de assinatura — validação de autenticidade indefinida na spec parcial |
| Status de evidência | observado (amostra) / inferido (representatividade do formato real) |
| Sensibilidade | Sintética; produção terá dados transacionais reais |
| Atualização | Estática; formato definitivo depende da spec completa (blocker) |

## Fonte 5 — Baseline esperada (baseline_expected.json)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | `legacy/baseline/baseline_expected.json` |
| Owner | Rafael Costa (dono do número — validação formal pendente, gate do 1º /change-number) |
| Uso na solução | REFERÊNCIA EXTERNA dos golden cases (ACC-001/ACC-002); evidence_status = observed_not_approved |
| Estrutura | version, evidence_status, input, expected_legacy_output[3], known_concern (T002) |
| Qualidade | Reproduzida 2× de forma independente (harness 3/3; recomputação manual da regra 3/3, 2026-09-03) |
| Status de evidência | observado |
| Sensibilidade | Interno |
| Atualização | Congelada com a tag baseline-v0; muda apenas por decisão registrada do dono do número |

## Fonte 6 — ERP da AuctaPay (títulos reais)

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | Sistema a nomear pelo consultor; mecanismo de extração a definir (arquivo? API? base?) |
| Owner | Financeiro AuctaPay (inferido) |
| Uso na solução | Fonte oficial dos títulos em produção (M3 — Ingestão ERP) |
| Estrutura | não validado — presumida compatível com o formato de titles.json |
| Qualidade | não validado |
| Status de evidência | não validado |
| Sensibilidade | PII + confidencial (CNPJ, nomes, e-mails, telefones, valores, observações de cobrança) — NUNCA no Git; homolog só mascarado (TRUTH-008); fixtures sintéticas em tests/fixtures/ |
| Atualização | não validado (presumida diária/contínua) |

## Fonte 7 — API do provedor de pagamentos

| Campo | Conteúdo |
| --- | --- |
| Fonte e localização | Provedor a nomear; spec parcial em `legacy/docs/api_provider_partial.yaml` (GET /payments, POST /webhooks/payment) |
| Owner | Provedor de pagamentos (externo); relacionamento: AuctaPay |
| Uso na solução | Fonte oficial dos pagamentos em produção (consulta + webhooks — M5) |
| Estrutura | Parcial: endpoints conhecidos; autenticação, assinatura de webhook, paginação, rate limits e erros PENDENTES |
| Qualidade | não validado (sem acesso ao sandbox) |
| Status de evidência | não validado (spec parcial observada; comportamento não testável) |
| Sensibilidade | Dados transacionais reais em produção; credenciais em cofre de segredos, nunca no código (.env) |
| Atualização | Tempo real (webhooks) + consulta sob demanda |

## Regras de tratamento e casos de controle

- Golden cases materializados em `tests/fixtures/golden_cases.csv` (GC-01..03, com colunas intermediárias) — conferidos por recomputação INDEPENDENTE da regra documentada (fora do código legado), 3/3, 2026-09-03. Tolerância proposta: R$ 0,00 (baseline determinística). GATE: validação formal de Rafael Costa antes do 1º /change-number.
- Exceções esperadas em `tests/fixtures/expected_exceptions.csv` (EX-01..05) — inclui o pagamento órfão P003 que o legado ignora (TRUTH-015) e o defeito candidato T002 (TRUTH-003).
- Estratégia detalhada em `tests/TEST_STRATEGY.md`.
