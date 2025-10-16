# Conceito de Product Requirement Prompt (PRP)

"Sobre-especificar o que construir enquanto sub-especifica o contexto e como construí-lo é por isso que tantas tentativas de codificação impulsionadas por IA param em 80%. Um Product Requirement Prompt (PRP) corrige isso fundindo o escopo disciplinado de um Product Requirements Document (PRD) clássico com a mentalidade 'contexto-é-rei' da engenharia de prompt moderna."

## O que é um PRP?

Product Requirement Prompt (PRP)
Um PRP é um prompt estruturado que fornece a um agente de codificação de IA tudo o que ele precisa para entregar uma fatia vertical de software funcionando—nem mais, nem menos.

### Como difere de um PRD

Um PRD tradicional esclarece o que o produto deve fazer e por que os clientes precisam dele, mas deliberadamente evita como será construído.

Um PRP mantém as seções de objetivo e justificativa de um PRD, mas adiciona três camadas críticas para IA:

### Contexto

- Caminhos de arquivo precisos e conteúdo, versões de biblioteca e contexto de biblioteca, exemplos de trechos de código. LLMs geram código de maior qualidade quando recebem referências diretas in-prompt em vez de descrições amplas. Uso de um diretório ai_docs/ para canalizar documentação de biblioteca e outras docs.

### Detalhes e Estratégia de Implementação

- Ao contrário de um PRD tradicional, um PRP explicitamente declara como o produto será construído. Isso inclui o uso de endpoints de API, test runners ou padrões de agente (ReAct, Plan-and-Execute) a serem usados. Uso de typehints, dependências, padrões arquiteturais e outras ferramentas para garantir que o código seja construído corretamente.

### Portões de Validação

- Verificações determinísticas como pytest, ruff ou passagens de tipo estático. Controles de qualidade "Shift-left" capturam defeitos cedo e são mais baratos do que retrabalho tardio.
  Exemplo: Cada nova função deve ser testada individualmente, Portão de validação = todos os testes passam.

### Camada PRP Por Que Existe

- A pasta PRP é usada para preparar e canalizar PRPs para o codificador agêntico.

## Por que o contexto é inegociável

Saídas de modelos de linguagem grandes são delimitadas pela sua janela de contexto; contexto irrelevante ou ausente literalmente espreme tokens úteis para fora

O mantra da indústria "Garbage In → Garbage Out" se aplica duplamente à engenharia de prompt e especialmente na engenharia agêntica: entrada desleixada produz código frágil

## Em resumo

Um PRP é PRD + inteligência curada da base de código + agente/runbook—o pacote mínimo viável que uma IA precisa para plausivelmente entregar código pronto para produção na primeira tentativa.

O PRP pode ser pequeno e focando em uma única tarefa ou grande e cobrindo múltiplas tarefas.
O verdadeiro poder do PRP está na habilidade de encadear tarefas juntas em um PRP para construir, auto-validar e entregar funcionalidades complexas.
