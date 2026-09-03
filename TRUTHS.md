# Project truths

> Verdades canônicas para a **versão atual** do projeto (blueprint 6.2). Cada item é atômico, verificável e relevante para decisões futuras. Hipóteses, pendências, opiniões e logs NÃO entram. Quando a realidade muda, a verdade é alterada por PR — o Git preserva o histórico.
>
> **Convenção de evidência (GLOSSARY):** *comportamento observado* = o que a `baseline-v0` faz, comprovado por execução, sem juízo de correção · *regra confirmada* = validada por Rafael Costa como regra da nova solução · *hipótese* = interpretação não confirmada · *defeito conhecido* = observado e classificado como incorreto pelo dono do número. Nenhum comportamento observado vira regra da nova solução sem decisão registrada (marco M3).

TRUTH-001 │ Regra de matching OBSERVADA na `baseline-v0`: pagamento com mesmo `documento` e diferença de valor ≤ R$ 5,00 é aprovado automaticamente; sem candidato, o título fica OPEN. Status de evidência: **comportamento observado** — NÃO é regra aprovada da nova solução.
Source: legacy/reconcile.py @ tag baseline-v0 + legacy/baseline/baseline_expected.json
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-002 │ A baseline do legado é reproduzível: sobre a massa sintética, produz T001=APPROVED/P001, T002=APPROVED/P002, T003=OPEN — verificado por execução independente em ambiente limpo, apenas Python padrão. Estado congelado na tag `baseline-v0` (commit 6895c92).
Source: legacy/baseline/baseline_expected.json (`evidence_status: observed_not_approved`) + execução de 2026-09-03 e harness tests/regression/baseline_check.py
Owner: Aucta (Caio Ferrari)
Last reviewed: 2026-09-03

TRUTH-003 │ O caso T002 (diferença de R$ 4,00, pago após o vencimento) é aprovado automaticamente pela `baseline-v0`. Status de evidência: **comportamento observado**, preservado como evidência de caracterização; classificado como **defeito candidato** (hipótese de defeito). NÃO é regra aprovada — a classificação definitiva (regra confirmada × defeito conhecido) é decisão de Rafael Costa no marco M3.
Source: known_concern em legacy/baseline/baseline_expected.json + tests/fixtures/golden_cases.csv (GC-02)
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-004 │ A v1 replica fielmente as regras de matching observadas, DEPOIS de aprovadas em M3; qualquer mudança de regra passa pelo workflow /change-number com aprovação do dono do número.
Source: decisão do consultor, 2026-09-03
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-005 │ Reutilização de código e dependências do legado NÃO está autorizada: titularidade não confirmada, contrato do fornecedor não localizado, redistribuição não autorizada.
Source: LICENSE_STATUS.md (legado) + decisão do consultor, 2026-09-03
Owner: Mariana Torres (CFO)
Last reviewed: 2026-09-03

TRUTH-006 │ `legacy-match-sdk`, `requests` e `fuzzywuzzy` constam em requirements.txt mas NÃO são importados por nenhum módulo do legado; a baseline não depende deles.
Source: inspeção do código, 2026-09-03
Owner: Aucta (Caio Ferrari)
Last reviewed: 2026-09-03

TRUTH-007 │ Login corporativo da nova solução = Microsoft Entra ID, com perfis Financeiro, Cobrança e Auditoria. A matriz de permissões por perfil (RBAC) ainda não existe — gate do marco M8.
Source: .env.example (legado) + confirmação do consultor, 2026-09-03
Owner: Segurança da Informação (AuctaPay)
Last reviewed: 2026-09-03

TRUTH-008 │ Dado real de cliente NUNCA entra no Git; homologação usa somente dados mascarados/sintéticos.
Source: decisão do consultor, 2026-09-03
Owner: Segurança da Informação (AuctaPay)
Last reviewed: 2026-09-03

TRUTH-009 │ Entrada em produção exige aprovação conjunta de Rafael Costa e Segurança da Informação; o aceite de cada entrega é formalizado por comentário de aprovação no PR.
Source: decisão do consultor, 2026-09-03
Owner: Mariana Torres (CFO)
Last reviewed: 2026-09-03

TRUTH-010 │ Fontes oficiais do projeto: pasta OneDrive `Aucta Blueprint Dev AI/inputs/teste 3` e o repositório `AuctaFerrari/aucta-teste-3-auctapay`, exclusivamente.
Source: declaração do consultor, 2026-09-03
Owner: Caio Ferrari (Aucta)
Last reviewed: 2026-09-03

TRUTH-011 │ A massa de dados do ZIP do legado é 100% sintética e não contém credenciais válidas.
Source: README.md do ZIP + declaração do consultor, 2026-09-03
Owner: Caio Ferrari (Aucta)
Last reviewed: 2026-09-03

TRUTH-012 │ Infra alvo de homologação e produção: nuvem Azure da AuctaPay, CONDICIONADA a aprovação formal de arquitetura antes do primeiro deploy.
Source: decisão do consultor, 2026-09-03
Owner: Segurança da Informação (AuctaPay)
Last reviewed: 2026-09-03

TRUTH-013 │ A pasta `backups/` no OneDrive do projeto preserva pacotes e evidências por release; NÃO substitui o backup operacional da aplicação e do PostgreSQL, cuja estratégia depende de RPO/RTO aprovados com a arquitetura.
Source: decisão do consultor, 2026-09-03
Owner: Mariana Torres (CFO)
Last reviewed: 2026-09-03

TRUTH-014 │ Se o histórico do repositório original do fornecedor for recebido, ele deve passar por saneamento de segredos ANTES de qualquer importação (houve token de homologação no histórico, já revogado); Segurança da Informação deve ser acionada.
Source: docs/production_notes.txt (legado)
Owner: Segurança da Informação (AuctaPay)
Last reviewed: 2026-09-03

TRUTH-015 │ A `baseline-v0` IGNORA silenciosamente pagamentos sem título correspondente (ex.: P003, documento NF-9999): eles não aparecem em nenhuma saída. Status de evidência: **comportamento observado**, NÃO regra aprovada. Tratamento proposto para a nova solução — pagamento órfão como divergência visível (EX-01) — é hipótese a ratificar por Rafael Costa em M3.
Source: recomputação independente de 2026-09-03 + tests/fixtures/expected_exceptions.csv
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-016 │ Sequência obrigatória do projeto: **caracterizar (M2) → aprovar funcionalmente (M3) → especificar (M4) → reescrever (M5)**. Especificação e reescrita do motor não começam antes da aprovação de regras, golden cases, exceções e tolerâncias pelo dono do número.
Source: decisão do consultor, 2026-09-03 (correção de consistência)
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03
