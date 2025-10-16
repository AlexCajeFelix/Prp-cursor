# Guia de Fluxo de Trabalho Story PRP

## Visão Geral

O fluxo de trabalho Story PRP é uma abordagem simplificada para converter histórias de usuário/tarefas do Jira, Linear ou outras ferramentas de gerenciamento de projetos em planos de implementação executáveis. Ao contrário do fluxo abrangente Base PRP, os Story PRPs focam em implementação tática e orientada a tarefas.

## Diferenças-Chave dos Base PRPs

| Aspecto | Base PRP | Story PRP |
|---------|----------|-----------|
| **Escopo** | Funcionalidade/produto completo | História/tarefa única |
| **Contexto** | Documentação extensiva | Referências focadas |
| **Formato** | Blueprint detalhado | Lista de verificação de tarefas |
| **Validação** | 4 níveis abrangentes | Inline por tarefa |
| **Caso de Uso** | Novas funcionalidades, mudanças importantes | Tarefas de sprint, correção de bugs |

## Componentes do Fluxo de Trabalho

### 1. Template: `PRPs/templates/prp_story.md`
- Estrutura simplificada focada em tarefas de implementação
- Cada tarefa tem validação inline
- Sem seções extensivas de blueprint
- Formato direto e acionável

### 2. Comandos

#### `/prp-story-create {descrição da história}`
Cria um Story PRP:
- Analisando base de código para padrões e convenções
- Decompondo história em tarefas concretas
- Gerando comandos de validação
- Aproveitando subagentes especializados para análise paralela

#### `/prp-story-execute {arquivo_prp}`
Executa um Story PRP:
- Implementando tarefas sequencialmente
- Validando cada tarefa imediatamente
- Seguindo padrões descobertos exatamente
- Garantindo que todos os critérios de aceitação sejam atendidos

### 3. Subagentes Especializados

#### `@codebase-analyst`
- Análise profunda de padrões
- Descoberta de convenções
- Compreensão de arquitetura
- Extração de padrões de teste

#### `@library-researcher`
- Busca de documentação externa
- Busca de exemplos de implementação
- Pesquisa de melhores práticas
- Identificação de problemas conhecidos

## Exemplos de Uso

### Criando um Story PRP

```bash
# De uma história de usuário
/prp-story-create Como usuário, quero adicionar paginação à API de lista de produtos para que grandes conjuntos de resultados carreguem mais rápido

# De um relatório de bug
/prp-story-create BUG: Notificações por email não estão sendo enviadas quando usuários resetam sua senha

# De uma tarefa técnica
/prp-story-create Refatorar pool de conexão do banco de dados para usar gerenciadores de contexto async
```

### Executando um Story PRP

```bash
# Executar o PRP gerado
/prp-story-execute PRPs/story_add_pagination.md

# Ou usar o script runner
uv run PRPs/scripts/prp_runner.py --prp story_add_pagination --interactive
```

## Exemplos de Formato de Tarefa

### Tarefa CREATE
```markdown
### CREATE services/pagination_service.py:
- IMPLEMENTAR: PaginationService com método calculate_offset()
- PADRÃO: Seguir estrutura services/filter_service.py
- IMPORTS: from typing import Tuple; from math import ceil
- PECULIARIDADE: Tratar números de página negativos graciosamente
- **VALIDAR**: `python -c "from services.pagination_service import PaginationService; print('✓')"`
```

### Tarefa UPDATE
```markdown
### UPDATE api/products.py:
- ADICIONAR: parâmetros de paginação ao endpoint list_products
- ENCONTRAR: `async def list_products(request: Request):`
- INSERIR: `page: int = Query(1, ge=1), per_page: int = Query(20, le=100)`
- **VALIDAR**: `grep -q "page.*Query" api/products.py && echo "✓ Parâmetros adicionados"`
```

## Melhores Práticas

### Ao Criar Story PRPs

1. **Forneça Contexto Claro**: Inclua critérios de aceitação e quaisquer restrições
2. **Deixe os Agentes Analisarem**: Não pré-especifique detalhes de implementação
3. **Confie no Processo**: O sistema descobrirá padrões e convenções

### Ao Executar Story PRPs

1. **Execução Sequencial**: Complete tarefas em ordem
2. **Valide Imediatamente**: Execute validação após cada tarefa
3. **Siga Padrões**: Não crie novos padrões, use os existentes
4. **Corrija Para Frente**: Se validação falhar, corrija e continue

## Tipos Típicos de História

- **Adição de Funcionalidade**: Novos endpoints, serviços ou componentes
- **Correção de Bugs**: Correções direcionadas com cobertura de teste
- **Refatoração**: Melhorias de código mantendo comportamento
- **Integração**: Adicionando serviços ou bibliotecas de terceiros
- **Performance**: Tarefas de otimização com benchmarks
- **Segurança**: Adicionando autenticação, validação ou endurecimento

## Uso Avançado

### Análise Paralela
O comando create spawna múltiplos subagentes para analisar:
- Estrutura do projeto
- Implementações similares
- Documentação externa
- Padrões de teste

### Validação Customizada
Cada tarefa pode ter validação customizada além de comandos padrão:
- Teste de endpoint de API com curl
- Queries de verificação de banco de dados
- Benchmarks de performance
- Testes de integração

### Referências de Contexto
O sistema descobre e inclui automaticamente:
- Padrões relevantes da base de código
- Documentação externa
- Exemplos de configuração
- Padrões de teste

## Quando Usar Story PRPs vs Base PRPs

**Use Story PRPs para:**
- Tarefas de sprint e histórias de usuário
- Correção de bugs e funcionalidades pequenas
- Refatoração e otimização
- Tarefas com escopo claro

**Use Base PRPs para:**
- Novos produtos ou funcionalidades importantes
- Mudanças arquiteturais complexas
- Integrações multi-sistema
- Funcionalidades requerendo contexto extensivo

## Resolução de Problemas

**Problema**: Tarefas parecem muito alto-nível
**Solução**: Forneça critérios de aceitação mais específicos na história

**Problema**: Padrões errados detectados
**Solução**: Inclua dicas sobre qual parte da base de código referenciar

**Problema**: Comandos de validação falham
**Solução**: Verifique configuração do projeto, garanta dependências instaladas

## Exemplo de Saída

Veja `PRPs/story_add_rate_limiting_example.md` para um exemplo completo de um Story PRP gerado a partir de uma história de usuário sobre adicionar limitação de taxa a uma API.
