---
Destinado para tarefas Jira/GitHub ou outros sistemas de gerenciamento de tarefas para decompor e planejar a implementação.
---

# Template de Tarefa v2 - Denso em Informação com Loops de Validação

> Tarefas concisas e executáveis com contexto embutido e comandos de validação

## Formato

```
[AÇÃO] caminho/para/arquivo:
  - [OPERAÇÃO]: [DETALHES]
  - VALIDAR: [COMANDO]
  - SE_FALHAR: [DICA_DEBUG]
```

## Palavras-chave de ações para usar ao criar tarefas para descrições concisas e significativas

- **LER**: Entender padrões existentes
- **CRIAR**: Novo arquivo com conteúdo específico
- **ATUALIZAR**: Modificar arquivo existente
- **DELETAR**: Remover arquivo/código
- **ENCONTRAR**: Pesquisar por padrões
- **TESTAR**: Verificar comportamento
- **CORRIGIR**: Depurar e reparar

## Seção de Contexto Crítico

```yaml
# Inclua estes ANTES das tarefas quando o contexto é crucial
context:
  docs:
    - url: [Documentação da API]
      focus: [método/seção específica]

  patterns:
    - file: existing/example.py
      copy: [nome do padrão]

  gotchas:
    - issue: "Biblioteca X requer Y"
      fix: "Sempre fazer Z primeiro"
```

## Exemplos de Tarefas com Validação

### Tarefas de Configuração

```
LER src/config/settings.py:
  - ENTENDER: Estrutura de configuração atual
  - ENCONTRAR: Padrão de configuração do modelo
  - NOTAR: Config usa pydantic BaseSettings

LER tests/test_models.py:
  - ENTENDER: Padrão de teste para modelos
  - ENCONTRAR: Abordagem de configuração de fixture
  - NOTAR: Usa pytest-asyncio para testes async
```

### Tarefas de Implementação

````
ATUALIZAR caminho/para/arquivo:
  - ENCONTRAR: MODEL_REGISTRY = {
  - ADICIONAR: "new-model": NewModelClass,
  - VALIDAR: python -c "from caminho/para/arquivo import MODEL_REGISTRY; assert 'new-model' in MODEL_REGISTRY"
  - SE_FALHAR: Verificar declaração de import para NewModelClass

CRIAR caminho/para/arquivo:
  - COPIAR_PADRÃO: caminho/para/outro/arquivo
  - IMPLEMENTAR:
   - [Descrição detalhada do que precisa ser implementado baseado na inteligência da base de código]
  - VALIDAR: uv run pytest caminho/para/arquivo -v

ATUALIZAR caminho/para/arquivo:
  - ENCONTRAR: app.include_router(
  - ADICIONAR_APÓS:
    ```python
    from .endpoints import new_model_router
    app.include_router(new_model_router, prefix="/api/v1")
    ```
  - VALIDAR: uv run pytest caminho/para/arquivo -v
````

## Pontos de Verificação de Validação

```
CHECKPOINT sintaxe:
  - EXECUTAR: ruff check && mypy .
  - CORRIGIR: Quaisquer problemas reportados
  - CONTINUAR: Apenas quando limpo

CHECKPOINT testes:
  - EXECUTAR: uv run pytest caminho/para/arquivo -v
  - REQUERER: Todos passando
  - DEBUGAR: uv run pytest -vvs caminho/para/arquivo/teste_falhando.py
  - CONTINUAR: Apenas quando todos verdes

CHECKPOINT integração:
  - INICIAR: docker-compose up -d
  - EXECUTAR: ./scripts/integration_test.sh
  - ESPERAR: "Todos os testes passaram"
  - LIMPAR: docker-compose down
```

## Padrões de Debug

```
DEBUG erro_de_import:
  - VERIFICAR: Arquivo existe no caminho
  - VERIFICAR: __init__.py em todos os diretórios pai
  - TENTAR: python -c "import caminho/para/arquivo"
  - CORRIGIR: Adicionar ao PYTHONPATH ou corrigir import

DEBUG falha_de_teste:
  - EXECUTAR: uv run pytest -vvs caminho/para/teste.py::nome_do_teste
  - ADICIONAR: print(f"Debug: {variable}")
  - IDENTIFICAR: Problema de asserção vs implementação
  - CORRIGIR: Atualizar teste ou corrigir código

DEBUG erro_de_api:
  - VERIFICAR: Servidor rodando (ps aux | grep uvicorn)
  - TESTAR: curl http://localhost:8000/health
  - LER: Logs do servidor para stack trace
  - CORRIGIR: Baseado no erro específico
```

## Exemplos de tarefas comuns

### Adicionar Nova Funcionalidade

```
1. LER funcionalidade similar existente
2. CRIAR arquivo de nova funcionalidade (COPIAR padrão)
3. ATUALIZAR registro/router para incluir
4. CRIAR testes para funcionalidade
5. TESTAR todos os testes passam
6. CORRIGIR quaisquer problemas de linting/tipo
7. TESTAR integração funciona
```

### Corrigir Bug

```
1. CRIAR teste falhando que reproduz o bug
2. TESTAR confirmar teste falha
3. LER código relevante para entender
4. ATUALIZAR código com correção
5. TESTAR confirmar teste agora passa
6. TESTAR nenhum outro teste quebrado
7. ATUALIZAR changelog
```

### Refatorar Código

```
1. TESTAR testes atuais passam (baseline)
2. CRIAR nova estrutura (não deletar antiga ainda)
3. ATUALIZAR um uso para nova estrutura
4. TESTAR ainda passa
5. ATUALIZAR usos restantes incrementalmente
6. DELETAR estrutura antiga
7. TESTAR suíte completa passa
```

## Dicas para Tarefas Efetivas

- Use VALIDAR após cada mudança
- Inclua dicas SE_FALHAR para problemas comuns
- Referencie números de linha específicos ou padrões
- Mantenha comandos de validação simples e rápidos
- Encadeie tarefas relacionadas com dependências claras
- Sempre inclua passos de rollback/desfazer para mudanças arriscadas
