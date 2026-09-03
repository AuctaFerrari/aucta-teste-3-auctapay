---
name: fix-bug
description: Diagnostica e corrige erro reproduzível ou regressão no projeto AuctaPay Concilia, investigando o sintoma antes de editar e criando teste de regressão que falha primeiro. Use quando há comportamento inesperado observável.
---

# /fix-bug — erro reproduzível ou regressão (AuctaPay Concilia)

Investigar o sintoma antes de editar (blueprint 4). Plausibilidade não é causa-raiz.

1. **Triagem pelo sintoma** (4.1): o que mudou no resultado, o esperado, em quais casos ocorre, desde quando, blocos suspeitos, qual teste discrimina as hipóteses. [skill: diagnosing-bugs / debugging-and-error-recovery]
2. **Reproduzir e medir**. Anomalia numérica → evidência mínima (4.3): valor observado, esperado, diferença, caso, versão, passos. Rótulos: medido / inferido / não verificado (4.2).
3. **Teste de regressão que FALHA** antes do fix. Erro numérico relevante → reconstruir 1 caso por caminho independente (4.4), como feito na conferência da baseline.
4. **Fix na causa-raiz**; artefatos gerados (relatórios, exports) nunca corrigidos à mão — corrige-se a origem e regenera (3.9).
5. **QA**: regressão verde + golden cases e casos vizinhos que NÃO deviam mudar.
6. **Atenção**: se o bug estiver na regra de conciliação, o caminho é `/change-number`, não este — mudança de número exige fonte e aprovação de Rafael Costa.
7. → `/pre-pr`.
