# AuctaPay Concilia — GLOSSARY.md

> Vocabulário canônico e termos do cliente (blueprint 6.1). Uma definição por linha.

| Termo | Definição | Fonte |
| --- | --- | --- |
| Título | Recebível emitido no ERP (nota/duplicata) com documento, CNPJ, valor e vencimento | briefing do consultor + synthetic/titles.json |
| Transação / pagamento | Evento de recebimento reportado pelo provedor de pagamentos | briefing + synthetic/payments.json |
| Matching | Associação automática entre um título e um pagamento candidato | reconcile.py (legado) |
| Match aprovado | Associação confirmada (automática no legado; manual ou automática na nova versão, com trilha) | briefing |
| Divergência | Título sem pagamento correspondente, pagamento sem título, ou diferença entre eles | briefing |
| Fila de divergências | Lista de casos pendentes de tratamento por Financeiro/Cobrança | briefing |
| Conciliação | Processo completo: importar, casar, tratar divergências e reportar | briefing |
| Webhook | Aviso automático enviado pelo provedor quando um pagamento muda | docs/api_provider_partial.yaml |
| Baseline | Foto reproduzível do comportamento atual do legado (inclusive defeitos), usada como referência de comparação | decisão do consultor 2026-09-03 |
| Golden case | Caso de conferência com entrada e resultado esperado conhecidos, validado fora do sistema | método Aucta |
| Comportamento observado | O que o legado FAZ, comprovado por execução — sem juízo de correção | decisão do consultor 2026-09-03 |
| Regra confirmada | Comportamento validado pelo dono do número como regra de negócio da nova solução | decisão do consultor 2026-09-03 |
| Hipótese | Interpretação ainda não confirmada de um comportamento ou regra | decisão do consultor 2026-09-03 |
| Defeito conhecido | Comportamento observado classificado como incorreto pelo dono do número | decisão do consultor 2026-09-03 |
