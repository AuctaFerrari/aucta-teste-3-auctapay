# Manifesto de vendorização — AuctaPay Concilia (decisão D3, refinada no Teste 1)

Este projeto **NÃO duplica** skills de terceiros. O manifesto aponta para as cópias auditadas no núcleo `AuctaFerrari/aucta-dev-core` (diretório `vendored/`), cuja auditoria completa — origem upstream, blob SHA por arquivo, data e responsável — vive em `aucta-dev-core/vendored/MANIFEST.md`.

**Núcleo referenciado:** `AuctaFerrari/aucta-dev-core` @ commit `007a7d3` (v0.3.0, 2026-09-03).
**Responsável pela seleção:** Caio Ferrari (Aucta) · **Data:** 2026-09-03.

A operação NUNCA depende de upstream vivo: se o repositório de terceiro mudar ou desaparecer, os workflows continuam rodando sobre as cópias do núcleo. O drift check sinaliza divergência ("upstream alterado — auditar e atualizar?") **sem bloquear nada**.

## Como esta pilha é usada — capacidades sob demanda, nunca carregadas juntas

As 19 entradas abaixo são um **catálogo de capacidades disponíveis**, não um conjunto carregado a cada sessão. O carregamento é progressivo (blueprint 6.5 / 7.4):

1. A sessão abre lendo apenas `PROJECT.md` + `TRUTHS.md` + a Issue/Spec ativa.
2. O **router** (`project-plugin/skills/router/SKILL.md`) classifica a demanda (tipo + tier) e escolhe **um** workflow.
3. O workflow escolhido invoca **somente as skills citadas nos seus próprios passos** — tipicamente 2 a 4 — no momento em que o passo executa.
4. Nada mais é lido. Uma demanda tier 0 (rótulo de tela) não carrega `security-and-hardening`; um `/change-number` não carrega `codebase-design`.

Exemplos de carga real por demanda:

| Demanda | Workflow | Skills efetivamente invocadas |
| --- | --- | --- |
| Ajustar rótulo de tela (tier 0) | caminho leve + `/pre-pr` | `code-review` |
| Caracterizar regras do legado (M2) | `/start-work` → análise documental | `context-engineering`, `grill-with-docs` |
| Alterar tolerância de matching (tier 2) | `/change-number` → `/pre-pr` | `to-spec`, `planning-and-task-breakdown`, `test-driven-development`, `code-review` |
| Desenhar autenticação Entra ID (tier 3) | `/architecture` → `/pre-pr` | `domain-modeling`, `security-and-hardening`, `documentation-and-adrs` |

Anti-padrão explícito (blueprint 8.1): empilhar skills redundantes ou carregar a pilha inteira "por garantia". `using-agent-skills` existe justamente para evitar isso.

## Catálogo de capacidades (tier 3 · web · integrações · números entregues)

| Skill | Caminho no núcleo | Origem upstream | Justificativa (uma linha) | Entra em |
| --- | --- | --- | --- | --- |
| using-agent-skills | `vendored/using-agent-skills` | addyosmani/agent-skills @ `d2c37ef` | Escolhe a capacidade adequada e evita empilhar skills redundantes. | router |
| context-engineering | `vendored/context-engineering` | addyosmani/agent-skills @ `d2c37ef` | Mantém contexto mínimo suficiente num projeto com 16 verdades e 7 fontes. | /start-work |
| interview-me | `vendored/interview-me` | addyosmani/agent-skills @ `d2c37ef` | Fecha lacunas de pedidos subespecificados — regras do legado ainda são parcialmente hipótese. | /build-feature |
| grill-with-docs | `vendored/grill-with-docs` | mattpocock/skills @ `6654f6b` | Refina requisitos junto à documentação parcial do provedor e do legado. | /build-feature, M2 |
| to-spec | `vendored/to-spec` | mattpocock/skills @ `6654f6b` | Especificação curta por mudança delimitada, ligada aos ACC. | /build-feature, /change-number |
| spec-driven-development | `vendored/spec-driven-development` | addyosmani/agent-skills @ `d2c37ef` | Transforma mudança material em comportamento + critérios testáveis. | /build-feature |
| planning-and-task-breakdown | `vendored/planning-and-task-breakdown` | addyosmani/agent-skills @ `d2c37ef` | Quebra a modernização em fases pequenas e verificáveis (Plano Visual Faseado). | /build-feature, /change-number |
| test-driven-development | `vendored/test-driven-development` | addyosmani/agent-skills @ `d2c37ef` | Proteção de regressão para o motor de matching replicado. | /build-feature, /change-number |
| tdd | `vendored/tdd` | mattpocock/skills @ `6654f6b` | Disciplina de TDD aplicada a regras e golden cases. | /build-feature |
| diagnosing-bugs | `vendored/diagnosing-bugs` | mattpocock/skills @ `6654f6b` | Investiga divergência numérica antes de editar (baseline × motor novo). | /fix-bug |
| debugging-and-error-recovery | `vendored/debugging-and-error-recovery` | addyosmani/agent-skills @ `d2c37ef` | Reproduz, isola causa-raiz e impede recorrência em integrações instáveis. | /fix-bug |
| security-and-hardening | `vendored/security-and-hardening` | addyosmani/agent-skills @ `d2c37ef` | Obrigatória no tier 3: SSO, RBAC, PII, assinatura de webhook, secrets. | /architecture |
| domain-modeling | `vendored/domain-modeling` | mattpocock/skills @ `6654f6b` | Modela título × pagamento × divergência antes de decidir persistência. | /architecture |
| codebase-design | `vendored/codebase-design` | mattpocock/skills @ `6654f6b` | Desenho de módulos e interfaces da reescrita limpa (sem herdar o legado). | /architecture (M4/M5) |
| improve-codebase-architecture | `vendored/improve-codebase-architecture` | mattpocock/skills @ `6654f6b` | Revisão estrutural quando a mudança justificar intervenção de arquitetura. | /architecture |
| documentation-and-adrs | `vendored/documentation-and-adrs` | addyosmani/agent-skills @ `d2c37ef` | ADRs das decisões duráveis (autenticação, banco, integração). | /architecture |
| git-workflow-and-versioning | `vendored/git-workflow-and-versioning` | addyosmani/agent-skills @ `d2c37ef` | Branch/commit/PR/tag coerentes — executados pelo agente (D6). | /start-work, /pre-pr, /release |
| code-review | `vendored/code-review` | mattpocock/skills @ `6654f6b` | Review de diff no /pre-pr em dois eixos (padrões e spec). | /pre-pr |
| handoff | `vendored/handoff` | mattpocock/skills @ `6654f6b` | Transferência de estado entre sessões sem depender do chat. | /handoff |

## Pendentes de vendorização (tranche 4 do núcleo)

| Skill | Uso previsto | Fallback documentado enquanto não vendorizada |
| --- | --- | --- |
| frontend-design | Implementação das telas (Financeiro/Cobrança/Auditoria) | `/ui-change` aplica os princípios manualmente e registra as escolhas no PR |
| impeccable | Acabamento visual quando a qualidade estiver no aceite | idem |
| andrej-karpathy-skills | Camada de comportamento (simplicidade, mudanças cirúrgicas) | Princípios embutidos nos workflows (uma mudança lógica por PR, critérios verificáveis) |

Skills de UI entram na pilha quando o marco de telas começar — pedido ao núcleo, nunca cópia local.

## Drift check

Executado pelo init-check ou sob demanda, contra o `MANIFEST.md` do núcleo: compara o blob SHA de cada arquivo vendorizado com o upstream em HEAD. Upstream alterado → sinaliza para auditoria; **operação continua** sobre a cópia do núcleo. Upstream inacessível → só relata. **Drift de PATH ≠ drift de conteúdo**: o núcleo já registra a reorganização de pastas do mattpocock (blobs idênticos em caminhos novos).

Última execução: 2026-09-03 (init-check, P11) — 4 skills conferidas por amostragem; `security-and-hardening` com upstream alterado (`c00236e` → `cf093e9`), sinalizada para auditoria no núcleo, sem bloqueio.
