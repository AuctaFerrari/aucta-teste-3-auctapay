---
name: build-feature
description: Implementa feature material (tier 1+) no projeto AuctaPay Concilia com spec curta, Plano Visual Faseado aprovado antes de implementar, e implementação incremental com testes. Use para mudanças funcionais que não alteram números entregues.
---

# /build-feature — feature material (AuctaPay Concilia)

1. **Requisitos**: fechar lacunas com perguntas curtas (1 decisão por pergunta, contexto em ≤4 bullets antes). [skills: grill-with-docs / interview-me — core]
2. **Spec curta**: comportamento + critérios de aceite, ligados a um ACC do ACCEPTANCE.md. [skill: to-spec / spec-driven-development]
3. **Plano Visual Faseado (OBRIGATÓRIO antes de implementar)** — `docs/planos/<feature>.md`, pt-BR de negócio: (a) fases com nome de negócio ("Fase 1 — leitura dos títulos do ERP"); (b) **esquema mermaid** do fluxo antes → depois; (c) o que muda e o que NÃO muda; (d) o que o consultor verá ao fim de cada fase. Aprovação do consultor ANTES de qualquer código. [skill: planning-and-task-breakdown]
4. **Implementação incremental** com TDD onde há lógica/regra, anunciando `Etapa N de X — <nome da fase>`. Uma mudança lógica por branch/PR; commits atômicos. [skills: tdd / test-driven-development]
5. **Fronteira do legado**: nada é copiado de `legacy/` (TRUTH-005) — a nova solução é escrita de forma limpa; `legacy/` serve só como referência de comportamento.
6. **QA**: fluxo exercitado + evidências; exceções esperadas relevantes (EX-01..05) cobertas.
7. → `/pre-pr`.
