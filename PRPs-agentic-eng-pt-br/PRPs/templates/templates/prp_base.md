name: "Template Base PRP v3 - Focado em Implementação com Padrões de Precisão"
description: |

---

## Objetivo

**Meta da Funcionalidade**: [Estado final específico e mensurável do que precisa ser construído]

**Entregável**: [Artefato concreto - endpoint de API, classe de serviço, integração, etc.]

**Definição de Sucesso**: [Como você saberá que isso está completo e funcionando]

## Persona do Usuário (se aplicável)

**Usuário Alvo**: [Tipo específico de usuário - desenvolvedor, usuário final, admin, etc.]

**Caso de Uso**: [Cenário principal quando esta funcionalidade será usada]

**Jornada do Usuário**: [Fluxo passo a passo de como o usuário interage com esta funcionalidade]

**Pontos de Dor Resolvidos**: [Frustrações específicas do usuário que esta funcionalidade resolve]

## Por que

- [Valor de negócio e impacto no usuário]
- [Integração com funcionalidades existentes]
- [Problemas que isso resolve e para quem]

## O que

[Comportamento visível ao usuário e requisitos técnicos]

### Critérios de Sucesso

- [ ] [Resultados específicos e mensuráveis]

## Todo o Contexto Necessário

### Verificação de Completude do Contexto

_Antes de escrever este PRP, valide: "Se alguém não soubesse nada sobre esta base de código, teria tudo o que é necessário para implementar isso com sucesso?"_

### Documentação e Referências

```yaml
# DEVE LER - Inclua estes na sua janela de contexto
- url: [URL completa com âncora de seção]
  why: [Métodos/conceitos específicos necessários para implementação]
  critical: [Insights-chave que previnem erros comuns de implementação]

- file: [caminho/exato/para/arquivo/padrão.py]
  why: [Padrão específico a seguir - estrutura de classe, tratamento de erro, etc.]
  pattern: [Breve descrição de qual padrão extrair]
  gotcha: [Restrições ou limitações conhecidas a evitar]

- docfile: [PRPs/ai_docs/domain_specific.md]
  why: [Documentação personalizada para padrões complexos de biblioteca/integração]
  section: [Seção específica se o documento for grande]
```

### Árvore atual da base de código (execute `tree` na raiz do projeto) para obter uma visão geral da base de código

```bash

```

### Árvore desejada da base de código com arquivos a serem adicionados e responsabilidade do arquivo

```bash

```

### Peculiaridades Conhecidas da nossa base de código e Biblioteca

```python
# CRÍTICO: [Nome da biblioteca] requer [configuração específica]
# Exemplo: FastAPI requer funções async para endpoints
# Exemplo: Este ORM não suporta inserções em lote acima de 1000 registros
```

## Blueprint de Implementação

### Modelos de dados e estrutura

Crie os modelos de dados principais, garantimos segurança de tipos e consistência.

```python
Exemplos:
 - modelos orm
 - modelos pydantic
 - schemas pydantic
 - validadores pydantic

```

### Tarefas de Implementação (ordenadas por dependências)

```yaml
Tarefa 1: CRIAR src/models/{domain}_models.py
  - IMPLEMENTAR: Modelos Pydantic {SpecificModel}Request, {SpecificModel}Response
  - SEGUIR padrão: src/models/existing_model.py (abordagem de validação de campo)
  - NOMENCLATURA: CamelCase para classes, snake_case para campos
  - LOCALIZAÇÃO: Arquivo de modelo específico do domínio em src/models/

Tarefa 2: CRIAR src/services/{domain}_service.py
  - IMPLEMENTAR: Classe {Domain}Service com métodos async
  - SEGUIR padrão: src/services/database_service.py (estrutura de serviço, tratamento de erro)
  - NOMENCLATURA: Classe {Domain}Service, métodos async def create_*, get_*, update_*, delete_*
  - DEPENDÊNCIAS: Importar modelos da Tarefa 1
  - LOCALIZAÇÃO: Camada de serviço em src/services/

Tarefa 3: CRIAR src/tools/{action}_{resource}.py
  - IMPLEMENTAR: Wrapper de ferramenta MCP chamando métodos de serviço
  - SEGUIR padrão: src/tools/existing_tool.py (estrutura de ferramenta FastMCP)
  - NOMENCLATURA: nome de arquivo snake_case, nome descritivo da função da ferramenta
  - DEPENDÊNCIAS: Importar serviço da Tarefa 2
  - LOCALIZAÇÃO: Camada de ferramenta em src/tools/

Tarefa 4: MODIFICAR src/main.py ou src/server.py
  - INTEGRAR: Registrar nova ferramenta com servidor MCP
  - ENCONTRAR padrão: registros de ferramentas existentes
  - ADICIONAR: Importar e registrar nova ferramenta seguindo padrão existente
  - PRESERVAR: Registros de ferramentas existentes e configuração do servidor

Tarefa 5: CRIAR src/services/tests/test_{domain}_service.py
  - IMPLEMENTAR: Testes unitários para todos os métodos de serviço (caminho feliz, casos extremos, tratamento de erro)
  - SEGUIR padrão: src/services/tests/test_existing_service.py (uso de fixture, padrões de asserção)
  - NOMENCLATURA: nomenclatura de função test_{method}_{scenario}
  - COBERTURA: Todos os métodos públicos com casos de teste positivos e negativos
  - LOCALIZAÇÃO: Testes junto ao código que eles testam

Tarefa 6: CRIAR src/tools/tests/test_{action}_{resource}.py
  - IMPLEMENTAR: Testes unitários para funcionalidade de ferramenta MCP
  - SEGUIR padrão: src/tools/tests/test_existing_tool.py (abordagem de teste de ferramenta MCP)
  - MOCK: Dependências de serviço externo
  - COBERTURA: Validação de entrada da ferramenta, respostas de sucesso, tratamento de erro
  - LOCALIZAÇÃO: Testes de ferramenta em src/tools/tests/
```

### Padrões de Implementação e Detalhes-Chave

```python
# Mostrar padrões críticos e peculiaridades - mantenha conciso, foque em detalhes não óbvios

# Exemplo: Padrão de método de serviço
async def {domain}_operation(self, request: {Domain}Request) -> {Domain}Response:
    # PADRÃO: Validação de entrada primeiro (seguir src/services/existing_service.py)
    validated = self.validate_request(request)

    # PECULIARIDADE: [Restrição específica da biblioteca ou requisito]
    # PADRÃO: Abordagem de tratamento de erro (referenciar padrão de serviço existente)
    # CRÍTICO: [Requisito não óbvio ou detalhe de configuração]

    return {Domain}Response(status="success", data=result)

# Exemplo: Padrão de ferramenta MCP
@app.tool()
async def {tool_name}({parameters}) -> str:
    # PADRÃO: Validação de ferramenta e delegação de serviço (ver src/tools/existing_tool.py)
    # RETORNAR: String JSON com formato de resposta padronizado
```

### Pontos de Integração

```yaml
BANCO DE DADOS:
  - migration: "Adicionar coluna 'feature_enabled' à tabela users"
  - index: "CREATE INDEX idx_feature_lookup ON users(feature_id)"

CONFIG:
  - adicionar a: config/settings.py
  - padrão: "FEATURE_TIMEOUT = int(os.getenv('FEATURE_TIMEOUT', '30'))"

ROTAS:
  - adicionar a: src/api/routes.py
  - padrão: "router.include_router(feature_router, prefix='/feature')"
```

## Loop de Validação

### Nível 1: Sintaxe e Estilo (Feedback Imediato)

```bash
# Execute após cada criação de arquivo - corrija antes de prosseguir
ruff check src/{new_files} --fix     # Auto-formatação e correção de problemas de linting
mypy src/{new_files}                 # Verificação de tipos com arquivos específicos
ruff format src/{new_files}          # Garantir formatação consistente

# Validação em todo o projeto
ruff check src/ --fix
mypy src/
ruff format src/

# Esperado: Zero erros. Se existirem erros, LEIA a saída e corrija antes de prosseguir.
```

### Nível 2: Testes Unitários (Validação de Componente)

```bash
# Teste cada componente conforme é criado
uv run pytest src/services/tests/test_{domain}_service.py -v
uv run pytest src/tools/tests/test_{action}_{resource}.py -v

# Suíte completa de testes para áreas afetadas
uv run pytest src/services/tests/ -v
uv run pytest src/tools/tests/ -v

# Validação de cobertura (se ferramentas de cobertura disponíveis)
uv run pytest src/ --cov=src --cov-report=term-missing

# Esperado: Todos os testes passam. Se falhando, depurar causa raiz e corrigir implementação.
```

### Nível 3: Teste de Integração (Validação do Sistema)

```bash
# Validação de inicialização do serviço
uv run python main.py &
sleep 3  # Permitir tempo de inicialização

# Validação de verificação de saúde
curl -f http://localhost:8000/health || echo "Verificação de saúde do serviço falhou"

# Teste de endpoint específico da funcionalidade
curl -X POST http://localhost:8000/{your_endpoint} \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}' \
  | jq .  # Imprimir resposta JSON formatada

# Validação do servidor MCP (se baseado em MCP)
# Testar funcionalidade da ferramenta MCP
echo '{"method": "tools/call", "params": {"name": "{tool_name}", "arguments": {}}}' | \
  uv run python -m src.main

# Validação do banco de dados (se integração de banco de dados)
# Verificar esquema do banco de dados, conexões, migrações
psql $DATABASE_URL -c "SELECT 1;" || echo "Conexão com banco de dados falhou"

# Esperado: Todas as integrações funcionando, respostas adequadas, sem erros de conexão
```

### Nível 4: Validação Criativa e Específica do Domínio

```bash
# Exemplos de Validação do Servidor MCP:

# Playwright MCP (para interfaces web)
playwright-mcp --url http://localhost:8000 --test-user-journey

# Docker MCP (para serviços containerizados)
docker-mcp --build --test --cleanup

# Database MCP (para operações de dados)
database-mcp --validate-schema --test-queries --check-performance

# Validação de Lógica de Negócio Personalizada
# [Adicionar comandos de validação específicos do domínio aqui]

# Teste de Performance (se requisitos de performance)
ab -n 100 -c 10 http://localhost:8000/{endpoint}

# Varredura de Segurança (se requisitos de segurança)
bandit -r src/

# Teste de Carga (se requisitos de escalabilidade)
# wrk -t12 -c400 -d30s http://localhost:8000/{endpoint}

# Validação de Documentação de API (se endpoints de API)
# swagger-codegen validate -i openapi.json

# Esperado: Todas as validações criativas passam, performance atende aos requisitos
```

## Lista de Verificação Final de Validação

### Validação Técnica

- [ ] Todos os 4 níveis de validação completados com sucesso
- [ ] Todos os testes passam: `uv run pytest src/ -v`
- [ ] Sem erros de linting: `uv run ruff check src/`
- [ ] Sem erros de tipo: `uv run mypy src/`
- [ ] Sem problemas de formatação: `uv run ruff format src/ --check`

### Validação da Funcionalidade

- [ ] Todos os critérios de sucesso da seção "O que" atendidos
- [ ] Teste manual bem-sucedido: [comandos específicos do Nível 3]
- [ ] Casos de erro tratados graciosamente com mensagens de erro adequadas
- [ ] Pontos de integração funcionam conforme especificado
- [ ] Requisitos da persona do usuário satisfeitos (se aplicável)

### Validação da Qualidade do Código

- [ ] Segue padrões e convenções de nomenclatura existentes da base de código
- [ ] Colocação de arquivo corresponde à estrutura da árvore da base de código desejada
- [ ] Anti-padrões evitados (verificar contra seção Anti-Padrões)
- [ ] Dependências adequadamente gerenciadas e importadas
- [ ] Mudanças de configuração adequadamente integradas

### Documentação e Implantação

- [ ] Código é auto-documentado com nomes claros de variáveis/funções
- [ ] Logs são informativos mas não verbosos
- [ ] Variáveis de ambiente documentadas se novas forem adicionadas

---

## Anti-Padrões a Evitar

- ❌ Não criar novos padrões quando os existentes funcionam
- ❌ Não pular validação porque "deveria funcionar"
- ❌ Não ignorar testes falhando - corrija-os
- ❌ Não usar funções sync em contexto async
- ❌ Não codificar valores que deveriam ser configuração
- ❌ Não capturar todas as exceções - seja específico
