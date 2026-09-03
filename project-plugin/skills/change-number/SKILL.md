---
name: change-number
description: Conduz mudança de resultado no projeto AuctaPay Concilia — regra de matching, tolerância, critério de aprovação, tratamento de divergências ou qualquer número de relatório. Obrigatório sempre que a saída entregue puder mudar (tier 2+).
---

# /change-number — mudança de resultado (AuctaPay Concilia — obrigatório)

Use: qualquer mudança em regra, dado, fórmula, parâmetro, classificação ou indicador entregue (3.7). **Neste projeto isso inclui**: regra de matching, tolerância de R$ 5,00, critério de aprovação automática, tratamento de pagamento órfão (EX-01), classificação do T002 (TRUTH-003) e números de relatórios.

1. **Fonte primeiro**: quem pediu/aprovou, documento, data. Sem fonte → parar e obter.
2. **Issue "Mudança de resultado"** (template do repo, label `muda-numero` + `risco-N`) com before/after esperado e os casos que NÃO devem mudar.
3. **Plano Visual Faseado (OBRIGATÓRIO antes de implementar)** — `docs/planos/<mudanca>.md`: fases com nome de negócio, **esquema mermaid** do cálculo antes → depois (onde exatamente o número muda), o que NÃO muda, o que o consultor verá por fase. Aprovação do consultor antes de implementar.
4. **Parâmetro rastreável** (3.8): nome canônico, valor, unidade, fonte, data de referência, escopo, owner, status. A tolerância de R$ 5,00 herdada do legado é número mágico sem fonte (EX-04) — ao ser tocada, precisa ganhar todos esses atributos.
5. **Golden cases ANTES da mudança**: rodar `tests/regression/baseline_check.py` e guardar as saídas. Tolerância vigente = **R$ 0,00 / igualdade exata** (baseline determinística); qualquer tolerância diferente é proposta pelo agente e **aprovada explicitamente por Rafael Costa** — nunca adotada em silêncio.
6. **Classificação da regra antes de alterar**: declarar se o comportamento afetado é *observado*, *regra confirmada*, *hipótese* ou *defeito conhecido* (GLOSSARY). Promover "observado" a "confirmada" ou "defeito" é decisão de Rafael Costa, registrada na Issue e nas TRUTHS.
7. **Critério novo = modo opcional com `default = vigente`**: a v1 replica o legado fielmente (TRUTH-004). Um critério corrigido entra selecionável (ex.: `--criterio {legado|revisado}`), com TRUTH própria; adoção pelo cliente é release à parte.
8. **Implementar e medir**: golden na versão nova → before/after, magnitude, cenários afetados. **Re-verificar o critério vigente no mesmo ciclo** (prova de conservação) em qualquer refactor do motor.
9. **Impacto + regressão completa**; TRUTHS afetadas atualizadas no MESMO PR (D5).
10. **Aprovação de negócio**: Rafael Costa aprova o before/after ANTES do merge (comentário de aprovação no PR — TRUTH-009). Tier 3 (se envolver integração/persistência): segundo revisor + SI.
11. → `/pre-pr` (as três camadas D4 confirmam a classificação por medição).
