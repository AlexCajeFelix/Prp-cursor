# PRP (Product Requirement Prompts - Prompts de Requisitos de Produto)

- Uma coleção de prompts que uso no meu trabalho do dia a dia

## Demonstração em Vídeo

👉 https://www.youtube.com/watch?v=KVOZ9s1S9Gk&lc=UgzfwxvFjo6pKEyPo1R4AaABAg

### ☕ Apoie Este Trabalho

**Encontrou valor nestes recursos?**

👉 **Pague-me um café:** https://coff.ee/wirasm

Passei um tempo considerável criando esses recursos e prompts. Se você encontrar valor neste projeto, considere pagar-me um café para apoiar meu trabalho.

Isso me ajudará a manter e melhorar os recursos disponíveis gratuitamente

---

### 🎯 Transforme Sua Equipe com Workshops de Engenharia de IA

**Pronto para ir além de demos de brinquedo para sistemas de IA prontos para produção?**

👉 **Agende um workshop:** https://www.rasmuswiding.com/

✅ **O que você receberá:**

- Coloque sua equipe no caminho para se tornar usuários avançados de IA
- Aprenda a metodologia PRP exata usada por equipes de engenharia de ponta
- Treinamento prático com Claude Code, PRPs e codebases reais
- De iniciante a workshops avançados de engenharia de IA para equipes e indivíduos

💡 **Perfeito para:** Equipes de engenharia, equipes de produto e desenvolvedores que querem IA que realmente funcione em produção

Vamos conversar!
Entre em contato diretamente em rasmus@widinglabs.com

# Recursos de Engenharia de IA para Claude Code

Uma biblioteca abrangente de ativos e engenharia de contexto para Engenharia Agêntica, otimizada para Claude Code. Este repositório fornece a metodologia Product Requirement Prompt (PRP), comandos pré-configurados e documentação extensa para permitir desenvolvimento assistido por IA que entrega código pronto para produção na primeira tentativa.

## O que é PRP?

Product Requirement Prompt (PRP - Prompt de Requisitos de Produto)

## Em Resumo

Um PRP é PRD + inteligência de codebase curada + agente/runbook—o pacote viável mínimo que uma IA precisa para plausivelmente entregar código pronto para produção na primeira tentativa.

Product Requirement Prompt (PRP) é uma metodologia de prompt estruturado estabelecida pela primeira vez no verão de 2024 com engenharia de contexto no centro. Um PRP fornece a um agente de codificação de IA tudo o que ele precisa para entregar uma fatia vertical de software funcionando—nem mais, nem menos.

### Como o PRP Difere do PRD Tradicional

Um PRD tradicional esclarece o que o produto deve fazer e por que os clientes precisam dele, mas deliberadamente evita como será construído.

Um PRP mantém as seções de objetivo e justificativa de um PRD, mas adiciona três camadas críticas para IA:

### Contexto

Caminhos e conteúdo precisos de arquivos, versões de biblioteca e contexto de biblioteca, exemplos de snippets de código. LLMs geram código de maior qualidade quando recebem referências diretas no prompt em vez de descrições amplas. Uso de um diretório ai_docs/ para inserir documentação de biblioteca e outros docs.

## Começando

### Opção 1: Copiar Recursos para Seu Projeto Existente

1. **Copie os comandos Claude** para seu projeto:

   ```bash
   # Da raiz do seu projeto
   cp -r /caminho/para/PRPs-agentic-eng/.claude/commands .claude/
   ```

2. **Copie os templates PRP e o runner**:

   ```bash
   cp -r /caminho/para/PRPs-agentic-eng/PRPs/templates PRPs/
   cp -r /caminho/para/PRPs-agentic-eng/PRPs/scripts PRPs/
   cp /caminho/para/PRPs-agentic-eng/PRPs/README.md PRPs/
   ```

3. **Copie a documentação AI** (opcional mas recomendado):
   ```bash
   cp -r /caminho/para/PRPs-agentic-eng/PRPs/ai_docs PRPs/
   ```

### Opção 2: Clonar e Iniciar um Novo Projeto

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/Wirasm/PRPs-agentic-eng.git
   cd PRPs-agentic-eng
   ```

2. **Crie a estrutura do seu projeto**:

   ```bash
   # Exemplo para um projeto Python
   mkdir -p src/tests
   touch src/__init__.py
   touch pyproject.toml
   touch CLAUDE.md
   ```

3. **Inicialize com UV** (para projetos Python):
   ```bash
   uv venv
   uv sync
   ```

## Usando Comandos Claude

O diretório `.claude/commands/` contém 12 comandos pré-configurados que aparecem como comandos de barra no Claude Code.

### Comandos Disponíveis

1. **Criação e Execução de PRP**:
   - `/create-base-prp` - Gerar PRPs abrangentes com pesquisa
   - `/execute-base-prp` - Executar PRPs contra codebase
   - `/planning-create` - Criar documentos de planejamento com diagramas
   - `/spec-create-adv` - Criação avançada de especificação
   - `/spec-execute` - Executar especificações

2. **Revisão de Código e Refatoração**:
   - `/review-general` - Revisão geral de código
   - `/review-staged-unstaged` - Revisar mudanças do git
   - `/refactor-simple` - Tarefas de refatoração simples

3. **Git & GitHub**:
   - `/create-pr` - Criar pull requests

4. **Utilitários**:
   - `/prime-core` - Preparar Claude com contexto do projeto
   - `/onboarding` - Processo de onboarding para novos membros da equipe
   - `/debug` - Fluxo de trabalho de depuração

### Como Usar os Comandos

1. **No Claude Code**, digite `/` para ver comandos disponíveis
2. **Selecione um comando** e forneça argumentos quando solicitado
3. **Exemplo de uso**:
   ```
   /create-base-prp sistema de autenticação de usuário com OAuth2
   ```

## Usando PRPs

### Criando um PRP

1. **Use o template** como ponto de partida:

   ```bash
   cp PRPs/templates/prp_base.md PRPs/minha-funcionalidade.md
   ```

2. **Preencha as seções**:
   - Objetivo: O que precisa ser construído
   - Por quê: Valor de negócio e impacto no usuário
   - Contexto: Documentação, exemplos de código, armadilhas
   - Blueprint de Implementação: Tarefas e pseudocódigo
   - Loop de Validação: Testes executáveis

3. **Ou use Claude para gerar um**:
   ```
   /create-base-prp implementar autenticação de usuário com tokens JWT
   ```

### Executando um PRP

1. **Usando o script runner**:

   ```bash
   # Modo interativo (recomendado para desenvolvimento)
   uv run PRPs/scripts/prp_runner.py --prp minha-funcionalidade --interactive

   # Modo headless (para CI/CD)
   uv run PRPs/scripts/prp_runner.py --prp minha-funcionalidade --output-format json

   # JSON em streaming (para monitoramento em tempo real)
   uv run PRPs/scripts/prp_runner.py --prp minha-funcionalidade --output-format stream-json
   ```

2. **Usando comandos Claude**:
   ```
   /execute-base-prp PRPs/minha-funcionalidade.md
   ```

### Melhores Práticas de PRP

1. **Contexto é Rei**: Inclua TODA a documentação necessária, exemplos e avisos
2. **Loops de Validação**: Forneça testes/lints executáveis que a IA possa rodar e corrigir
3. **Denso em Informação**: Use palavras-chave e padrões do codebase
4. **Sucesso Progressivo**: Comece simples, valide, depois aprimorevolha

### Exemplo de Estrutura de PRP

```markdown
## Objetivo

Implementar autenticação de usuário com tokens JWT

## Por quê

- Permitir sessões de usuário seguras
- Suportar autenticação de API
- Substituir autenticação básica por padrão da indústria

## O quê

Sistema de autenticação baseado em JWT com login, logout e atualização de token

### Critérios de Sucesso

- [ ] Usuários podem fazer login com email/senha
- [ ] Tokens JWT expiram após 24 horas
- [ ] Tokens de atualização funcionam corretamente
- [ ] Todos os endpoints devidamente protegidos

## Todo Contexto Necessário

### Documentação e Referências

- url: https://jwt.io/introduction/
  por quê: Estrutura JWT e melhores práticas

- file: src/auth/basic_auth.py
  por quê: Padrão de autenticação atual a ser substituído

- doc: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
  seção: OAuth2 com Senha e JWT

### Armadilhas Conhecidas

# CRÍTICO: Use algoritmo RS256 para produção

# CRÍTICO: Armazene tokens de atualização em cookies httpOnly

# CRÍTICO: Implemente lista negra de tokens para logout

## Blueprint de Implementação

[... plano detalhado de implementação ...]

## Loop de Validação

### Nível 1: Sintaxe e Estilo

ruff check src/ --fix
mypy src/

### Nível 2: Testes Unitários

uv run pytest tests/test_auth.py -v

### Nível 3: Teste de Integração

curl -X POST http://localhost:8000/auth/login \
 -H "Content-Type: application/json" \
 -d '{"email": "test@example.com", "password": "testpass"}'
```

## Recomendações de Estrutura de Projeto

```
seu-projeto/
|-- .claude/
|   |-- commands/          # Comandos Claude Code
|   `-- settings.json      # Permissões de ferramentas
|-- PRPs/
|   |-- templates/         # Templates PRP
|   |-- scripts/          # Runner PRP
|   |-- ai_docs/          # Documentação de biblioteca
|   |-- completed/        # PRPs finalizados
|   `-- *.md              # PRPs ativos
|-- CLAUDE.md             # Diretrizes específicas do projeto
|-- src/                  # Seu código fonte
`-- tests/                # Seus testes
```

## Configurando CLAUDE.md

Crie um arquivo `CLAUDE.md` na raiz do seu projeto com:

1. **Princípios Fundamentais**: KISS, YAGNI, etc.
2. **Estrutura de Código**: Limites de tamanho de arquivo, comprimento de função
3. **Arquitetura**: Como seu projeto está organizado
4. **Testes**: Padrões e requisitos de teste
5. **Convenções de Estilo**: Diretrizes específicas da linguagem
6. **Comandos de Desenvolvimento**: Como executar testes, lint, etc.

Veja o exemplo CLAUDE.md neste repositório para um template abrangente.

## Uso Avançado

### Executando Múltiplas Sessões Claude

Use worktrees do Git para desenvolvimento paralelo:

```bash
git worktree add -b feature-auth ../project-auth
git worktree add -b feature-api ../project-api

# Execute Claude em cada worktree
cd ../project-auth && claude
cd ../project-api && claude
```

### Integração CI/CD

Use o runner PRP em modo headless:

```yaml
# Exemplo GitHub Actions
- name: Executar PRP
  run: |
    uv run PRPs/scripts/prp_runner.py \
      --prp implementar-funcionalidade \
      --output-format json > result.json
```

### Comandos Personalizados

Crie seus próprios comandos em `.claude/commands/`:

```markdown
# .claude/commands/meu-comando.md

# Meu Comando Personalizado

Fazer algo específico do meu projeto.

## Argumentos: $ARGUMENTS

[Sua implementação do comando]
```

## Recursos Incluídos

### Documentação (PRPs/ai_docs/)

- `cc_base.md` - Documentação principal do Claude Code
- `cc_actions_sdk.md` - Integração GitHub Actions e SDK
- `cc_best_practices.md` - Guia de melhores práticas
- `cc_settings.md` - Configuração e segurança
- `cc_tutorials.md` - Tutoriais passo a passo

### Templates (PRPs/templates/)

- `prp_base.md` - Template PRP abrangente com validação
- `prp_spec.md` - Template de especificação
- `prp_planning_base.md` - Template de planejamento com diagramas

### Exemplo de PRP

- `example-from-workshop-mcp-crawl4ai-refactor-1.md` - Exemplo de refatoração do mundo real

## Licença

Licença MIT

## Suporte

Passei um tempo considerável criando esses recursos e prompts. Se você encontrar valor neste projeto, considere pagar-me um café para apoiar meu trabalho.

👉 **Pague-me um café:** https://coff.ee/wirasm

---

Lembre-se: O objetivo é sucesso de implementação em uma tentativa através de contexto abrangente. Boa codificação com Claude Code!
