# Revisão de Código

Por favor, realize uma revisão abrangente de código das mudanças atuais ou arquivos especificados.

## Escopo da Revisão
$ARGUMENTS

## Processo de Revisão

1. **Entender Mudanças**
   - Se revisando mudanças staged: `git diff --staged`
   - Se revisando arquivos específicos: Ler os arquivos especificados
   - Se revisando um PR: `gh pr view $ARGUMENTS --json files,additions,deletions`
   - Se revisando um diretório local: `git diff $ARGUMENTS`
   - Se revisando a codebase inteira: `git diff origin/main`

## Áreas de Foco da Revisão

1. **Qualidade de Código**
   - Type hints em todas as funções e classes
   - Modelos Pydantic v2 para validação de dados
   - Sem declarações print() (use logging)
   - Tratamento de erro adequado
   - Seguindo PEP 8
   - Docstrings seguindo estilo google para python

2. **Padrões Pydantic v2**
   - Usando ConfigDict não class Config
   - field_validator não @validator
   - model_dump() não dict()
   - Uso adequado de tipos Annotated

3. **Segurança**
   - Validação de entrada em todos os endpoints
   - Sem vulnerabilidades de injeção SQL
   - Senhas adequadamente hasheadas
   - Sem secrets hardcoded

4. **Estrutura**
   - Testes unitários co-localizados com o código que testam em pastas tests/
   - Cada funcionalidade é autocontida com seus próprios models, service e tools
   - Componentes compartilhados são apenas coisas usadas por múltiplas funcionalidades
   - Melhorias futuras (como múltiplos provedores AI) iriam em src/shared/ai_providers/ quando implementadas
   - Testes de integração permanecem no nível raiz em tests/integration/

5. **Linting**
   - ruff check --fix
   - mypy

6. **Testes**
   - Novo código tem testes
   - Casos extremos cobertos
   - Mockando dependências externas

7. **Performance**
   - Sem queries N+1
   - Algoritmos eficientes
   - Uso adequado de async

8. **Documentação**
   - README claro com instruções de setup
   - CLAUDE.md atualizado com novos utils importantes, dependências etc para futuras instâncias do claude code

## Saída da Revisão

Crie um relatório de revisão conciso com:

```markdown
# Revisão de Código #[número]

## Resumo
[Visão geral de 2-3 frases]

## Problemas Encontrados

### 🔴 Crítico (Deve Corrigir)
- [Problema com arquivo:linha e correção sugerida]

### 🟡 Importante (Deveria Corrigir)
- [Problema com arquivo:linha e correção sugerida]

### 🟢 Menor (Considerar)
- [Sugestões de melhoria]

## Boas Práticas
- [O que foi feito bem]

## Cobertura de Testes
Atual: X% | Requerido: 80%
Testes ausentes: [lista]
Salve relatório em PRPs/code_reviews/review[#].md (verifique arquivos existentes primeiro)
```
