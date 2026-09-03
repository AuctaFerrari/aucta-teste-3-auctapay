---
name: start-work
description: Abre qualquer mudança no projeto AuctaPay Concilia — carrega contexto mínimo, classifica tier e Muda-numero, cria Issue e branch e registra o plano de validação. Use ao iniciar qualquer demanda antes de implementar.
---

# /start-work — abrir qualquer mudança (AuctaPay Concilia)

Always the first workflow of a demand. All Git by the agent (D6).

1. **Contexto mínimo** (6.5): `PROJECT.md`, `TRUTHS.md` e a Issue/Spec ativa. Nada além disso por padrão. [skill: context-engineering — vendorizada no core]
2. **Classificar**: tier (0–3) + provável Muda-numero, aplicando as **sentinelas do router** (reconcile, tolerância R$ 5,00, critério de aprovação, órfãos, golden/exceptions, harness). Tier de partida deste projeto = 3 para qualquer coisa que toque autenticação, integrações ou persistência.
3. **Issue** pelo template do repo: resultado desejado, critérios de aceite, tier, Muda-numero, labels (`risco-N`, `muda-numero` quando aplicável). [agente]
4. **Branch** `feat|fix|refactor|docs/<tema>` a partir da main. [agente — consultor nunca digita Git]
5. **Plano de validação** proporcional ao tier: quais golden cases rodam, quais exceções (EX-01..05) devem ser exercitadas, rollback quando aplicável. Tier ≥ 2: capturar baseline ANTES da mudança.
6. **Ritual de abertura** (3.5): confirmar branch, working tree limpo e que o harness `tests/regression/baseline_check.py` está verde no ponto de partida.

Gate de saída: Issue criada, branch criada, plano de validação registrado na Issue.
