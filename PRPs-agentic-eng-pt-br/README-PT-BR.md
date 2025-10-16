# 🇧🇷 PRPs Agentic Engineering - Versão Português Brasil

> Tradução e adaptação completa do repositório [Wirasm/PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng) para português brasileiro.

## 📚 O que é este projeto?

Este é um framework completo de **Product Requirement Prompts (PRPs - Prompts de Requisitos de Produto)** - prompts estruturados otimizados para desenvolvimento com IA que combinam:
- Escopo disciplinado de PRDs tradicionais
- Contexto rico para agentes de IA
- Validação automatizada em múltiplos níveis
- Padrões de código e melhores práticas

## 🎯 Conceito Central: O que é um PRP?

**PRP = PRD + inteligência de codebase curada + agente/runbook**

É o pacote viável mínimo que uma IA precisa para plausivelmente entregar código pronto para produção na primeira tentativa.

### Como Difere de um PRD Tradicional

| Aspecto | PRD Tradicional | PRP |
|---------|----------------|-----|
| **Objetivo** | O QUE construir | O QUE + COMO construir |
| **Contexto** | Mínimo/genérico | Máximo/específico |
| **Implementação** | Não especificado | Detalhado com padrões |
| **Validação** | Manual | Automatizada em 4 níveis |
| **Público** | Stakeholders | Agentes de IA + Desenvolvedores |

## 🗂️ Estrutura do Repositório

```
PRPs-agentic-eng-pt-br/
├── 📄 README.md                    # README principal ✅ TRADUZIDO
├── 📄 README-PT-BR.md              # Este arquivo - índice completo em português
├── 📄 CLAUDE.md                    # Instruções para Claude ✅ TRADUZIDO
├── 📄 README-for-DUMMIES.md        # Guia completo para iniciantes
│
├── 📁 .claude/                     # Comandos e agentes Claude Code
│   ├── agents/                     # 2 agentes especializados
│   │   ├── codebase-analyst.md    # Análise de padrões de código
│   │   └── library-researcher.md  # Pesquisa de bibliotecas
│   │
│   └── commands/                   # 28+ comandos pré-configurados
│       ├── code-quality/           # Revisão e refatoração
│       ├── development/            # Utilitários de desenvolvimento
│       ├── git-operations/         # Operações Git inteligentes
│       ├── prp-commands/           # Comandos PRP principais
│       ├── rapid-development/      # Desenvolvimento rápido
│       └── typescript/             # Específicos para TypeScript
│
├── 📁 PRPs/                        # Coração do framework
│   ├── README.md                   # Conceito PRP ✅ TRADUZIDO
│   ├── STORY_WORKFLOW_GUIDE.md    # Guia de fluxo Story PRP ✅ TRADUZIDO
│   │
│   ├── templates/                  # 7 templates PRP
│   │   ├── prp_base.md            # Template base completo
│   │   ├── prp_base_typescript.md # Template TypeScript
│   │   ├── prp_planning.md        # Template de planejamento
│   │   ├── prp_poc_react.md       # Template POC React
│   │   ├── prp_spec.md            # Template de especificação
│   │   ├── prp_story_task.md      # Template Story/Task
│   │   └── prp_task.md            # Template de tarefa
│   │
│   ├── ai_docs/                    # 15 documentações Claude Code
│   │   ├── build_with_claude_code.md
│   │   ├── cc_administration.md
│   │   ├── cc_cli.md
│   │   ├── cc_commands.md
│   │   ├── cc_containers.md
│   │   ├── cc_deployment.md
│   │   ├── cc_hooks.md
│   │   ├── cc_mcp.md
│   │   ├── cc_monitoring.md
│   │   ├── cc_settings.md
│   │   ├── cc_troubleshoot.md
│   │   ├── getting_started.md
│   │   ├── github_actions.md
│   │   ├── hooks.md
│   │   └── subagents.md
│   │
│   ├── scripts/                    # Scripts utilitários
│   │   └── prp_runner.py          # Runner PRP em Python
│   │
│   └── *.md                        # PRPs de exemplo
│
└── 📁 claude_md_files/             # 8 guias de tecnologia
    ├── CLAUDE-ASTRO.md            # Guia Astro 5+
    ├── CLAUDE-JAVA-GRADLE.md      # Guia Java/Gradle
    ├── CLAUDE-JAVA-MAVEN.md       # Guia Java/Maven
    ├── CLAUDE-NEXTJS-15.md        # Guia Next.js 15
    ├── CLAUDE-NODE.md             # Guia Node.js 23
    ├── CLAUDE-PYTHON-BASIC.md     # Guia Python
    ├── CLAUDE-REACT.md            # Guia React 19
    └── CLAUDE-RUST.md             # Guia Rust 1.88+
```

## 🚀 Como Começar

### Opção 1: Copiar para Projeto Existente

```bash
# Copie os comandos Claude
cp -r PRPs-agentic-eng-pt-br/.claude/commands .claude/

# Copie os templates e runner PRP
cp -r PRPs-agentic-eng-pt-br/PRPs/templates PRPs/
cp -r PRPs-agentic-eng-pt-br/PRPs/scripts PRPs/

# Copie documentação AI (opcional mas recomendado)
cp -r PRPs-agentic-eng-pt-br/PRPs/ai_docs PRPs/
```

### Opção 2: Clonar e Iniciar Novo Projeto

```bash
git clone [este-repositório]
cd PRPs-agentic-eng-pt-br

# Para projetos Python
mkdir -p src/tests
touch src/__init__.py pyproject.toml CLAUDE.md
uv venv && uv sync
```

## 📋 Comandos Claude Disponíveis

### Comandos PRP (Principais)

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/prp-base-create` | Criar PRP abrangente com pesquisa | Novas funcionalidades complexas |
| `/prp-base-execute` | Executar PRP contra codebase | Implementar funcionalidade planejada |
| `/prp-planning-create` | Criar documento de planejamento com diagramas | Fase de concepção/arquitetura |
| `/prp-spec-create` | Criar especificação de transformação | Refatorações e migrações |
| `/prp-spec-execute` | Executar especificação | Aplicar transformações planejadas |
| `/prp-story-create` | Converter história de usuário em PRP | Tarefas de sprint, bugs |
| `/prp-story-execute` | Executar Story PRP | Implementar história/tarefa |
| `/prp-task-create` | Criar PRP de tarefa focada | Mudanças pequenas e focadas |
| `/prp-task-execute` | Executar tarefa | Completar tarefa específica |

### Comandos de Desenvolvimento

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/prime-core` | Carregar contexto do projeto | Início de cada conversa |
| `/onboarding` | Gerar documentação de onboarding | Novos membros da equipe |
| `/debug-RCA` | Análise de causa raiz | Bugs complexos |
| `/smart-commit` | Criar commit inteligente | Antes de commits |
| `/create-pr` | Criar pull request | Após completar funcionalidade |
| `/new-dev-branch` | Criar branch de desenvolvimento | Iniciar novo trabalho |

### Comandos de Qualidade de Código

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/review-general` | Revisão abrangente de código | Antes de PRs, auditorias |
| `/review-staged-unstaged` | Revisar mudanças Git | Pré-commit |
| `/refactor-simple` | Análise de refatoração | Limpeza de dívida técnica |

### Comandos Git

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/conflict-resolver-general` | Resolver conflitos Git | Após merge conflicts |
| `/smart-resolver` | Resolução avançada de conflitos | Conflitos complexos |
| `/conflict-resolver-specific` | Resolução direcionada | Conflitos em arquivos específicos |

### Comandos TypeScript

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/TS-create-base-prp` | Criar PRP TypeScript | Projetos TypeScript/React |
| `/TS-execute-base-prp` | Executar PRP TypeScript | Implementar features TS |
| `/TS-review-general` | Revisão código TypeScript | Revisões específicas de TS |
| `/TS-review-staged-unstaged` | Revisar mudanças TS Git | Pré-commit TS |

### Comandos de Desenvolvimento Rápido

| Comando | Descrição | Quando Usar |
|---------|-----------|-------------|
| `/hackathon-research` | Análise multi-opção com 15 agentes | Hackathons, avaliar soluções |
| `/parallel-prp-creation` | Criar múltiplos PRPs em paralelo | Conjuntos grandes de funcionalidades |
| `/prp-validate` | Validar qualidade PRP | QA antes de execução |
| `/create-base-prp-parallel` | PRP com pesquisa paralela | Features complexas |
| `/hackathon-prp-parallel` | PRP otimizado para hackathon | Desenvolvimento com restrição de tempo |

## 📐 Templates PRP

### 1. `prp_base.md` - Template Base Completo
**Uso:** Funcionalidades novas e complexas

**Estrutura:**
- Objetivo, Por quê, O quê
- Todo Contexto Necessário (URLs, arquivos, gotchas)
- Blueprint de Implementação
- Loop de Validação (4 níveis)

### 2. `prp_base_typescript.md` - Template TypeScript
**Uso:** Projetos TypeScript/React/Next.js

**Diferenças do base:**
- Exemplos TypeScript específicos
- Validação com `tsc --noEmit`
- Padrões React/Next.js

### 3. `prp_planning.md` - Template de Planejamento
**Uso:** Fase de planejamento e concepção

**Características:**
- Geração de PRD com diagramas Mermaid
- 4 fases de planejamento
- Pesquisa de mercado e técnica

### 4. `prp_poc_react.md` - Template POC React
**Uso:** Prototipação rápida para validação

**Foco:**
- Desenvolvimento rápido
- Validação de conceito
- Não qualidade de produção

### 5. `prp_spec.md` - Template de Especificação
**Uso:** Transformações e migrações

**Inclui:**
- Estado atual vs desejado
- Objetivos hierárquicos
- Estratégia de implementação

### 6. `prp_story_task.md` - Template Story/Task
**Uso:** Histórias de usuário e tarefas de sprint

**Características:**
- Conversão de história em tarefas
- Palavras-chave densas em informação
- Validação por tarefa

### 7. `prp_task.md` - Template de Tarefa
**Uso:** Tarefas Jira/GitHub

**Foco:**
- Tarefas executáveis
- Contexto incorporado
- Comandos de validação

## 🎯 Fluxos de Trabalho Típicos

### Fluxo 1: Nova Funcionalidade Complexa

```bash
# 1. Planejar
/prp-planning-create "sistema de autenticação com OAuth2"

# 2. Criar implementação
/prp-base-create "implementar auth usando PRPs/auth-prd.md"

# 3. Executar
/prp-base-execute PRPs/auth-implementation.md

# 4. Revisar
/review-staged-unstaged

# 5. Commit e PR
/smart-commit "feat: adicionar autenticação OAuth2"
/create-pr
```

### Fluxo 2: História de Usuário (Sprint)

```bash
# 1. Converter história em PRP
/prp-story-create "Como usuário, quero editar meu perfil"

# 2. Executar
/prp-story-execute PRPs/story_user_profile_edit.md

# 3. Revisar e commit
/review-staged-unstaged
/smart-commit "feat: adicionar edição de perfil"
```

### Fluxo 3: Refatoração/Migração

```bash
# 1. Criar especificação
/prp-spec-create "migrar de REST para GraphQL"

# 2. Executar transformação
/prp-spec-execute SPEC_PRP/PRPs/graphql-migration.md

# 3. Validar
/review-general src/api
```

### Fluxo 4: Bug Fix Rápido

```bash
# 1. Debugar
/debug-RCA "usuários não conseguem fazer login"

# 2. Criar tarefa
/prp-task-create "corrigir validação de senha no login"

# 3. Executar
/prp-task-execute TASK_PRP/PRPs/fix-login-validation.md
```

## 💡 Melhores Práticas

### 1. Contexto é Rei 👑
- Sempre inclua URLs específicas com seções
- Reference arquivos existentes do codebase
- Document gotchas e armadilhas conhecidas
- Use exemplos concretos, não abstratos

### 2. Validação em 4 Níveis ✅
```bash
# Nível 1: Sintaxe e Estilo
ruff check --fix && mypy .

# Nível 2: Testes Unitários
pytest tests/ -v

# Nível 3: Testes de Integração
# Testes end-to-end, APIs, etc.

# Nível 4: Validação Criativa
# MCP servers, benchmarks, etc.
```

### 3. Informação Densa 📊
Use palavras-chave específicas:
- `CREATE`, `UPDATE`, `ADD`, `REMOVE`, `REFACTOR`, `MIRROR`
- `PATTERN`, `IMPORTS`, `GOTCHA`, `VALIDATE`

### 4. Sucesso Progressivo 📈
1. Comece simples
2. Valide cada passo
3. Itere e aprimorevolha
4. Documente aprendizados

## 🔧 Agentes Especializados

### @codebase-analyst
**Função:** Análise profunda de padrões do codebase

**Usa para:**
- Descoberta de convenções
- Extração de padrões
- Análise de arquitetura
- Padrões de teste

### @library-researcher
**Função:** Pesquisa de documentação externa

**Usa para:**
- Documentação oficial
- Exemplos de implementação
- Melhores práticas
- Problemas conhecidos

## 📚 Guias de Tecnologia

### Guias Disponíveis (claude_md_files/)

| Tecnologia | Arquivo | Foco Principal |
|------------|---------|----------------|
| **Astro 5+** | CLAUDE-ASTRO.md | Islands Architecture, performance |
| **Java/Gradle** | CLAUDE-JAVA-GRADLE.md | Gradle, Spring Boot |
| **Java/Maven** | CLAUDE-JAVA-MAVEN.md | Maven, configuração POM |
| **Next.js 15** | CLAUDE-NEXTJS-15.md | App Router, React 19, Server Components |
| **Node.js 23** | CLAUDE-NODE.md | ESM, fetch API, Test Runner |
| **Python** | CLAUDE-PYTHON-BASIC.md | Ruff, mypy, pytest |
| **React 19** | CLAUDE-REACT.md | React Compiler, Actions, Suspense |
| **Rust 1.88+** | CLAUDE-RUST.md | Edition 2024, async/await |

### Princípios Comuns

Todos os guias enfatizam:
- **KISS** (Keep It Simple, Stupid)
- **YAGNI** (You Aren't Gonna Need It)
- **Vertical Slice Architecture**
- **Composition Over Inheritance**
- **Fail Fast**
- **Dependency Inversion**
- **Open/Closed Principle**
- **Single Responsibility**

## 📊 Status de Tradução

### ✅ Totalmente Traduzido
- README.md (principal)
- CLAUDE.md
- PRPs/README.md (conceito PRP)
- PRPs/STORY_WORKFLOW_GUIDE.md
- README-PT-BR.md (este arquivo)

### 🔄 Em Tradução
- Templates PRP (7 arquivos)
- Comandos Claude (28+ arquivos)
- Agentes (2 arquivos)

### ⏳ Pendente
- Documentação AI (PRPs/ai_docs/ - 15 arquivos)
- Guias de tecnologia (claude_md_files/ - 8 arquivos)
- PRPs de exemplo

## 🎓 Recursos de Aprendizado

### Para Iniciantes
1. Leia `README-for-DUMMIES.md` - Guia completo com analogias
2. Leia `PRPs/README.md` - Entenda o conceito de PRP
3. Experimente com `/prime-core` e `/prp-base-create`

### Para Intermediários
1. Leia `PRPs/STORY_WORKFLOW_GUIDE.md`
2. Explore os templates em `PRPs/templates/`
3. Use subagentes especializados

### Para Avançados
1. Crie comandos personalizados em `.claude/commands/`
2. Use desenvolvimento paralelo com Git worktrees
3. Integre com CI/CD usando modo headless

## 🛠️ Executando PRPs

### Modo Interativo (Desenvolvimento)
```bash
uv run PRPs/scripts/prp_runner.py --prp nome-prp --interactive
```

### Modo Headless (CI/CD)
```bash
uv run PRPs/scripts/prp_runner.py --prp nome-prp --output-format json
```

### Modo Streaming (Monitoramento)
```bash
uv run PRPs/scripts/prp_runner.py --prp nome-prp --output-format stream-json
```

## 🤝 Contribuindo

Este é um repositório de tradução. Para contribuir:
1. Corrija erros de tradução
2. Melhore clareza de textos
3. Adicione exemplos em português
4. Reporte issues no repositório original

## 📞 Suporte

- **Repositório Original**: https://github.com/Wirasm/PRPs-agentic-eng
- **Autor Original**: Rasmus Widing
- **Buy me a coffee**: https://coff.ee/wirasm
- **Workshops**: https://www.rasmuswiding.com/

## 📄 Licença

MIT License - Mesmo do repositório original

---

**Lembre-se**: O objetivo é sucesso de implementação em uma tentativa através de contexto abrangente. Boa codificação com Claude Code! 🚀
