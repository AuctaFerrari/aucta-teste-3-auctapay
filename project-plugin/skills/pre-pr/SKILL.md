---
name: pre-pr
description: Gate obrigatório antes de abrir ou atualizar qualquer PR no projeto AuctaPay Concilia — testes, QA, verificação Muda-numero em três camadas, check de TRUTHS, sincronização de documentação e abertura do PR pelo agente. Use sempre antes do PR.
---

# /pre-pr — gate antes de abrir/atualizar PR (AuctaPay Concilia — sempre)

All Git/PR mechanics by the agent (D6).

1. **Testes**: suite do tier verde; `tests/regression/baseline_check.py` verde; evidências coletadas.
2. **QA**: fluxo crítico exercitado; artefatos gerados regenerados pela origem, nunca editados à mão (3.9).
3. **Review preparatório do diff**: simplicidade, ausência de refactor lateral; dividir o PR se houver objetivos independentes. Confirmar que `legacy/` não sofreu alteração indevida. [skill: code-review]
4. **Muda-numero — três camadas (D4), nunca só declaração:**
   - a) *Caminho*: o diff tocou alguma sentinela do router (reconcile / tolerância / critério / órfãos / golden / exceptions / harness, ou módulo novo de matching, parâmetros, relatórios)? → pergunta obrigatória, sem opção de pular.
   - b) *Conteúdo*: o diff altera constantes numéricas, comparações de valor, datas de corte ou fórmulas? → idem.
   - c) *Golden before/after*: rodar o harness na base e no head. Qualquer saída diferente → Muda-numero é **fato medido** → exigir os artefatos do `/change-number` (fonte, before/after, magnitude, aprovação de Rafael Costa).
5. **Check de TRUTHS (D5)**: comparar diff + contexto da sessão com `TRUTHS.md` → duas listas: (a) verdades contraditas ou alteradas; (b) fatos novos que parecem canônicos (ex.: comportamento do legado recém-descoberto). Confirmar com o consultor; atualização entra no MESMO PR. **A IA detecta; o consultor decide.**
6. **Docs sync** (3.11): PROJECT / ACCEPTANCE / DATA_CATALOG / ADRs que ficariam incorretos são atualizados no mesmo ciclo.
7. **Risk gate**: tier 2 → aprovação de Rafael Costa registrada; tier 3 → segundo revisor (+ SI quando toca autenticação, dados pessoais ou exposição); produção → Rafael + SI (TRUTH-009).
8. **PR**: abrir/atualizar com o template preenchido (contexto, o que mudou, por quê, Muda-numero, risco, validação, release) e labels corretas. [agente]
