---
name: "Template PRP de História - Foco em Implementação de Tarefas"
description: "Template para converter histórias de usuário em tarefas de implementação executáveis"
---

## História Original

Cole aqui a história original compartilhada pelo usuário abaixo:

```
[Descrição de história/tarefa de usuário do Jira/Linear/etc]
```

## Metadados da História

**Tipo de História**: [Funcionalidade/Bug/Melhoria/Refatoração]
**Complexidade Estimada**: [Baixa/Média/Alta]
**Sistemas Principais Afetados**: [Lista de componentes/serviços principais]

---

## REFERÊNCIAS DE CONTEXTO

[Documentação e padrões descobertos automaticamente]

- {caminho_do_arquivo} - {Por que este padrão/arquivo é relevante}
- {caminho_doc} - {Seções específicas necessárias para implementação}
- {url_externa} - {Documentação de biblioteca ou exemplos}

---

## TAREFAS DE IMPLEMENTAÇÃO

[Blocos de tarefa em ordem de dependência - cada bloco é atômico e testável]

### Conceito Para tarefas

- Estamos usando palavras-chave densas em informação para ser específico e conciso sobre passos e detalhes de implementação.
- As tarefas devem ser detalhadas e específicas para garantir clareza e precisão.
- O desenvolvedor que executará as tarefas deve ser capaz de completar a tarefa usando apenas o contexto deste arquivo, com referências a caminhos de base de código relevantes e pontos de integração.

### {AÇÃO} {arquivo_alvo}:

- {VERBO/PALAVRA_CHAVE}: {Detalhe específico de implementação}
- {PADRÃO}: {Padrão existente a seguir da base de código}
- {IMPORTS}: {Imports ou dependências necessárias}
- {PECULIARIDADE}: {Problemas ou restrições conhecidas a evitar}
- **VALIDAR**: `{comando de validação executável}`

### Formato de Exemplo:

### CRIAR services/user_service.py:

- IMPLEMENTAR: Classe UserService com operações CRUD async
- PADRÃO: Seguir estrutura services/product_service.py
- IMPORTS: from models.user import User; from db import get_session
- PECULIARIDADE: Sempre usar gerenciador de contexto de sessão async
- **VALIDAR**: ` uv run python -c "from services.user_service import UserService; print('✓ Import bem-sucedido')"`

### ATUALIZAR api/routes.py:

- ADICIONAR: user_router ao router principal
- ENCONTRAR: `app.include_router(product_router)`
- INSERIR: `app.include_router(user_router, prefix="/users", tags=["users"])`
- **VALIDAR**: `grep -q "user_router" api/routes.py && echo "✓ Router adicionado"`

### ADICIONAR tests/

- CRIAR: tests/user_service_test.py
- IMPLEMENTAR: Casos de teste para classe UserService
- PADRÃO: Seguir estrutura tests/product_service_test.py
- IMPORTS: from services.user_service import UserService; from models.user import User; from db import get_session
- PECULIARIDADE: Usar gerenciador de contexto de sessão async em testes
- **VALIDAR**: `uv run python -m pytest tests/user_service_test.py && echo "✓ Testes passaram"`

---

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

Você pode usar CLI que estão instalados no sistema ou servidores MCP para estender a validação e loop de auto-fechamento.

Identifique se você está conectado a algum servidor MCP que pode ser usado para validação e se você tem alguma ferramenta cli instalada no sistema que pode ajudar com validação.

Por exemplo:

```bash
# Exemplos de Validação do Servidor MCP:

# Playwright MCP (para interfaces web)
playwright-mcp --url http://localhost:8000 --test-user-journey

# Docker MCP (para serviços containerizados)
docker-mcp --build --test --cleanup

# Database MCP (para operações de dados)
database-mcp --validate-schema --test-queries --check-performance
```

---

## LISTA DE VERIFICAÇÃO DE CONCLUSÃO

- [ ] Todas as tarefas completadas
- [ ] Validação de cada tarefa passou
- [ ] Suíte completa de testes passa
- [ ] Sem erros de linting
- [ ] Todos os portões de validação disponíveis passaram
- [ ] Critérios de aceitação da história atendidos

---

## Notas

[Qualquer contexto adicional, decisões tomadas ou itens de acompanhamento]

```
