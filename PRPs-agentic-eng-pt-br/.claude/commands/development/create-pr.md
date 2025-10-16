# Criar Pull Request

Crie um pull request bem estruturado com descrição e contexto adequados.

## Título do PR (se fornecido)
$ARGUMENTS

## Processo

1. **Preparar Branch**
   ```bash
   # Verificar branch atual
   git branch --show-current
   
   # Garantir que não estamos na main
   # Se na main, criar uma branch de feature
   ```

2. **Revisar Mudanças**
   ```bash
   # Ver o que será incluído
   git status
   git diff main...HEAD
   ```

3. **Criar Commits**
   - Fazer stage de arquivos relevantes
   - Criar commits lógicos e atômicos se ainda não feito
   - Escrever mensagens de commit claras seguindo conventional commits, não inclua nenhuma referência ao claude, escrito por claude etc:
     - `feat:` para novas funcionalidades
     - `fix:` para correções de bugs
     - `docs:` para documentação
     - `test:` para testes
     - `refactor:` para refatoração

4. **Fazer Push para Remoto**
   ```bash
   git push -u origin HEAD
   ```

5. **Criar PR**
   ```bash
   gh pr create --title "$ARGUMENTS" --body "$(cat <<'EOF'
   ## Resumo
   [Breve descrição do que este PR faz]
   
   ## Mudanças
   - [Listar mudanças principais]
   - [Ser específico]
   
   ## Tipo de Mudança
   - [ ] Correção de bug
   - [ ] Nova funcionalidade
   - [ ] Mudança breaking
   - [ ] Atualização de documentação
   
   ## Testes
   - [ ] Testes passam localmente
   - [ ] Adicionados novos testes
   - [ ] Testes manuais completados
   
   ## Checklist
   - [ ] Código segue estilo do projeto
   - [ ] Auto-revisado
   - [ ] Documentação atualizada
   - [ ] Sem console.logs ou código de debug
   
   ## Screenshots (se aplicável)
   [Adicionar screenshots para mudanças de UI]
   
   ## Contexto Adicional
   [Qualquer informação extra que revisores devem saber]
   EOF
   )"
   ```

6. **Pós-Criação**
   - Adicionar labels se necessário: `gh pr edit --add-label "feature,needs-review"`
   - Solicitar revisores se conhecidos
   - Linkar issues relacionadas

Lembre-se de:
- Manter PRs focados e pequenos
- Fornecer contexto para revisores
- Testar completamente antes de criar PR
