---
name: commit
description: Analise mudanças e crie um commit git inteligente
arguments: "Instruções adicionais para o commit"
---

instruções adicionais = $ARGUMENTS

tipo = "feat", "fix", "docs", "style", "refactor", "perf", "test", "chore"

# Commit Git Inteligente

Por favor me ajude a criar um commit git:

1. Primeiro, verifique o status git atual e analise o que mudou:

```bash
git status
git diff --staged
```

2. Se nenhum arquivo estiver em stage, mostre-me as mudanças e me ajude a decidir o que fazer stage:

```bash
git diff
git status -s
```

3. Baseado nas mudanças, sugira:

- O tipo de commit apropriado (feat/fix/docs/style/refactor/perf/test/chore)
- Uma mensagem de commit concisa e descritiva seguindo conventional commits
- Se as mudanças forem complexas, sugira dividir em múltiplos commits

4. O formato do commit deve ser:

$tipo: descrição para commits simples
Para mudanças complexas, inclua um corpo explicando o que e por quê

5. Depois de me mostrar a mensagem de commit sugerida, pergunte se eu quero:

- Usar como está
- Modificar
- Adicionar mais detalhes ao corpo
- Fazer stage de arquivos diferentes

6. Uma vez aprovado, crie o commit e mostre-me o resultado.

7. Finalmente, pergunte se eu quero fazer push ou criar um PR.
