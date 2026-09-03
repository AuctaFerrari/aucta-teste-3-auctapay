# Manifesto de vendorização — AuctaPay Concilia (decisão D3, refinada no Teste 1)

Este projeto **NÃO duplica** skills de terceiros. O manifesto aponta para as cópias auditadas no núcleo `AuctaFerrari/aucta-dev-core` (diretório `vendored/`), cuja auditoria completa — origem upstream, blob SHA por arquivo, data e responsável — vive em `aucta-dev-core/vendored/MANIFEST.md`.

**Núcleo referenciado:** `AuctaFerrari/aucta-dev-core` @ commit `007a7d3` (v0.3.0, 2026-09-03).
**Responsável pela seleção:** Caio Ferrari (Aucta) · **Data:** 2026-09-03.

A operação NUNCA depende de upstream vivo: se o repositório de terceiro mudar ou desaparecer, os workflows continuam rodando sobre as cópias do núcleo. O drift check sinaliza divergência ("upstream alterado — auditar e atualizar?") **sem bloquear nada**.

## Pilha selecionada (tier 3 · web · integrações · números entregues)

| Skill | Caminho no núcleo | Origem upstream | Justificativa (uma linha) |
| --- | --- | --- | --- |
| using-agent-skills | `vendored/using-agent-skills` | addyosmani/agent-skills @ `d2c37ef` | Escolhe a capacidade adequada e evita empilhar skills redundantes. |
| context-engineering | `vendored/context-engineering` | addyosmani/agent-skills @ `d2c37ef` | Mantém contexto mínimo suficiente num projeto com 15 verdades e 7 fontes. |
| interview-me | `vendored/interview-me` | addyosmani/agent-skills @ `d2c37ef` | Fecha lacunas de pedidos subespecificados — regras do legado ainda são parcialmente hipótese. |
| grill-with-docs | `vendored/grill-with-docs` | mattpocock/skills @ `6654f6b` | Refina requisitos junto à documentação parcial do provedor e do legado. |
| to-spec | `vendored/to-spec` | mattpocock/skills @ `6654f6b` | Especificação curta por mudança delimitada, ligada aos ACC. |
| spec-driven-development | `vendored/spec-driven-development` | addyosmani/agent-skills @ `d2c37ef` | Transforma mudança material em comportamento + critérios testáveis. |
| planning-and-task-breakdown | `vendored/planning-and-task-breakdown` | addyosmani/agent-skills @ `d2c37ef` | Quebra a modernização em fases pequenas e verificáveis (Plano Visual Faseado). |
| test-driven-development | `vendored/test-driven-development` | addyosmani/agent-skills @ `d2c37ef` | Proteção de regressão para o motor de matching replicado. |
| tdd | `vendored/tdd` | mattpocock/skills @ `6654f6b` | Disciplina de TDD aplicada a regras e golden cases. |
| diagnosing-bugs | `vendored/diagnosing-bugs` | mattpocock/skills @ `6654f6b` | Investiga divergência numérica antes de editar (baseline × motor novo). |
| debugging-and-error-recovery | `vendored/debugging-and-error-recovery` | addyosmani/agent-skills @ `d2c37ef` | Reproduz, isola causa-raiz e impede recorrência em integrações instáveis. |
| security-and-hardening | `vendored/security-and-hardening` | addyosmani/agent-skills @ `d2c37ef` | Obrigatória no tier 3: SSO, perfis, PII, assinatura de webhook, secrets. |
| domain-modeling | `vendored/domain-modeling` | mattpocock/skills @ `6654f6b` | Modela título × pagamento × divergência antes de decidir persistência. |
| codebase-design | `vendored/codebase-design` | mattpocock/skills @ `6654f6b` | Desenho de módulos e interfaces da reescrita limpa (sem herdar o legado). |
| improve-codebase-architecture | `vendored/improve-codebase-architecture` | mattpocock/skills @ `6654f6b` | Revisão estrutural quando a mudança justificar intervenção de arquitetura. |
| documentation-and-adrs | `vendored/documentation-and-adrs` | addyosmani/agent-skills @ `d2c37ef` | ADRs das decisões duráveis (autenticação, banco, integração). |
| git-workflow-and-versioning | `vendored/git-workflow-and-versioning` | addyosmani/agent-skills @ `d2c37ef` | Branch/commit/PR/tag coerentes — executados pelo agente (D6). |
| code-review | `vendored/code-review` | mattpocock/skills @ `6654f6b` | Review de diff no /pre-pr em dois eixos (padrões e spec). |
| handoff | `vendored/handoff` | mattpocock/skills @ `6654f6b` | Transferência de estado entre sessões sem depender do chat. |

## Pendentes de vendorização (tranche 4 do núcleo)

| Skill | Uso previsto | Fallback documentado enquanto não vendorizada |
| --- | --- | --- |
| frontend-design | Implementação das telas (Financeiro/Cobrança/Auditoria) | `/ui-change` aplica os princípios manualmente e registra as escolhas no PR |
| impeccable | Acabamento visual quando a qualidade estiver no aceite | idem |
| andrej-karpathy-skills | Camada de comportamento (simplicidade, mudanças cirúrgicas) | Princípios embutidos nos workflows (uma mudança lógica por PR, critérios verificáveis) |

Skills de UI entram na pilha quando o marco de telas começar — pedido ao núcleo, nunca cópia local.

## Drift check

Executado pelo init-check ou sob demanda, contra o `MANIFEST.md` do núcleo: compara o blob SHA de cada arquivo vendorizado com o upstream em HEAD. Upstream alterado → sinaliza para auditoria; **operação continua** sobre a cópia do núcleo. Upstream inacessível → só relata. **Drift de PATH ≠ drift de conteúdo**: o núcleo já registra a reorganização de pastas do mattpocock (blobs idênticos em caminhos novos).
