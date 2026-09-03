---
name: handoff
description: Transfere o estado do projeto AuctaPay Concilia entre pessoas ou sessões, gerando o resumo a partir dos artefatos versionados e publicando na Issue/PR. Use ao encerrar sessão longa ou passar o trabalho adiante.
---

# /handoff — troca de pessoa ou sessão (AuctaPay Concilia)

O handoff é **gerado dos artefatos** — não os substitui (6.4). Critério de sucesso: a próxima sessão continua só com repo + artefatos, sem ler o chat anterior.

1. **Verdades materiais primeiro**: mini-check D5 — algo desta sessão muda `TRUTHS.md` / `PROJECT.md` / `.project/init-state.md`? Atualizar por PR antes do handoff.
2. **Registrar** mudanças e decisões materiais no PR/Issue; testes executados e evidências guardadas (ritual de fechamento 3.5).
3. **Resumo de handoff** (6.4): objetivo da mudança · estado do branch · o que já foi feito · testes e evidências · decisões tomadas · blockers (com o que cada um bloqueia) · próximo passo · arquivos e fontes a consultar. Publicar na Issue/PR — **não só no chat**. [skill: handoff]
4. **Estado do branch/PR explícito**: o que está commitado, o que falta, situação do CI.
5. **Neste projeto, sempre reafirmar no handoff**: `legacy/` é read-only; reutilização do legado suspensa (TRUTH-005); gates abertos (sandbox da API, Entra ID, arquitetura Azure, validação do dono do número).
