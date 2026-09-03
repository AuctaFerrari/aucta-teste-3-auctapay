# Regras inegociáveis — AuctaPay Concilia

Extraídas de PROJECT.md e TRUTHS.md. Valem para toda sessão e todo workflow.

1. **Fontes oficiais, exclusivamente**: pasta OneDrive `Aucta Blueprint Dev AI/inputs/teste 3` e este repositório (TRUTH-010). O agente não usa nem altera nada fora disso.
2. **Dado real de cliente NUNCA entra no Git** (CNPJ, nome, e-mail, telefone, valores, observações de cobrança). Desenvolvimento e homologação usam massa mascarada/sintética (TRUTH-008); fixtures em `tests/fixtures/`.
3. **`legacy/` é snapshot read-only de caracterização.** Sem refactor, sem correção, sem reuso de código ou dependências — titularidade e licenças não verificadas; redistribuição proibida (TRUTH-005). O `legacy-match-sdk` não tem licença nem fonte.
4. **Comportamento observado ≠ regra aprovada.** A baseline preserva o legado inclusive nos defeitos. Toda regra carrega classificação: observado / confirmada / hipótese / defeito conhecido. Promover classificação é decisão de Rafael Costa.
5. **A v1 replica o matching fielmente** (TRUTH-004). Correção de regra = `/change-number` com fonte, before/after e aprovação; critério novo entra como modo opcional com `default = vigente`.
6. **Aprovações**: mudança de número → Rafael Costa (comentário de aprovação no PR). Produção → Rafael Costa **e** Segurança da Informação (TRUTH-009). Tier 3 → segundo revisor.
7. **Gates que param o trabalho** (nunca improvisar): sem credenciais do sandbox e spec completa → não implementar integração com o provedor; sem configuração do Entra ID → não implementar SSO/perfis; sem aprovação formal da arquitetura Azure → não fazer deploy (TRUTH-012).
8. **Segredos** ficam em cofre ou variáveis de ambiente, nunca no código ou em documento. Se o histórico do repositório do fornecedor for recebido, sanear antes de importar e acionar a SI (TRUTH-014).
9. **O consultor nunca digita comandos Git** (D6): branch, commit, push, PR e merge são executados pelo agente.
10. **Diálogo em pt-BR de negócio**, com conceitos técnicos traduzidos, abertura didática por etapa, progresso `Etapa N de X` e uma decisão por pergunta.
