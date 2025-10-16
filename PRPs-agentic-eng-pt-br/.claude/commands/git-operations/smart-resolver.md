Realize uma resolução inteligente de conflitos de merge com entendimento profundo de nossa codebase.

## Análise pré-resolução:

1. Entenda o que cada branch estava tentando alcançar:
git log --oneline origin/main..HEAD
git log --oneline HEAD..origin/main

2. Verifique se há issues ou PRs relacionados:
git log --grep="fix" --grep="feat" --oneline -20
- Use o github cli conforme necessário

3. Identifique o tipo de conflitos (feature vs feature, fix vs refactor, etc.)

4. Pense com cuidado sobre suas descobertas e planeje adequadamente

## Estratégia de resolução:

### Para diferentes tipos de arquivo:

**Conflitos de código fonte (.js, .ts, .py, etc.)**:
- Entenda a lógica de negócio de ambas as mudanças
- Faça merge de ambas as features se forem complementares
- Se conflitantes, verifique qual tem melhor cobertura de testes
- Procure por arquivos relacionados que podem precisar atualizações

**Conflitos em arquivos de teste**:
- Geralmente faça merge de ambos os conjuntos de testes
- Garanta que não há nomes de teste duplicados
- Atualize descrições de teste se necessário

**Arquivos de configuração**:
- package.json: Faça merge de dependências, scripts
- .env.example: Inclua todas as novas variáveis
- Configs de CI/CD: Faça merge de todos os jobs a menos que duplicados

**Conflitos de documentação**:
- Faça merge de ambas as atualizações de documentação
- Garanta consistência na terminologia
- Atualize índice se necessário

**Arquivos de lock (package-lock.json, poetry.lock)**:
- Delete e regenere após resolver package.json/pyproject.toml

## Verificação pós-resolução:

1. Execute linters para verificar estilo de código
2. Execute verificadores de tipo se aplicável  
3. Execute suite de testes
4. Verifique por conflitos semânticos (código que faz merge mas quebra funcionalidade)
5. Verifique que nenhum código de debug foi deixado

## Passos finais:

1. Crie um resumo detalhado de todas as resoluções
2. Se alguma resolução for incerta, marque com comentários TODO
3. Sugira testes adicionais que podem ser necessários
4. Faça stage de todos os arquivos resolvidos

Comece analisando a situação atual de conflito com git status e entendendo ambas as branches.
