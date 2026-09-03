# Project truths

> Verdades canônicas para a **versão atual** do projeto (blueprint 6.2). Cada item é atômico, verificável e relevante para decisões futuras. Hipóteses, pendências, opiniões e logs NÃO entram. Quando a realidade muda, a verdade é alterada por PR — o Git preserva o histórico.

TRUTH-001 │ Regra de matching OBSERVADA no legado: pagamento com mesmo `documento` e diferença de valor ≤ R$ 5,00 é aprovado automaticamente; sem candidato, o título fica OPEN. Status de evidência: comportamento observado — NÃO é regra aprovada.
Source: reconcile.py (legado) + baseline/baseline_expected.json
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-002 │ A baseline do legado é reproduzível: sobre a massa sintética, produz T001=APPROVED/P001, T002=APPROVED/P002, T003=OPEN — verificado por execução independente em ambiente limpo, apenas Python padrão.
Source: baseline/baseline_expected.json + execução de 2026-09-03 (registrada no init-state)
Owner: Aucta (Caio Ferrari)
Last reviewed: 2026-09-03

TRUTH-003 │ O caso T002 (diferença de R$ 4,00, pago após o vencimento) é aprovado pelo legado — preservar na baseline como evidência de caracterização; classificado como DEFEITO CANDIDATO, não regra.
Source: known_concern em baseline/baseline_expected.json
Owner: Rafael Costa (Controladoria)
Last reviewed: 2026-09-03

TRUTH-004 │ A v1 replica fielmente as regras de matching observadas; qualquer mudança de regra passa pelo workflow /change-number com aprovação do dono do número.
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

TRUTH-007 │ Login corporativo da nova solução = Microsoft Entra ID, com perfis Financeiro, Cobrança e Auditoria.
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
