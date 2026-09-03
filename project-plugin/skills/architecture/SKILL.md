---
name: architecture
description: Conduz mudança estrutural no projeto AuctaPay Concilia — autenticação Entra ID, perfis de acesso, banco PostgreSQL, integração com ERP, API do provedor, webhooks, deploy em Azure ou migração. Use para qualquer decisão tier 3.
---

# /architecture — mudança estrutural (AuctaPay Concilia — tier 3)

Use: arquitetura, segurança, autenticação, perfis, persistência, integrações centrais, deploy, migração. Este projeto é tier 3 por natureza — este workflow é frequente, não excepcional.

1. **Modelagem e alternativas**: comparar opções em linguagem de negócio (benefício, risco, manutenção, desempenho, complexidade) com recomendação explícita (3.1). [skills: domain-modeling / codebase-design / improve-codebase-architecture]
2. **Plano técnico + threat model** (obrigatório quando envolve autenticação, perfis, dados pessoais ou exposição externa): trust boundaries, secrets, validação de entrada, assinatura de webhook, autorização por perfil. [skill: security-and-hardening]
3. **ADR** para a decisão durável em `docs/architecture/`: contexto, opções, decisão, consequências (3.4). [skill: documentation-and-adrs]
4. **Gates deste projeto — verificar ANTES de projetar em detalhe:**
   - Integração com a API do provedor: bloqueada (sem credenciais de sandbox e spec incompleta — auth, assinatura, paginação, erros).
   - SSO/perfis: bloqueado (sem configuração do Entra ID).
   - Deploy homolog/prod: bloqueado até **aprovação formal da arquitetura Azure** (TRUTH-012); backup operacional depende de RPO/RTO aprovados (TRUTH-013).
   Nesses casos: projetar o que é possível sem a dependência, registrar o que falta e parar no gate — nunca inventar credencial, contrato de API ou política de acesso.
5. **Fronteira do legado**: nenhuma dependência de `legacy/` entra na arquitetura nova até liberação de IP/licenças (TRUTH-005); o `legacy-match-sdk` não tem licença nem fonte e está fora de qualquer desenho.
6. **Implementação incremental** com rollback planejado.
7. **Segundo revisor** obrigatório (tier 3) + Segurança da Informação quando toca autenticação, dados pessoais ou exposição.
8. → `/pre-pr`.
