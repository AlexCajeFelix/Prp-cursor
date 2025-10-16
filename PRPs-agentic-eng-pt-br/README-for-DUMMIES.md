# Comandos PRP para Leigos 🏗️
*Construindo Software Como um Arquiteto Mestre*

## O que é essa Coisa?

Imagine que você quer construir uma casa. Você não pegaria um martelo e começaria a bater na madeira, certo? Você contrataria um arquiteto para desenhar as plantas, um engenheiro estrutural para calcular a fundação, e construtores habilidosos para seguir os projetos.

**O Framework PRP funciona exatamente da mesma forma para construir software.**

Em vez de escrever código aleatoriamente e torcer para que funcione, você usa "trabalhadores de construção especializados em IA" que seguem projetos detalhados para construir suas funcionalidades de software corretamente na primeira tentativa.

---

## A Analogia da Equipe de Construção 🏢

Pense nos comandos PRP como diferentes especialistas em uma empresa de construção:

### **🏗️ O Arquiteto Mestre** (`/prp-planning-create`)
- **O que fazem:** Pegam sua ideia vaga ("Quero uma casa bonita") e criam plantas arquitetônicas detalhadas com projetos, lista de materiais e fases de construção
- **Quando usar:** Quando você tem uma ideia básica mas precisa de planejamento abrangente
- **Exemplo:** "Quero que usuários possam curtir posts" → Especificação completa da funcionalidade com diagramas

### **📋 O Engenheiro Estrutural** (`/api-contract-define`) 
- **O que fazem:** Criam especificações detalhadas de como diferentes partes se conectam (como a fundação se conecta às paredes)
- **Quando usar:** Depois que o arquiteto cria os projetos, quando você precisa que frontend e backend trabalhem juntos
- **Exemplo:** Define exatamente como o "botão de curtir" se comunica com o banco de dados

### **📐 O Arquiteto de Detalhes** (`/prp-base-create`)
- **O que fazem:** Criam manuais de construção incrivelmente detalhados com cada prego, parafuso e medida especificados
- **Quando usar:** Quando você precisa de instruções de implementação abrangentes
- **Exemplo:** Instruções passo-a-passo para construir toda a funcionalidade do botão de curtir

### **🔧 O Especialista em Renovação** (`/prp-spec-create`)
- **O que fazem:** Planejam como mudar edifícios existentes (como converter uma garagem em quarto)
- **Quando usar:** Quando você precisa modificar código existente em vez de construir algo novo
- **Exemplo:** Mudando de autenticação simples para OAuth2

### **✅ O Encarregado do Projeto** (`/prp-task-create`)
- **O que fazem:** Criam ordens de trabalho diárias focadas com verificações de qualidade
- **Quando usar:** Para tarefas pequenas e específicas que precisam de execução cuidadosa
- **Exemplo:** "Adicionar alternador de modo escuro na página de configurações"

### **🔨 O Construtor Mestre** (`/prp-base-execute`)
- **O que fazem:** Na verdade constroem toda a funcionalidade seguindo os projetos detalhados
- **Quando usar:** Depois que você tem projetos de construção abrangentes
- **Exemplo:** Pega os projetos do botão de curtir e constrói a funcionalidade funcionando

### **🏠 A Equipe de Renovação** (`/prp-spec-execute`)
- **O que fazem:** Executam planos de renovação, transformando cuidadosamente estruturas existentes
- **Quando usar:** Depois que você tem especificações de renovação
- **Exemplo:** Na verdade migra seu sistema de autenticação

### **⚡ A Equipe Especializada** (`/prp-task-execute`)
- **O que fazem:** Lidam com tarefas focadas com precisão cirúrgica
- **Quando usar:** Depois que você tem listas de tarefas específicas
- **Exemplo:** Adiciona o alternador de modo escuro exatamente como especificado

### **🏃‍♂️ A Equipe de Resposta de Emergência** (`/task-list-init`)
- **O que fazem:** Criam planos de ação rápida para situações urgentes
- **Quando usar:** Hackathons, correções urgentes, ou quando você precisa se mover rapidamente
- **Exemplo:** "Construir um painel social em 2 dias"

---

## A Mágica: Como Eles Trabalham Juntos 🔗

**Esta é a parte CHAVE que faz tudo funcionar!**

Assim como na construção real, cada especialista constrói sobre o trabalho do anterior:

```
🏗️ Arquiteto Mestre cria projetos de construção
    ↓ (Projetos são passados para...)
📋 Engenheiro Estrutural cria especificações de conexão  
    ↓ (Tanto projetos quanto especificações são passados para...)
📐 Arquiteto de Detalhes cria manual de construção
    ↓ (Manual é passado para...)
🔨 Construtor Mestre constrói a funcionalidade real
```

**IMPORTANTE:** Cada passo usa a saída dos passos anteriores - eles não são ferramentas isoladas!

---

## O Processo Passo-a-Passo 📋

### **Para Construir Novas Funcionalidades (Mais Comum)**

**Passo 1: Obter o Panorama Geral**
```bash
/prp-planning-create "página de perfil de usuário com upload de avatar e edição de bio"
```
- Cria: `PRPs/user-profile-prd.md` (projetos arquitetônicos)
- Contém: Especificação completa da funcionalidade, fluxos de usuário, arquitetura técnica

**Passo 2: Definir Como as Partes se Conectam**  
```bash
/api-contract-define "criar endpoints de API para a funcionalidade de perfil de usuário descrita em PRPs/user-profile-prd.md"
```
- Cria: `PRPs/contracts/user-profile-api-contract.md` (especificações de conexão)
- Contém: Endpoints de API exatos, estruturas de dados, tratamento de erros

**Passo 3: Criar Instruções Detalhadas**
```bash
/prp-base-create "implementar funcionalidade de perfil de usuário usando arquitetura de PRPs/user-profile-prd.md e especificações de PRPs/contracts/user-profile-api-contract.md"
```
- Cria: `PRPs/user-profile-implementation.md` (manual de construção)
- Contém: Implementação passo-a-passo com todo o contexto necessário

**Passo 4: Construir**
```bash
/prp-base-execute PRPs/user-profile-implementation.md
```
- Resultado: Funcionalidade de perfil de usuário funcionando com todos os testes passando

---

### **Para Mudar Código Existente**

**Passo 1: Planejar as Mudanças**
```bash
/prp-spec-create "migrar autenticação de usuário de auth básico para OAuth2 com integração do Google"
```
- Cria: `SPEC_PRP/PRPs/oauth2-migration.md` (planos de renovação)
- Contém: Estado atual, estado desejado, passos de transformação

**Passo 2: Executar as Mudanças**
```bash
/prp-spec-execute SPEC_PRP/PRPs/oauth2-migration.md
```
- Resultado: Sistema de autenticação migrado com sucesso

---

### **Para Tarefas Pequenas e Focadas**

**Passo 1: Definir a Tarefa**
```bash
/prp-task-create "adicionar validação de email no formulário de cadastro com mensagens de erro apropriadas"
```
- Cria: `TASK_PRP/PRPs/email-validation.md` (ordem de trabalho)
- Contém: Tarefas específicas com validação e planos de rollback

**Passo 2: Fazer a Tarefa**
```bash
/prp-task-execute TASK_PRP/PRPs/email-validation.md
```
- Resultado: Validação de email adicionada com testes apropriados

---

### **Para Trabalho de Emergência/Rápido**

**Passo 1: Criar Plano de Ação**
```bash
/task-list-init "projeto hackathon: painel de mídia social com posts, curtidas e perfis de usuário"
```
- Cria: `PRPs/checklist.md` (plano de ação de emergência)
- Contém: Lista de tarefas priorizadas com rastreamento de status

**Passo 2: Executar Manualmente**
- Siga a lista de verificação, marcando itens conforme os completa
- Use outros comandos para partes específicas se necessário

---

## Exemplo Real Completo: Construindo um "Botão de Curtir" 💖

Vamos construir um botão de curtir de mídia social do zero, passo a passo:

### **Passo 1: O Arquiteto Mestre Faz Sua Mágica** 🏗️
```bash
/prp-planning-create "botão de curtir de mídia social com atualizações em tempo real e rastreamento de analytics"
```

**O que acontece nos bastidores:**
- IA pesquisa implementações existentes de botões de curtir
- Cria diagramas de fluxo de usuário
- Projeta esquema de banco de dados para curtidas
- Planeja arquitetura de atualização em tempo real
- Especifica requisitos de analytics
- Cria documento PRD abrangente

**Resultado:** `PRPs/like-button-prd.md` com projetos arquitetônicos completos

---

### **Passo 2: O Engenheiro Estrutural Cria Especificações de Conexão** 📋
```bash
/api-contract-define "criar contratos de API para a funcionalidade de botão de curtir especificada em PRPs/like-button-prd.md, incluindo atualizações em tempo real e analytics"
```

**O que acontece nos bastidores:**
- Lê os projetos arquitetônicos do Passo 1
- Define endpoints de API específicos:
  - `POST /api/posts/{id}/like`
  - `DELETE /api/posts/{id}/like`  
  - `GET /api/posts/{id}/likes/analytics`
- Cria interfaces TypeScript
- Especifica eventos WebSocket para atualizações em tempo real
- Define respostas de erro

**Resultado:** `PRPs/contracts/like-button-api-contract.md` com especificações técnicas exatas

---

### **Passo 3: O Arquiteto de Detalhes Cria o Manual de Construção** 📐
```bash
/prp-base-create "implementar funcionalidade de botão de curtir usando arquitetura de PRPs/like-button-prd.md e especificações de API de PRPs/contracts/like-button-api-contract.md"
```

**O que acontece nos bastidores:**
- Lê TANTO os projetos arquitetônicos QUANTO os contratos de API
- Pesquisa o codebase existente por padrões
- Cria plano de implementação passo-a-passo
- Inclui todo o contexto necessário (links de documentação, exemplos de código)
- Define processo de verificação de qualidade de 4 níveis
- Cria manual de construção abrangente

**Resultado:** `PRPs/like-button-implementation.md` com tudo necessário para construí-lo

---

### **Passo 4: O Construtor Mestre Constrói a Funcionalidade** 🔨
```bash
/prp-base-execute PRPs/like-button-implementation.md
```

**O que acontece nos bastidores:**
- **Fase de Planejamento:** Cria lista detalhada de tarefas usando TodoWrite
- **Fundação (Nível 1):** 
  - Cria migração de banco de dados para tabela de curtidas
  - Configura interfaces TypeScript
  - Executa verificação de sintaxe: `ruff check --fix && mypy .`
- **Estrutura (Nível 2):**
  - Implementa endpoints de API seguindo o contrato
  - Cria componente React com gerenciamento de estado apropriado
  - Adiciona testes unitários abrangentes
  - Executa testes: `uv run pytest tests/ -v`
- **Sistemas (Nível 3):**
  - Integra WebSocket para atualizações em tempo real
  - Conecta frontend às APIs do backend
  - Testa fluxos de usuário completos
  - Executa testes de integração
- **Inspeção Final (Nível 4):**
  - Testes de carga com múltiplos usuários simultâneos
  - Testa casos extremos e cenários de erro
  - Verifica precisão dos analytics

**Resultado:** Botão de curtir totalmente funcional com atualizações em tempo real, analytics, e todos os testes passando!

---

### **Passo 5: Adicionando uma Melhoria Rápida** ✅
```bash
/prp-task-create "adicionar efeito animado de coração flutuante quando usuários curtirem posts para melhor feedback visual"
```

**O que acontece:** Cria lista de tarefas focadas para o aprimoramento da animação

```bash
/prp-task-execute TASK_PRP/PRPs/heart-animation.md
```

**Resultado:** Linda animação de coração flutuante adicionada ao botão de curtir

---

## O Sistema de Controle de Qualidade 🔍

Toda funcionalidade passa por 4 níveis de controle de qualidade, assim como inspeções de construção:

### **Nível 1: Verificação de Fundação** 
```bash
ruff check --fix && mypy .
```
*Como verificar se a fundação está nivelada e atende aos códigos de construção*

### **Nível 2: Verificação Quarto por Quarto**
```bash
uv run pytest tests/ -v  
```
*Como testar se cada quarto funciona corretamente (luzes funcionam, portas abrem, etc.)*

### **Nível 3: Verificação de Integração de Sistemas**
```bash
curl -X POST http://localhost:8000/api/posts/123/like
```
*Como testar se encanamento, elétrica e aquecimento funcionam todos juntos*

### **Nível 4: Teste de Estresse do Mundo Real**
*Como ter uma família realmente morando na casa para encontrar problemas restantes*

---

## Quando Usar Cada Comando 🤔

### **Use `/prp-planning-create` quando:**
- Você tem uma ideia vaga que precisa se tornar um plano concreto
- Você está começando uma nova funcionalidade principal
- Você precisa pesquisar e entender o espaço do problema
- Você quer documentação abrangente com diagramas

### **Use `/api-contract-define` quando:**
- Você tem projetos arquitetônicos e precisa de especificações técnicas
- Equipes de frontend e backend precisam coordenar
- Você precisa de definições exatas de endpoints de API
- Você quer prevenir problemas de integração

### **Use `/prp-base-create` quando:**
- Você precisa de instruções de implementação abrangentes
- Você está construindo algo completamente novo
- Você quer todo o contexto e exemplos incluídos
- Você precisa do processo completo de validação de 4 níveis

### **Use `/prp-spec-create` quando:**
- Você precisa modificar código existente
- Você está fazendo uma migração ou refatoração
- Você precisa documentar estado atual vs. desejado
- Você quer planos de rollback para segurança

### **Use `/prp-task-create` quando:**
- Você tem uma mudança pequena e focada para fazer  
- Você precisa de precisão cirúrgica em código específico
- Você quer validação imediata após cada passo
- A mudança afeta apenas alguns arquivos

### **Use os comandos execute quando:**
- Você tem o documento de plano/especificação/tarefa correspondente
- Você está pronto para realmente construir/mudar o código
- Você quer implementação sistemática e validada
- Você confia que a IA seguirá as instruções detalhadas

### **Use `/task-list-init` quando:**
- Você está em um hackathon ou pressão de tempo
- Você precisa de uma visão rápida do que precisa ser feito
- Você quer rastrear progresso manualmente
- Você está fazendo prototipagem rápida

---

## Erros Comuns (Não Faça Isso!) ❌

### **❌ Usando Comandos em Isolamento**
```bash
# ERRADO - cada comando cria trabalho isolado
/api-contract-define "autenticação de usuário"
/prp-base-create "autenticação de usuário" 
```

```bash
# CERTO - cada comando constrói sobre o anterior
/prp-planning-create "autenticação de usuário com login social"
/api-contract-define "criar API para autenticação descrita em PRPs/user-auth-prd.md"
/prp-base-create "implementar autenticação usando PRPs/user-auth-prd.md e PRPs/contracts/user-auth-api-contract.md"
```

### **❌ Pulando a Fase de Planejamento**
```bash
# ERRADO - pulando direto para implementação
/prp-base-create "alguma funcionalidade complicada"
```

```bash  
# CERTO - planejar primeiro, depois implementar
/prp-planning-create "alguma funcionalidade complicada"
/prp-base-create "implementar funcionalidade usando PRPs/complicated-feature-prd.md"
```

### **❌ Não Sendo Específico**
```bash
# ERRADO - vago e inútil
/prp-base-create "tornar o app melhor"
```

```bash
# CERTO - específico e acionável  
/prp-base-create "adicionar edição de perfil de usuário com upload de avatar, edição de bio e preferências de email"
```

---

## Dicas Profissionais para Sucesso 🚀

### **🎯 Sempre Comece com Planejamento**
Para qualquer funcionalidade não trivial, comece com `/prp-planning-create`. O tempo que você gasta planejando economiza horas de confusão na implementação.

### **🔗 Conecte Seus Comandos**
Sempre referencie saídas anteriores em seu próximo comando. Se você criou `PRPs/user-auth-prd.md`, referencie-o em seu próximo comando.

### **📝 Seja Específico em Suas Solicitações**
Em vez de "adicionar autenticação," diga "adicionar autenticação OAuth2 com integração do Google e GitHub, incluindo sincronização de perfil de usuário e permissões baseadas em função."

### **🔍 Confie no Controle de Qualidade**
Deixe cada comando passar por todos os 4 níveis de qualidade. A validação pega problemas antes que se tornem problemas.

### **🏗️ Pense Como um Arquiteto**
Planeje a fundação antes de construir as paredes. Projete a estrutura geral antes de implementar componentes individuais.

### **📚 Inclua Contexto**
Ao criar PRPs de implementação, referencie padrões de código existentes, URLs de documentação e implementações similares em seu codebase.

---

## Cartão de Referência Rápida 📋

| Comando | Propósito | Entrada | Saída |
|---------|-----------|---------|-------|
| `/prp-planning-create` | Planejamento mestre | Ideia básica | PRD abrangente com diagramas |
| `/api-contract-define` | Especificações técnicas | Funcionalidade + referência PRD | Contratos de API e interfaces |
| `/prp-base-create` | Manual de implementação | Funcionalidade + todas as referências | Guia completo de construção |
| `/prp-base-execute` | Construir nova funcionalidade | Caminho do PRP de implementação | Funcionalidade funcionando |
| `/prp-spec-create` | Planos de renovação | Requisitos de mudança | Transformação atual→desejado |
| `/prp-spec-execute` | Executar mudanças | Caminho do PRP de especificação | Código modificado |
| `/prp-task-create` | Ordens de trabalho focadas | Tarefa específica | Lista detalhada de tarefas |
| `/prp-task-execute` | Fazer tarefas específicas | Caminho do PRP de tarefa | Tarefa completada |
| `/task-list-init` | Planejamento de emergência | Projeto urgente | Lista de verificação rastreável |

---

## Começando Agora Mesmo 🚀

### **Sua Primeira Funcionalidade (5 minutos)**

1. **Escolha algo simples** como "adicionar um rodapé ao site com direitos autorais e links"

2. **Planeje:**
   ```bash
   /prp-planning-create "rodapé do site com direitos autorais, link de política de privacidade e link de contato"
   ```

3. **Crie guia de implementação:**
   ```bash
   /prp-base-create "implementar rodapé usando arquitetura de PRPs/website-footer-prd.md"
   ```

4. **Construa:**
   ```bash
   /prp-base-execute PRPs/website-footer-implementation.md
   ```

5. **Celebre!** 🎉 Você acabou de usar IA para construir uma funcionalidade com planejamento apropriado, documentação e controle de qualidade!

---

## Todos os Comandos Disponíveis - A Caixa de Ferramentas Completa 🧰

### **Comandos de Desenvolvimento** 💻

#### **🎯 /prime-core - Carregar Contexto do Projeto**
- **O que fazem:** Prepara o Claude com conhecimento essencial do projeto lendo arquivos-chave
- **Quando usar:** Início de toda conversa, após mudanças importantes
- **Exemplo:** `/prime-core`
- **Resultado:** Claude entende sua estrutura de projeto e pode trabalhar efetivamente

#### **🚀 /onboarding - Criar Integração de Desenvolvedor**
- **O que fazem:** Gera documentação abrangente de integração para novos desenvolvedores
- **Quando usar:** Novos membros da equipe se juntam, documentando projetos não documentados
- **Exemplo:** `/onboarding`
- **Resultado:** Cria ONBOARDING.md e QUICKSTART.md com guias de configuração completos

#### **💾 /smart-commit ou /commit - Commits Git Inteligentes**
- **O que fazem:** Analisam mudanças e criam mensagens de commit formatadas apropriadamente
- **Quando usar:** Antes de fazer commit do código, quando seguindo convenções de commit
- **Exemplo:** `/commit "corrigindo bug de autenticação"`
- **Resultado:** Commit formatado apropriadamente com estilo de commit convencional

#### **🌿 /new-dev-branch - Criar Branch de Desenvolvimento**
- **O que fazem:** Criam uma nova branch git seguindo convenções da equipe
- **Quando usar:** Iniciando novo trabalho de funcionalidade, criando branches de correção de bug
- **Exemplo:** `/new-dev-branch feature/user-profile`
- **Resultado:** Nova branch criada com nomenclatura apropriada

#### **🔍 /debug-RCA - Análise de Causa Raiz**
- **O que fazem:** Debug sistemático para encontrar causas raiz de problemas
- **Quando usar:** Quando enfrentando bugs complexos, erros misteriosos
- **Exemplo:** `/debug-RCA "usuários não conseguem fazer login após redefinir senha"`
- **Resultado:** Análise detalhada com causa raiz e recomendações de correção

#### **🚀 /create-pr - Criar Pull Request**
- **O que fazem:** Geram PR abrangente com descrição e notas de teste
- **Quando usar:** Após conclusão da funcionalidade, pronto para revisão de código
- **Exemplo:** `/create-pr`
- **Resultado:** PR bem documentado pronto para revisão

---

### **Comandos de Qualidade de Código** 🎨

#### **🔧 /refactor-simple - Análise Rápida de Refatoração**
- **O que fazem:** Escaneiam código por oportunidades de refatoração (foco em Python)
- **Quando usar:** Antes de fazer merge, limpando dívida técnica
- **Exemplo:** `/refactor-simple`
- **Resultado:** Cria refactor_plan.md com melhorias priorizadas

#### **👀 /review-general - Revisão Abrangente de Código**
- **O que fazem:** Revisão completa verificando qualidade, segurança, performance
- **Quando usar:** Antes de commits, revisões de PR, auditorias de código
- **Exemplo:** `/review-general src/features/authentication`
- **Resultado:** Relatório de revisão detalhado em PRPs/code_reviews/

#### **📊 /review-staged-unstaged - Revisar Mudanças Git**
- **O que fazem:** Revisam especificamente o que está staged/unstaged no git
- **Quando usar:** Revisão pré-commit, entendendo mudanças atuais
- **Exemplo:** `/review-staged-unstaged`
- **Resultado:** Análise do status git atual com recomendações

---

### **Comandos de Operações Git** 🔀

#### **🛠️ /conflict-resolver-general - Resolução Básica de Conflitos**
- **O que fazem:** Resolvem conflitos de merge git inteligentemente
- **Quando usar:** Após conflitos de merge, durante rebases
- **Exemplo:** `/conflict-resolver-general`
- **Resultado:** Conflitos resolvidos com integridade mantida

#### **🧠 /smart-resolver - Resolução Avançada de Conflitos**
- **O que fazem:** Resolução de conflitos com análise profunda e entendimento de lógica de negócio
- **Quando usar:** Conflitos complexos, conflitos críticos de lógica de negócio
- **Exemplo:** `/smart-resolver`
- **Resultado:** Resolução inteligente com documentação detalhada

#### **🎯 /conflict-resolver-specific - Resolução Direcionada de Conflitos**
- **O que fazem:** Resolvem conflitos em arquivos específicos apenas
- **Quando usar:** Quando você só precisa resolver certos arquivos
- **Exemplo:** `/conflict-resolver-specific src/api/auth.ts`
- **Resultado:** Resolução direcionada dos arquivos especificados

---

### **Comandos de Desenvolvimento Rápido** ⚡

#### **🏃‍♂️ /hackathon-research - Análise Multi-Opção**
- **O que fazem:** 15 agentes paralelos analisam 3 abordagens para desafios de hackathon
- **Quando usar:** Início de hackathon, avaliando múltiplas soluções
- **Exemplo:** `/hackathon-research "ferramenta de revisão de código com IA"`
- **Resultado:** Análise abrangente com recomendação da melhor abordagem

#### **🎯 /user-story-rapid - Criação Rápida de História de Usuário**
- **O que fazem:** Geram histórias de usuário com critérios de aceitação rapidamente
- **Quando usar:** Planejamento de sprint, definição de funcionalidade
- **Exemplo:** `/user-story-rapid "gerenciamento de perfil de usuário"`
- **Resultado:** Histórias de usuário completas prontas para implementação

#### **⚡ /parallel-prp-creation - Criação de PRP em Lote**
- **O que fazem:** Criam múltiplos PRPs simultaneamente usando processamento paralelo
- **Quando usar:** Grandes conjuntos de funcionalidades, múltiplas funcionalidades relacionadas
- **Exemplo:** `/parallel-prp-creation "fluxo de checkout de e-commerce"`
- **Resultado:** Múltiplos PRPs coordenados criados eficientemente

#### **🔍 /prp-analyze-run - Analisar e Executar PRPs**
- **O que fazem:** Analisam PRPs existentes e opcionalmente os executam
- **Quando usar:** Entendendo qualidade de PRP, execução em lote
- **Exemplo:** `/prp-analyze-run`
- **Resultado:** Relatório de análise e resultados de execução

#### **✅ /prp-validate - Validar Qualidade de PRP**
- **O que fazem:** Verificam PRPs contra padrões de qualidade
- **Quando usar:** Antes da execução, garantia de qualidade
- **Exemplo:** `/prp-validate PRPs/user-auth.md`
- **Resultado:** Relatório de validação com sugestões de melhoria

#### **🚀 /create-base-prp-parallel - Criação Paralela de PRP Base**
- **O que fazem:** Criam PRPs abrangentes usando pesquisa paralela
- **Quando usar:** Funcionalidades complexas precisando de pesquisa profunda
- **Exemplo:** `/create-base-prp-parallel "colaboração em tempo real"`
- **Resultado:** PRP abrangente baseado em pesquisa

#### **📋 /create-planning-parallel - Criação Paralela de Planejamento**
- **O que fazem:** Criam PRDs de planejamento usando análise paralela
- **Quando usar:** Planejamento inicial de funcionalidade, design de arquitetura
- **Exemplo:** `/create-planning-parallel "backend de app mobile"`
- **Resultado:** PRD abrangente com múltiplas perspectivas

#### **🏁 /hackathon-prp-parallel - PRPs Otimizados para Hackathon**
- **O que fazem:** Criam PRPs de implementação rápida para hackathons
- **Quando usar:** Desenvolvimento com restrição de tempo, MVPs
- **Exemplo:** `/hackathon-prp-parallel "integração de chatbot com IA"`
- **Resultado:** PRP simplificado otimizado para velocidade

---

### **Comandos Específicos para TypeScript** 📘

#### **📐 /TS-create-base-prp - Criação de PRP TypeScript**
- **O que fazem:** Criam PRPs otimizados para projetos TypeScript
- **Quando usar:** Desenvolvimento de funcionalidade TypeScript
- **Exemplo:** `/TS-create-base-prp "cliente de API type-safe"`
- **Resultado:** PRP de implementação focado em TypeScript

#### **🔨 /TS-execute-base-prp - Executar PRPs TypeScript**
- **O que fazem:** Executam PRPs com validação específica para TypeScript
- **Quando usar:** Implementando funcionalidades TypeScript
- **Exemplo:** `/TS-execute-base-prp PRPs/api-client.md`
- **Resultado:** Implementação type-safe com validação completa

#### **👀 /TS-review-general - Revisão de Código TypeScript**
- **O que fazem:** Revisam com foco em melhores práticas TypeScript
- **Quando usar:** Revisões de código TypeScript
- **Exemplo:** `/TS-review-general src/components`
- **Resultado:** Revisão específica de TS com verificações de segurança de tipo

#### **📊 /TS-review-staged-unstaged - Revisão Git TypeScript**
- **O que fazem:** Revisam mudanças staged/unstaged de TS
- **Quando usar:** Revisões pré-commit de TS
- **Exemplo:** `/TS-review-staged-unstaged`
- **Resultado:** Análise de mudanças focada em TypeScript

---

## Referência Rápida de Categorias de Comandos 📚

### **Para Começar o Trabalho:**
- `/prime-core` - Carregar contexto do projeto
- `/onboarding` - Entender o projeto
- `/new-dev-branch` - Criar branch de funcionalidade

### **Para Planejar Funcionalidades:**
- `/prp-planning-create` - Planejamento abrangente
- `/hackathon-research` - Avaliar abordagens
- `/user-story-rapid` - Histórias de usuário rápidas

### **Para Implementação:**
- `/prp-base-create` → `/prp-base-execute` - Novas funcionalidades
- `/prp-spec-create` → `/prp-spec-execute` - Modificações
- `/prp-task-create` → `/prp-task-execute` - Tarefas pequenas

### **Para Qualidade de Código:**
- `/review-general` - Revisão completa de código
- `/refactor-simple` - Encontrar melhorias
- `/debug-RCA` - Corrigir bugs complexos

### **Para Operações Git:**
- `/smart-commit` - Criar commits
- `/conflict-resolver-general` - Resolver conflitos
- `/create-pr` - Criar pull requests

### **Para Desenvolvimento Rápido:**
- `/hackathon-research` - Análise rápida
- `/parallel-prp-creation` - Criação em lote
- `/task-list-init` - Rastreamento rápido de tarefas

---

## Dicas Profissionais para Uso de Comandos 🎯

### **🔄 Encadeamento de Comandos**
Muitos comandos funcionam melhor juntos:
```bash
/prime-core
/prp-planning-create "descrição da funcionalidade"
/api-contract-define "usando PRPs/feature-prd.md"
/prp-base-create "usando ambos os arquivos anteriores"
/prp-base-execute PRPs/feature-implementation.md
/smart-commit "feat: adicionar nova funcionalidade"
/create-pr
```

### **⚡ Processamento Paralelo**
Use comandos paralelos para velocidade:
- Fase de pesquisa: `/hackathon-research`
- Fase de planejamento: `/create-planning-parallel`
- Implementação: `/create-base-prp-parallel`

### **🎯 Contexto é Chave**
Sempre referencie saídas anteriores:
- Ruim: `/prp-base-create "autenticação de usuário"`
- Bom: `/prp-base-create "implementar autenticação usando PRPs/auth-prd.md e PRPs/contracts/auth-api.md"`

### **🔍 Revisar Cedo e Frequentemente**
- Use `/review-staged-unstaged` antes de todo commit
- Execute `/refactor-simple` semanalmente para saúde do código
- Aplique `/review-general` antes de PRs

---

## Lembre-se: Você é o Arquiteto, IA é Sua Equipe de Construção 🏗️

- **Você decide O QUE construir** (a visão, requisitos, objetivos de negócio)
- **IA descobre COMO construir** (implementação técnica, padrões de código, testes)
- **O sistema PRP garante qualidade** (planejamento apropriado, validação, documentação)

Isso não é sobre substituir criatividade humana - é sobre amplificar suas ideias com implementação sistemática e de alta qualidade.

---

**Pronto para construir algo incrível? Comece com `/prime-core`, depois `/prp-planning-create` e veja suas ideias ganharem vida!** ✨