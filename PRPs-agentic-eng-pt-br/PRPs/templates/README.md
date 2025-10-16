# 📚 Documentação PRP Traduzida para Português

Esta pasta contém todos os templates e guias do repositório [PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng) traduzidos e adaptados para português brasileiro.

## 📁 Estrutura de Pastas

### `/templates/` - Templates PRP
Templates para criação de Product Requirement Prompts (PRPs) - prompts estruturados para desenvolvimento com IA.

**Arquivos disponíveis:**
- `prp_base.md` - Template Base PRP v3 (Python/geral)
- `prp_base_typescript.md` - Template Base PRP v3 (TypeScript)
- `prp_planning.md` - Template de Planejamento (geração de PRD com diagramas)
- `prp_poc_react.md` - Template POC React v1 (desenvolvimento rápido de protótipos)
- `prp_spec.md` - Template de Especificação (inspirado por IndyDevDan)
- `prp_story_task.md` - Template PRP de História (conversão de user stories)
- `prp_task.md` - Template de Tarefa v2 (denso em informação)
- `STORY_WORKFLOW_GUIDE.md` - Guia de Fluxo de Trabalho Story PRP
- `README.md` - Conceito e Filosofia de PRP

### `/guias-tecnologia/` - Guias de Tecnologia Claude
Guias específicos de linguagem e framework para uso com Claude Code e outras ferramentas de IA.

**Arquivos disponíveis:**
- `CLAUDE-REACT.md` - Guia React 19
- `CLAUDE-PYTHON-BASIC.md` - Guia Python Básico
- `CLAUDE-NODE.md` - Guia Node.js 23
- `CLAUDE-JAVA-MAVEN.md` - Guia Java com Maven
- `CLAUDE-JAVA-GRADLE.md` - Guia Java com Gradle
- `CLAUDE-NEXTJS-15.md` - Guia Next.js 15 + React 19
- `CLAUDE-ASTRO.md` - Guia Astro 5+ (Islands Architecture)
- `CLAUDE-RUST.md` - Guia Rust 1.88

## 🎯 O que é um PRP?

Um **Product Requirement Prompt (PRP)** é um prompt estruturado que fornece a um agente de codificação de IA tudo o que ele precisa para entregar uma fatia vertical de software funcionando.

### Diferenças entre PRP e PRD

| Aspecto | PRD Tradicional | PRP |
|---------|----------------|-----|
| **Foco** | O que construir | O que + Como + Contexto |
| **Implementação** | Evita detalhes | Especifica estratégia |
| **Contexto** | Alto nível | Caminhos de arquivo, exemplos de código |
| **Validação** | Manual | Automatizada com comandos |
| **Uso** | Equipes humanas | Agentes de IA |

## 📖 Como Usar

### 1. Escolha o Template Adequado

- **`prp_base.md`** - Para funcionalidades completas em Python
- **`prp_base_typescript.md`** - Para funcionalidades completas em TypeScript/JavaScript
- **`prp_planning.md`** - Para planejar e criar PRDs com diagramas
- **`prp_poc_react.md`** - Para criar protótipos React rapidamente
- **`prp_story_task.md`** - Para converter user stories do Jira/Linear
- **`prp_task.md`** - Para tarefas específicas e bem definidas
- **`prp_spec.md`** - Para especificações técnicas detalhadas

### 2. Consulte o Guia de Tecnologia

Antes de criar seu PRP, leia o guia de tecnologia correspondente em `/guias-tecnologia/` para entender:
- Padrões de código recomendados
- Estrutura de arquivos
- Convenções de nomenclatura
- Melhores práticas
- Anti-padrões a evitar

### 3. Preencha o Template

Siga a estrutura do template escolhido, fornecendo:
- **Objetivo**: O que precisa ser construído
- **Contexto**: Arquivos relevantes, padrões existentes
- **Blueprint**: Tarefas ordenadas de implementação
- **Validação**: Comandos para verificar cada etapa

### 4. Execute com Agente de IA

Use ferramentas como:
- **Claude Code** (Cursor, Windsurf)
- **GitHub Copilot**
- **Aider**
- Outros agentes de codificação

## 🔑 Conceitos-Chave

### Arquitetura Vertical Slice
Organize código por funcionalidade, não por camada técnica.

### Validação em Loops
Cada tarefa tem validação inline:
```bash
# Nível 1: Sintaxe
ruff check src/ && mypy src/

# Nível 2: Testes
pytest src/tests/

# Nível 3: Integração
curl http://localhost:8000/api/endpoint

# Nível 4: Específico do domínio
# Performance, segurança, etc.
```

### Padrões > Inovação
Siga padrões existentes da base de código em vez de criar novos.

## 📚 Recursos Adicionais

### Repositório Original
[Wirasm/PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng)

### Exemplos de Uso
Veja a pasta `/examples/` no projeto principal para exemplos completos de PRPs.

### Contribuindo
Para melhorias ou correções nas traduções, abra uma issue ou pull request.

## 🌟 Melhores Práticas

1. **Seja Específico**: Forneça caminhos exatos, não descrições vagas
2. **Inclua Contexto**: Referências de código, padrões existentes
3. **Valide Cedo**: Comandos de validação após cada tarefa
4. **Falhe Rápido**: Valide entradas cedo, lance erros imediatamente
5. **KISS**: Keep It Simple, Stupid - simplicidade sobre complexidade
6. **YAGNI**: You Aren't Gonna Need It - implemente apenas o necessário

## 📝 Licença

Os templates e guias originais são de [Wirasm/PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng).
Esta tradução foi feita para facilitar o uso pela comunidade brasileira de desenvolvimento.

---

**Dica**: Comece com `README.md` em `/templates/` para entender a filosofia completa dos PRPs antes de usar os templates!
