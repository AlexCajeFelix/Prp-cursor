# Conceito de Product Requirement Prompt (PRP)

"Especificar demais o que construir enquanto subespecifica o contexto e como construir é por que tantas tentativas de codificação orientadas por IA param em 80%. Um Product Requirement Prompt (PRP) resolve isso fundindo o escopo disciplinado de um Documento de Requisitos de Produto (PRD) clássico com a mentalidade 'contexto-é-rei' da engenharia de prompt moderna."

## O que é um PRP?

Product Requirement Prompt (PRP - Prompt de Requisitos de Produto)
Um PRP é um prompt estruturado que fornece a um agente de codificação de IA tudo o que ele precisa para entregar uma fatia vertical de software funcionando—nem mais, nem menos.

### Como difere de um PRD

Um PRD tradicional esclarece o que o produto deve fazer e por que os clientes precisam dele, mas deliberadamente evita como será construído.

Um PRP mantém as seções de objetivo e justificativa de um PRD, mas adiciona três camadas críticas para IA:

### Contexto

- Caminhos e conteúdo precisos de arquivos, versões de biblioteca e contexto de biblioteca, exemplos de snippets de código. LLMs geram código de maior qualidade quando recebem referências diretas no prompt em vez de descrições amplas. Uso de um diretório ai_docs/ para inserir documentação de biblioteca e outros docs.

### Detalhes e Estratégia de Implementação

- Ao contrário de um PRD tradicional, um PRP declara explicitamente como o produto será construído. Isso inclui o uso de endpoints de API, executores de teste ou padrões de agente (ReAct, Plan-and-Execute) a serem usados. Uso de typehints, dependências, padrões arquiteturais e outras ferramentas para garantir que o código seja construído corretamente.

### Portões de Validação

- Verificações determinísticas como pytest, ruff ou passagens de tipo estático "Shift-left" - controles de qualidade capturam defeitos cedo e são mais baratos do que retrabalho tardio.
  Exemplo: Cada nova função deve ser testada individualmente, Portão de validação = todos os testes passam.

### Camada PRP - Por que Existe

- A pasta PRP é usada para preparar e canalizar PRPs para o codificador agêntico.

## Por que o contexto não é negociável

Saídas de large-language-model são limitadas por sua janela de contexto; contexto irrelevante ou ausente literalmente espreme tokens úteis

O mantra da indústria "Garbage In → Garbage Out" se aplica duplamente à engenharia de prompt e especialmente na engenharia agêntica: entrada desleixada gera código frágil

## Em Resumo

Um PRP é PRD + inteligência de codebase curada + agente/runbook—o pacote viável mínimo que uma IA precisa para plausivelmente entregar código pronto para produção na primeira tentativa.

O PRP pode ser pequeno e focando em uma única tarefa ou grande e cobrindo múltiplas tarefas.
O verdadeiro poder do PRP está na capacidade de encadear tarefas juntas em um PRP para construir, auto-validar e entregar funcionalidades complexas.
