---
name: ui-change
description: Conduz mudança de interface no projeto AuctaPay Concilia (telas de conciliação, fila de divergências, aprovação de matches, relatórios), com direção visual única, teste de navegador e acessibilidade. Use para qualquer alteração visual ou de usabilidade.
---

# /ui-change — mudança de interface (AuctaPay Concilia)

Uma direção principal de design; um segundo gate só se o risco justificar (blueprint 8.4). Não combinar várias suítes de design sem razão explícita.

1. **Plano de design**: o que muda na tela, para qual perfil (Financeiro / Cobrança / Auditoria) e qual tarefa fica mais fácil. Perfis diferentes veem funções diferentes — mudança que altere o que um perfil ENXERGA é questão de autorização (tier 3), não de UI.
2. **Direção visual**: `frontend-design` como implementação padrão; `impeccable` para acabamento quando a qualidade visual estiver no aceite. *(Pendentes de vendorização — tranche 4 do core; até então, aplicar os princípios manualmente e registrar as escolhas no PR.)*
3. **Plano Visual Faseado** quando a mudança for material (mesma regra do /build-feature).
4. **Nada de número na UI sem gate**: se a tela passar a exibir valor, indicador ou classificação novos ou diferentes, o caminho é `/change-number` em paralelo.
5. **Teste de navegador** dos fluxos afetados + estados (vazio, erro, carregando) e acessibilidade básica (foco, contraste, rótulos).
6. **Evidência**: screenshots antes/depois no PR.
7. → `/pre-pr`.
