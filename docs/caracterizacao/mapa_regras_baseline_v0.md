# M2 — Mapa das regras observadas da `baseline-v0`

**Issue:** #7 · **Data:** 2026-09-03 · **Fonte única:** `legacy/` na tag `baseline-v0` (commit 6895c92) · **Massa:** 100% sintética

> **O que este documento é:** a descrição do que o sistema atual **faz de fato**, com evidência por regra e uma **proposta** de classificação para o dono do número decidir.
>
> **O que este documento NÃO é:** especificação da nova solução, decisão de negócio, nem análise do que o legado deixa de fazer (escopo definido pelo consultor: apenas o que a baseline executa). Nenhuma linha de `legacy/` foi alterada.
>
> **Classificação (GLOSSARY):** *regra confirmada* = deve valer na nova solução · *hipótese* = plausível, precisa de confirmação · *defeito conhecido* = observado e considerado incorreto. Nada aqui está decidido: **a decisão é de Rafael Costa no M3.**

## Como as regras foram levantadas

1. Leitura integral de `legacy/reconcile.py`, `legacy/app.py` e `legacy/storage.py` na tag `baseline-v0`.
2. **Sondagens de comportamento** (E1–E7): entradas sintéticas construídas para isolar uma pergunta cada, executadas contra o motor legado sem modificá-lo. Nenhuma sondagem foi persistida no repo como fixture — elas são evidência deste mapa, não casos de teste.
3. Cruzamento com os golden cases (GC-01..03) e exceções esperadas (EX-01..05) já materializados na iniciação.

Resultados das sondagens (executadas em 2026-09-03):

| Sondagem | Pergunta | Entrada | Saída observada |
| --- | --- | --- | --- |
| E1 | A tolerância inclui exatamente R$ 5,00? | dif. 5,00 e dif. 5,01 | 5,00 → APPROVED · 5,01 → OPEN |
| E2 | O mesmo pagamento pode casar com dois títulos? | 2 títulos de mesmo documento e valor, 1 pagamento | **Ambos APPROVED com o MESMO `payment_id`** |
| E3 | Havendo dois candidatos válidos, qual vence? | pagamento com dif. 4,00 antes do exato | Vence o **primeiro da lista**, não o mais próximo |
| E4 | A moeda é considerada? | título BRL × pagamento USD, mesmo valor | APPROVED — **moeda ignorada** |
| E5 | Pagamento a menos e a mais são tratados igual? | dif. −4,00 e +4,00 | Ambos APPROVED — tolerância **absoluta** |
| E6 | A comparação é em ponto flutuante? | 0.1+0.2 × 0.3 (dif. ~5,5e−17) | APPROVED — comparação em `float` |
| E7 | O que é gravado como data? | título sem candidato | `processed_on` = **data da execução**, não do pagamento |

## Mapa de regras

| # | O que o sistema atual faz (linguagem de negócio) | Evidência | Classificação proposta | Justificativa (uma linha) |
| --- | --- | --- | --- | --- |
| R-01 | **Percorre a lista de títulos** e, para cada título, procura um pagamento. A saída tem exatamente uma linha por título. | `reconcile.py` laço `for title in titles`; GC-01..03 (3 títulos → 3 linhas) | **Regra confirmada** | O relatório de conciliação é orientado a recebível; uma linha por título é o que o Financeiro trata. |
| R-02 | **Casa por documento idêntico** (número da nota): sem igualdade exata do documento, não há candidato. | `payment.get("documento") == title.get("documento")`; GC-03 (NF-1003 × NF-9999 → OPEN) | **Regra confirmada** | Documento é a chave de negócio natural entre ERP e provedor. |
| R-03 | **Aceita diferença de valor de até R$ 5,00, inclusive**, em qualquer direção (pagou a mais ou a menos). | `abs(...) <= 5.00`; sondagens E1 e E5; EX-04 | **Hipótese** | O critério existe e opera, mas o valor R$ 5,00 não tem fonte, dono nem data — só vira regra após decisão do dono do número. |
| R-04 | **Aprova automaticamente** o título que encontra candidato — sem intervenção humana, sem registro de quem aprovou. | `status = "APPROVED"`; GC-01/GC-02 | **Defeito conhecido** | A nova solução exige aprovação manual com trilha (ACC-006); aprovação automática sem rastro contradiz o objetivo de auditoria. |
| R-05 | **Aprova match aproximado dentro da tolerância mesmo quando o pagamento ocorre após o vencimento** (caso T002: dif. R$ 4,00, pago 1 dia depois). | GC-02; TRUTH-003; `known_concern` do próprio ZIP | **Defeito conhecido** | O legado declara o caso como preocupação conhecida; aprovar diferença de valor sem tratar atraso mistura dois julgamentos distintos. |
| R-06 | **Marca como OPEN o título sem candidato**, com pagamento vazio. | `status = "OPEN"`, `payment_id = None`; GC-03 | **Regra confirmada** | É a origem da fila de divergências que Cobrança trata. |
| R-07 | **Pega o primeiro pagamento da lista que satisfaz o critério**, não o mais próximo em valor nem o mais próximo em data. | `next((...), None)`; sondagem E3 | **Defeito conhecido** | Resultado depende da ordem em que o provedor devolveu os dados — mesma entrada em ordem diferente pode conciliar pagamento diferente. |
| R-08 | **Não marca pagamento como consumido**: o mesmo pagamento pode ser associado a vários títulos. | Sondagem E2 (dois títulos, mesmo `payment_id`) | **Defeito conhecido** | Um recebimento aparecendo como baixa de dois títulos infla a conciliação e distorce a cobrança. |
| R-09 | **Ignora a moeda** na comparação: título em BRL casa com pagamento em outra moeda de mesmo valor numérico. | Sondagem E4 (campo `moeda` existe nas duas bases e não é lido) | **Defeito conhecido** | O dado está disponível e não é usado; se houver qualquer operação não-BRL, o match é inválido. |
| R-10 | **Só reporta títulos**: pagamento que não casa com nenhum título não aparece em nenhuma saída (caso P003, documento NF-9999). | TRUTH-015; EX-01; saída de GC-01..03 (3 linhas para 3 pagamentos, P003 ausente) | **Defeito conhecido** | Dinheiro recebido sem título correspondente fica invisível — exatamente o tipo de divergência que a nova fila precisa mostrar. |
| R-11 | **Compara valores em ponto flutuante**, sem arredondamento explícito para centavos. | Sondagem E6 | **Hipótese** (de risco técnico) | Hoje inofensivo pela folga de R$ 5,00; vira risco real se a tolerância cair para zero ou centavos — decisão técnica a registrar em M4. |
| R-12 | **Grava como data do processamento a data em que o cálculo rodou** (`processed_on`), não a data do pagamento nem a do vencimento. | Sondagem E7; EX-05 | **Regra confirmada** (com ressalva) | Registrar quando a conciliação rodou é legítimo; a nova solução deve manter isso **e** preservar as datas de negócio, hoje descartadas da saída. |
| R-13 | **Não guarda histórico na prática**: existe código de gravação em SQLite (`storage.py`), mas o endpoint não o chama — cada execução devolve o resultado e nada persiste. | `app.py` não importa `storage`; `save_result` sem chamador | **Defeito conhecido** | Explica por que hoje não há trilha nem série histórica; também significa que **não existe base legada de resultados a migrar** (insumo da decisão D-06 do threat model). |
| R-14 | **Recebe títulos e pagamentos no corpo da chamada**: não busca no ERP nem no provedor — quem chama fornece as duas listas. | `app.py`: `payload["titles"]`, `payload["payments"]` | **Regra confirmada** (como fato do legado) | Confirma que a integração com ERP e provedor é capacidade **nova** (M6/M7), não rescrita de algo existente. |

**Resumo da proposta:** 5 regras confirmadas · 2 hipóteses · 7 defeitos conhecidos.

### Onde cada caso de controle se encaixa

| Caso | Regras que exercita |
| --- | --- |
| GC-01 (match exato) | R-01, R-02, R-03, R-04, R-12 |
| GC-02 (T002, aproximado e atrasado) | R-03, R-04, **R-05** |
| GC-03 (título sem pagamento) | R-02, R-06 |
| EX-01 (P003 órfão) | **R-10** |
| EX-04 (tolerância sem fonte) | **R-03** |
| EX-05 (`processed_on` não determinístico) | R-12 |
| _sem caso de controle hoje_ | **R-07** (ordem decide), **R-08** (pagamento reutilizado), **R-09** (moeda ignorada) — lacuna a cobrir em M3/M4 |

## Perguntas para o dono do número (M3) — uma decisão cada

| # | Pergunta | Regra | Por que precisa de você |
| --- | --- | --- | --- |
| Q1 | A tolerância de diferença de valor continua sendo R$ 5,00? | R-03 | Valor sem fonte; precisa de dono, unidade e data para virar parâmetro rastreável. |
| Q2 | A tolerância deve ser um valor fixo em reais ou um percentual do título? | R-03 | Muda o comportamento em títulos grandes e pequenos. |
| Q3 | Diferença dentro da tolerância deve ser aprovada automaticamente ou entrar na fila para aprovação humana? | R-04, R-05 | Define se a nova solução mantém aprovação automática ou exige trilha em todo match aproximado. |
| Q4 | Pagamento após o vencimento deve afetar a conciliação (bloquear, sinalizar ou nada)? | R-05 | Hoje o atraso é invisível ao matching. |
| Q5 | Havendo mais de um pagamento elegível para o mesmo título, qual deve vencer — o de valor mais próximo, o mais antigo, ou fila para decisão humana? | R-07 | Hoje quem decide é a ordem da lista, o que não é critério de negócio. |
| Q6 | Um mesmo pagamento pode dar baixa em mais de um título? | R-08 | Se não, a nova solução precisa consumir o pagamento; se sim (rateio), precisa de regra própria. |
| Q7 | A conciliação opera somente em BRL? | R-09 | Define se a moeda entra como critério obrigatório de match. |
| Q8 | Pagamento sem título correspondente deve aparecer na fila de divergências? | R-10 | Confirma a proposta EX-01 e cria uma classe de divergência que hoje não existe. |
| Q9 | Pagamento parcial (valor muito abaixo do título) tem tratamento próprio? | R-03, R-06 | Hoje cai em OPEN sem distinção — confirmar se é o comportamento desejado. |
| Q10 | Os três golden cases (GC-01..03) e as cinco exceções (EX-01..05) estão corretos como referência da baseline, com tolerância R$ 0,00 na comparação? | todas | É a ratificação formal que libera o M4 (ACC-002). |

## Saída esperada do M3

Para cada regra R-01..R-14: classificação **decidida** (confirmada / defeito) registrada na Issue e promovida a TRUTHS quando mudar como a solução deve ser construída; respostas Q1–Q10 registradas; golden e exceções ratificados. Só depois disso o M4 (especificação) começa.
