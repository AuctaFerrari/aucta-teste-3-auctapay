---
name: release
description: Publica versão entregue do projeto AuctaPay Concilia — validação prévia, release notes com impacto numérico quantificado, tag, manifest com checksum, arquivo corporativo e backup do repositório. Use quando uma versão for entregue a homologação ou produção.
---

# /release — versão entregue (AuctaPay Concilia)

Release = estado identificado do repositório, reproduzível (blueprint 5). **Gate ativo: deploy em homologação/produção exige aprovação formal da arquitetura Azure (TRUTH-012) e aprovação conjunta Rafael Costa + Segurança da Informação (TRUTH-009).**

1. **Validação prévia** (5.1): features novas, regressão, integrações, fluxos por perfil, golden cases, comparação com a versão anterior. **Entregável = configuração validada**: os artefatos saem da MESMA configuração e parâmetros usados na validação golden — nunca de um caminho paralelo (lição do Teste 1).
2. **Docs e mapas** refletem a versão (5.2); higienização (5.5): sem temporários, versão vigente identificada.
3. **Release notes** (5.3): versão, mudanças, bugs corrigidos, limitações conhecidas, testes executados, cuidados de uso. **Muda-numero quantificado** (5.4): regra/parâmetro, before/after, magnitude, segmentos/períodos afetados, aprovação — nunca descrito como "melhoria técnica".
4. **Tag + GitHub Release** com o artefato. [agente quando o ambiente permite; senão click-path na UI]
5. **Manifest** (9.7): tag, commit, data, owner, checksum SHA-256 do artefato.
6. **Arquivo corporativo** (9.6): pasta de releases na pasta oficial do projeto com artefato, release notes, manifest, resumo de testes e aprovações. [assistido — conector M365 é leitura; consultor faz upload, agente valida por busca]
7. **Backup do repositório** — independência do GitHub: snapshot ZIP do repo na tag em `backups/<tag>.zip` na pasta do projeto no OneDrive. Click-path: página do repo na tag → **Code → Download ZIP** → salvar em `backups/`. **Não substitui** o backup operacional da aplicação e do PostgreSQL, que depende de RPO/RTO aprovados (TRUTH-013).
8. **CHANGELOG + VERSION** atualizados. [agente]
9. **Segurança antes de publicar**: confirmar que nenhum segredo, credencial ou dado real entrou no pacote; se o histórico do fornecedor tiver sido importado, confirmar saneamento (TRUTH-014).
