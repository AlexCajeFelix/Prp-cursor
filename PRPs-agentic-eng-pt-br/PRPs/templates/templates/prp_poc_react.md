name: "Template POC React v1 - Desenvolvimento Rápido de Protótipo"
description: |
Otimizado para criar POCs e protótipos baseados em React do zero.
Foca na validação de conceito sobre qualidade de produção.
Projetado para criação de POC paralela (10+ simultâneas).
Apenas frontend com dados simulados.
Abordagem "funcionando sobre excelente" para iteração rápida.

---

## Objetivo

**Meta do POC**: [Conceito específico a validar - ex: "Dashboard interativo para visualização de dados"]

**Entregável**: [Artefato React concreto - componente, página, fluxo do usuário, demo de integração]

**Definição de Sucesso**: [Como você saberá que o conceito foi validado - ex: "Stakeholders podem navegar pelo fluxo principal com dados realistas"]

## Escopo e Limitações do POC

**Nível de Fidelidade**: [Demo/MVP]

- **Demo**: UI polida para apresentações de stakeholders
- **MVP**: Qualidade próxima à produção para teste de usuário

**Deve Ter**: [Funcionalidade principal que prova o conceito]

- [ ] [Interação principal do usuário funciona]
- [ ] [Dados principais exibidos corretamente com dados simulados]
- [ ] [Fluxo crítico do usuário é navegável]

**Seria Bom Ter**: [Funcionalidades que aprimoram mas não são críticas]

- [ ] [Interações secundárias]
- [ ] [Polimento visual aprimorado]
- [ ] [Fluxos/personas de usuário adicionais]

**Não Terá**: [Explicitamente excluído para manter o foco]

- [ ] [Integração de API real]
- [ ] [Tratamento complexo de erro]
- [ ] [Otimização de performance]
- [ ] [Teste abrangente]

## Por que

**Necessidade de Validação de Conceito**: [Que hipótese você está testando?]

**Pergunta de Experiência do Usuário**: [Que suposição de UX precisa de validação?]

**Viabilidade Técnica**: [Que abordagem técnica precisa ser comprovada?]

**Valor de Negócio**: [Como este POC impulsiona a tomada de decisão?]

## O que

**Jornada Principal do Usuário**: [Fluxo principal passo a passo para demonstrar]

1. [Ação do usuário/carregamento de página]
2. [Interação do usuário com dados/UI]
3. [Resposta do sistema/navegação]
4. [Estado de resultado/conclusão]

**Interações-Chave**: [Interações críticas do usuário que validam o conceito]

- [Tipo de interação]: [Comportamento esperado com dados simulados]
- [Elemento de UI]: [Feedback do usuário/resposta do sistema]

**Requisitos Visuais**: [Necessidades de UI/UX para validação efetiva de conceito]

- [Requisitos de layout/componente]
- [Necessidades de visualização de dados]
- [Especificações de elementos interativos]

### Critérios de Sucesso

- [ ] **Fluxo Principal Completo**: Jornada principal do usuário funciona de ponta a ponta com dados simulados
- [ ] **Interações-Chave Funcionais**: Interações críticas demonstram o conceito claramente
- [ ] **Pronto para Stakeholders**: POC pode ser demonstrado para tomadores de decisão
- [ ] **Validação de Conceito**: Hipótese pode ser testada com interações realistas do usuário
- [ ] **Documentação Completa**: Pressupostos, limitações e próximos passos documentados

## Todo o Contexto Necessário (Otimizado para POC)

### Verificação de Completude do Contexto

_Para desenvolvimento de POC: "Este contexto permite construir um protótipo funcional que valida o conceito principal?"_

### Stack Tecnológico React

```yaml
# Requisitos da Stack Tecnológica Atual
framework: [React 19/Next.js 15/Vite]
styling: [Tailwind CSS/CSS Modules/styled-components]
components: [shadcn/ui/Material-UI/componentes customizados]
typescript: [Modo strict/Tipos básicos/validação Zod]
testing: [React Testing Library/Vitest/Jest]

# Escolhas Específicas do POC
mock_data: [MSW/JSON estático/faker.js]
data_pattern: [Simulação de API REST/mocks GraphQL/objetos estáticos]
state_management: [useState/useReducer/Zustand (se complexo)]
routing: [React Router/Next.js router/roteamento hash]
```

### Estratégia de Dados Simulados

```yaml
# Abordagem Principal de Mock
strategy: [MSW com faker.js/Arquivos JSON estáticos/Objetos hardcoded]
complexity: [Objetos simples/Dados relacionais/Estruturas aninhadas complexas]
volume:
  [Dataset pequeno para demos/Médio para teste realista/Grande para performance]

# Requisitos de Dados
entities: [Listar modelos de dados principais - User, Product, Order, etc.]
relationships: [Como entidades se conectam - um-para-muitos, muitos-para-muitos]
realistic_data:
  [Usar faker.js/Conteúdo placeholder realista/Exemplos específicos do domínio]
```

### Exemplos Similares e Padrões (Se Disponível)

```yaml
# DEVE LER - Inclua estes na sua janela de contexto
- file: [caminho/para/componente/similar.tsx]
  why: [Padrão de estrutura de componente a seguir]
  adapt: [O que modificar para o escopo do POC]
  critical: [Padrões-chave que previnem erros comuns do React]

- url: [URL de documentação React com seção específica]
  why: [Hooks/padrões específicos necessários para implementação]
  critical: [Melhores práticas para prototipagem rápida]

- example: [Link para POC ou demo similar]
  why: [Inspiração de padrão UI/UX]
  adapt: [Como customizar para seu conceito]
```

### Contexto do Projeto e Limitações

```yaml
# Ambiente de Desenvolvimento
package_manager: [npm]
build_tool: [Vite]
dev_server: [3212]


# Convenção de Estrutura de Arquivo
poc_directory: [/poc-{name}/src/poc-{name}//demos/{name}]
component_pattern: [PascalCase/kebab-case/convenção do projeto existente]
```

## Blueprint de Implementação

### Arquitetura do POC

```
/poc-{name}/
├── components/           # Componentes UI principais
│   ├── ui/              # Elementos UI reutilizáveis
│   ├── features/        # Componentes específicos da funcionalidade
│   └── layout/          # Componentes de layout
├── hooks/               # Hooks personalizados para dados/estado
│   ├── useMockData.ts   # Busca de dados simulados
│   └── usePocState.ts   # Estado específico do POC
├── data/                # Dados simulados e handlers
│   ├── mocks/           # Dados simulados estáticos
│   ├── handlers/        # Handlers de request MSW
│   └── schemas/         # Tipos TypeScript
├── pages/               # Páginas/rotas principais do POC
│   ├── index.tsx        # Ponto de entrada
│   └── demo/            # Páginas de demo principais
├── styles/              # Estilização específica do POC
├── tests/               # Testes básicos de fumaça
└── README.md            # Documentação do POC
```

### Tarefas de Implementação

**Tarefa 1: CRIAR fundação poc-{name}**

- CONFIGURAR: Estrutura do projeto React no diretório designado
- CONFIGURAR: Config TypeScript, regras de linting, dependências básicas
- INSTALAR: Pacotes necessários (MSW, faker.js, biblioteca UI, etc.)
- SIMULAR: Estrutura de dados inicial e configuração MSW
- LOCALIZAÇÃO: Seguir convenções de diretório do projeto
- DOCUMENTAR: Escopo do POC e instruções de configuração

**Tarefa 2: CRIAR sistema de dados simulados**

- IMPLEMENTAR: Geração de dados simulados com faker.js ou dados estáticos
- SEGUIR: Padrões de modelagem de dados do projeto (se existentes)
- CRIAR: Handlers MSW para simulação de API
- TIPOS: Interfaces TypeScript para todos os modelos de dados
- VALIDAR: Dados simulados cobrem todos os cenários de usuário do POC

**Tarefa 3: CRIAR componentes UI principais**

- IMPLEMENTAR: Componentes UI principais do POC com TypeScript
- SEGUIR: Padrões de componente existentes e convenções de nomenclatura
- ESTILIZAR: Estilização de componente seguindo padrões do projeto
- PROPS: Interfaces TypeScript adequadas para todas as props
- RESPONSIVO: Design responsivo básico para mobile (se necessário)

**Tarefa 4: CRIAR páginas de fluxo do usuário**

- IMPLEMENTAR: Páginas principais para jornada principal do usuário
- CONECTAR: Componentes com hooks de dados simulados
- NAVEGAR: Roteamento entre telas do POC
- ESTADO: Gerenciamento de estado de interação do usuário
- DEMO: Experiência completa do usuário no caminho feliz

**Tarefa 5: CRIAR interações básicas**

- IMPLEMENTAR: Interações principais do usuário (cliques, formulários, navegação)
- MANIPULAR: Submissões de formulário com respostas simuladas
- FEEDBACK: Feedback do usuário para interações (estados de carregamento, confirmações)
- ERRO: Error boundaries básicos para prevenção de crashes
- ACESSIBILIDADE: Labels ARIA básicos e navegação por teclado

**Tarefa 6: CRIAR validação e documentação**

- IMPLEMENTAR: Testes básicos de fumaça para funcionalidade principal
- VALIDAR: Teste manual do fluxo completo do usuário
- DOCUMENTAR: Pressupostos, limitações e descobertas do POC
- DEMO: Notas de preparação para apresentações de stakeholders
- PRÓXIMO: Recomendações para implementação de produção

## Loop de Validação (Otimizado para POC)

### Nível 1: Sintaxe e Build (Feedback Imediato)

```bash
# Validação TypeScript e linting
npm run lint                     # ESLint com regras React/TS
npx tsc --noEmit                # Verificação de tipos sem build
npm run format                   # Formatação Prettier

# Validação de build
npm run build                    # Build de produção bem-sucedido
npm run analyze                  # Análise de tamanho de bundle (se disponível)

# Esperado: Zero erros TypeScript, build bem-sucedido, tamanho de bundle razoável
```

### Nível 2: Validação de Demo (Experiência do Usuário)

```bash
# Servidor de desenvolvimento
npm run dev                      # Servidor dev inicia com sucesso
# Lista de verificação de validação manual:
# ✓ POC carrega sem erros
# ✓ Fluxo principal do usuário navegável
# ✓ Interações-chave funcionam com dados simulados
# ✓ UI renderiza corretamente em desktop/mobile
# ✓ Dados simulados exibem realisticamente

# Teste automatizado básico
npm test                         # Testes de fumaça passam
npm test -- --coverage           # Relatório básico de cobertura

# Screenshot/gravação para stakeholders
# Documentar quaisquer problemas ou limitações descobertas
```

### Nível 3: Validação de Conceito (Stakeholder e Negócio)

```bash
# Preparação de demo para stakeholders
# ✓ Script de demo preparado com pontos-chave de discussão
# ✓ Cenários de dados simulados cobrem casos de uso realistas
# ✓ Limitações conhecidas documentadas e comunicadas
# ✓ Próximos passos e requisitos de produção identificados

# Coleta de feedback
# ✓ Sessão de feedback de stakeholders realizada
# ✓ Reação/entendimento do usuário avaliado
# ✓ Perguntas de validação de conceito respondidas
# ✓ Critérios de tomada de decisão avaliados

# Documentação e próximos passos
# ✓ Descobertas do POC documentadas
# ✓ Requisitos de implementação de produção identificados
# ✓ Ações de acompanhamento definidas
```

## Lista de Verificação Final de Validação

### Completude Técnica

- [ ] **Modo Strict TypeScript**: Todos os componentes e dados adequadamente tipados
- [ ] **Dados Simulados Realistas**: Cenários de dados representam uso do mundo real
- [ ] **Estrutura de Componente**: Seguindo melhores práticas React e convenções do projeto
- [ ] **Processo de Build**: POC constrói e executa sem erros
- [ ] **Teste Básico**: Funcionalidade principal tem testes de fumaça

### Completude da Funcionalidade

- [ ] **Fluxo Principal do Usuário**: Jornada completa ponta a ponta funciona
- [ ] **Interações-Chave**: Interações críticas do usuário demonstram conceito
- [ ] **Clareza Visual**: UI comunica claramente o conceito sendo validado
- [ ] **Integração de Dados**: Integração de dados simulados mostra uso realista
- [ ] **Tratamento de Erro**: Error boundaries básicos previnem crashes

### Validação de Negócio

- [ ] **Conceito Demonstrado**: Hipótese principal pode ser avaliada
- [ ] **Pronto para Stakeholders**: POC pronto para revisão de tomadores de decisão
- [ ] **Limitações Claras**: Restrições conhecidas claramente documentadas
- [ ] **Próximos Passos Definidos**: Requisitos de produção identificados
- [ ] **Critérios de Sucesso Atendidos**: Todas as metas originais do POC alcançadas

## Anti-Padrões do POC

### Anti-Padrões de Implementação

- ❌ **Não super-engenheirar**: Pular padrões de arquitetura complexos para POC
- ❌ **Não implementar tratamento completo de erro**: Focar na demonstração do caminho feliz
- ❌ **Não criar suítes abrangentes de teste**: Apenas testes básicos de fumaça
- ❌ **Não otimizar para performance**: Funcionalidade sobre otimização
- ❌ **Não integrar APIs reais**: Dados simulados exclusivamente
- ❌ **Não construir funcionalidades de produção**: Implementação apenas no nível de protótipo

### Anti-Padrões de Processo

- ❌ **Não expandir escopo durante desenvolvimento**: Manter itens "Deve Ter" definidos
- ❌ **Não perfeccionar a UI**: Bom o suficiente para validação de conceito
- ❌ **Não implementar casos extremos**: Focar na jornada principal do usuário
- ❌ **Não construir para escalabilidade**: Focado em demo, usuário único

### Anti-Padrões de Comunicação

- ❌ **Não apresentar como pronto para produção**: Expectativas claras de POC
- ❌ **Não esconder limitações**: Transparente sobre o que é simulado/limitado
- ❌ **Não prometer cronogramas específicos**: Descobertas do POC informam estimativas
- ❌ **Não pular documentação**: Desenvolvedores futuros precisam de contexto

### FOQUE EM

- ✅ **Validação de conceito**: Stakeholders podem avaliar a ideia principal?
- ✅ **Demonstração da jornada do usuário**: Fluxo principal funciona ponta a ponta
- ✅ **Clareza do conceito visual**: UI comunica efetivamente o conceito
- ✅ **Cenários de dados realistas**: Dados simulados representam uso atual
- ✅ **Iteração rápida**: Priorizar velocidade de desenvolvimento e ciclos de feedback
- ✅ **Clareza de limitações**: Documentar pressupostos e restrições
- ✅ **Clareza de próximos passos**: Requisitos e recomendações de produção

## Considerações de POC Paralelo

### Identificação Única

- **Convenção de Nomenclatura**: `poc-{feature}-{variant}` (ex: poc-dashboard-minimal, poc-dashboard-advanced)
- **Estrutura de Diretório**: Diretório isolado por POC para prevenir conflitos
- **Estratégia Git**: Branches ou worktrees separados para desenvolvimento paralelo

### Recursos Compartilhados

- **Padrões de Dados Simulados**: Estratégias comuns de geração de dados simulados

---

**Lembre-se**: Este template otimiza para **validação rápida de conceito** sobre **qualidade de produção**. O objetivo é provar conceitos rapidamente e informar decisões de desenvolvimento de produção, não construir código pronto para produção.
