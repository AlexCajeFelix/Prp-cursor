# CLAUDE.md

Este arquivo fornece orientação ao Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Natureza do Projeto

Este é um repositório de **Framework PRP (Product Requirement Prompt)**, não um projeto de software tradicional. O conceito central: **"PRP = PRD + inteligência de codebase curada + agente/runbook"** - projetado para permitir que agentes de IA entreguem código pronto para produção na primeira tentativa.

## Arquitetura Central

### Sistema Orientado a Comandos

- **comandos Claude Code pré-configurados** em `.claude/commands/`
- Comandos organizados por função:
  - `PRPs/` - Fluxos de trabalho de criação e execução de PRP
  - `development/` - Utilitários centrais de desenvolvimento (prime-core, onboarding, debug)
  - `code-quality/` - Comandos de revisão e refatoração
  - `rapid-development/experimental/` - Criação paralela de PRP e ferramentas de hackathon
  - `git-operations/` - Resolução de conflitos e operações inteligentes do git

### Metodologia Baseada em Templates

- **Templates PRP** em `PRPs/templates/` seguem formato estruturado com loops de validação
- **Abordagem Rica em Contexto**: Cada PRP deve incluir documentação abrangente, exemplos e armadilhas
- **Design com Validação em Primeiro Lugar**: Cada PRP contém portões de validação executáveis (sintaxe, testes, integração)

### Curadoria de Documentação IA

- `PRPs/ai_docs/` contém documentação curada do Claude Code para injeção de contexto
- `claude_md_files/` fornece exemplos de CLAUDE.md específicos de framework

## Comandos de Desenvolvimento

### Execução de PRP

```bash
# Modo interativo (recomendado para desenvolvimento)
uv run PRPs/scripts/prp_runner.py --prp [nome-prp] --interactive

# Modo headless (para CI/CD)
uv run PRPs/scripts/prp_runner.py --prp [nome-prp] --output-format json

# JSON em streaming (para monitoramento em tempo real)
uv run PRPs/scripts/prp_runner.py --prp [nome-prp] --output-format stream-json
```

### Comandos Claude Principais

- `/prp-base-create` - Gerar PRPs abrangentes com pesquisa
- `/prp-base-execute` - Executar PRPs contra codebase
- `/prp-planning-create` - Criar documentos de planejamento com diagramas
- `/prime-core` - Preparar Claude com contexto do projeto
- `/review-staged-unstaged` - Revisar mudanças do git usando metodologia PRP

## Padrões Críticos de Sucesso

### A Metodologia PRP

1. **Contexto é Rei**: Inclua TODA a documentação necessária, exemplos e avisos
2. **Loops de Validação**: Forneça testes/lints executáveis que a IA possa rodar e corrigir
3. **Denso em Informação**: Use palavras-chave e padrões do codebase
4. **Sucesso Progressivo**: Comece simples, valide, depois aprimorevolha

### Requisitos de Estrutura PRP

- **Objetivo**: Estado final específico e desejos
- **Por quê**: Valor de negócio e impacto no usuário
- **O quê**: Comportamento visível ao usuário e requisitos técnicos
- **Todo Contexto Necessário**: URLs de documentação, exemplos de código, armadilhas, padrões
- **Blueprint de Implementação**: Pseudocódigo com detalhes críticos e listas de tarefas
- **Loop de Validação**: Comandos executáveis para sintaxe, testes, integração

### Portões de Validação (Devem ser Executáveis)

```bash
# Nível 1: Sintaxe e Estilo
ruff check --fix && mypy .

# Nível 2: Testes Unitários
uv run pytest tests/ -v

# Nível 3: Integração
uv run uvicorn main:app --reload
curl -X POST http://localhost:8000/endpoint -H "Content-Type: application/json" -d '{...}'

# Nível 4: Implantação
# servidores mcp, ou outras maneiras criativas de auto-validação
```

## Anti-Padrões a Evitar

- ❌ Não crie prompts com contexto mínimo - contexto é tudo - o PRP deve ser abrangente e autocontido, referenciando documentação e exemplos relevantes.
- ❌ Não pule etapas de validação - elas são críticas para sucesso em uma tentativa - Quanto melhor a IA estiver em executar o loop de validação, mais provável é que tenha sucesso.
- ❌ Não ignore o formato estruturado de PRP - ele foi testado em batalha
- ❌ Não crie novos padrões quando templates existentes funcionam
- ❌ Não codifique valores que deveriam ser config
- ❌ Não capture todas as exceções - seja específico

## Trabalhando com Este Framework

### Ao Criar novos PRPs

1. **Processo de Contexto**: Novos PRPs devem consistir em seções de contexto, Contexto é Rei!
2.

### Ao Executar PRPs

1. **Carregar PRP**: Ler e entender todo contexto e requisitos
2. **ULTRATHINK**: Criar plano abrangente, dividir em todos, usar subagentes, batch tool etc verificar prps/ai_docs/
3. **Executar**: Implementar seguindo o blueprint
4. **Validar**: Executar cada comando de validação, corrigir falhas
5. **Completar**: Garantir que todos os itens da checklist estejam feitos

### Uso de Comandos

- Leia o diretório .claude/commands
- Acesse via prefixo `/` no Claude Code
- Comandos são autodocumentados com placeholders de argumentos
- Use comandos de criação paralela para desenvolvimento rápido
- Aproveite comandos existentes de revisão e refatoração

## Entendendo a Estrutura do Projeto

```
PRPs-agentic-eng/
.claude/
  commands/           # 28+ comandos Claude Code
  settings.local.json # Permissões de ferramentas
PRPs/
  templates/          # Templates PRP com validação
  scripts/           # Runner PRP e utilitários
  ai_docs/           # Documentação curada do Claude Code
   *.md               # PRPs ativos e exemplos
 claude_md_files/        # Exemplos de CLAUDE.md específicos de framework
 pyproject.toml         # Configuração de pacote Python
```

Lembre-se: Este framework é sobre **sucesso de implementação em uma tentativa através de contexto abrangente e validação**. Cada PRP deve conter o contexto exato para um agente de IA implementar com sucesso código funcionando em uma única tentativa.
