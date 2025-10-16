name: "Template PRP de Planejamento - Geração de PRD com Diagramas"
description: |

## Propósito
Gerar Documentos de Requisitos de Produto (PRDs) abrangentes com diagramas visuais, transformando ideias em especificações detalhadas prontas para PRPs de implementação.

## Filosofia
1. **Pesquisa Primeiro**: Colete contexto antes de planejar
2. **Pensamento Visual**: Use diagramas para esclarecer conceitos
3. **Validação Integrada**: Inclua desafios e casos extremos
4. **Pronto para Implementação**: Saída alimenta diretamente outros PRPs

---

## Conceito Inicial
$ARGUMENTS

## Processo de Planejamento

### Fase 1: Expansão de Ideias e Pesquisa

#### Coleta de Contexto
```yaml
areas_de_pesquisa:
  analise_de_mercado:
    - concorrentes: [Pesquisar soluções similares]
    - necessidades_do_usuario: [Identificar pontos de dor]
    - tendencias: [Direções atuais da indústria]
  
  pesquisa_tecnica:
    - solucoes_existentes: [Como outros resolvem isso]
    - bibliotecas: [Ferramentas/frameworks disponíveis]
    - padroes: [Abordagens comuns de implementação]
  
  contexto_interno:
    - sistema_atual: [Como funciona hoje]
    - limitacoes: [Limitações técnicas/de negócio]
    - pontos_de_integracao: [Com o que deve funcionar]
```

#### Exploração Inicial
```
PESQUISAR soluções similares:
  - WEB_SEARCH: "exemplos de implementação {concept}"
  - WEB_SEARCH: "melhores práticas {concept}"
  - WEB_SEARCH: "padrões de arquitetura {concept}"

ANALISAR base de código existente:
  - ENCONTRAR: Funcionalidades similares já implementadas
  - IDENTIFICAR: Padrões a seguir
  - NOTAR: Restrições técnicas
```

### Fase 2: Geração da Estrutura do PRD

#### 1. Resumo Executivo
```markdown
## Declaração do Problema
[Articulação clara do problema sendo resolvido]

## Visão Geral da Solução
[Descrição de alto nível da solução proposta]

## Métricas de Sucesso
- Métrica 1: [Resultado mensurável]
- Métrica 2: [Resultado mensurável]
- KPI: [Indicador-chave de performance]
```

#### 2. Histórias de Usuário e Cenários
```markdown
## Fluxo Principal do Usuário
\```mermaid
graph LR
    A[Ação do Usuário] --> B{Ponto de Decisão}
    B -->|Caminho 1| C[Resultado 1]
    B -->|Caminho 2| D[Resultado 2]
    D --> E[Estado Final]
    C --> E
\```

## Histórias de Usuário
1. **Como um [tipo de usuário]**, eu quero [ação] para que [benefício]
   - Critérios de Aceitação:
     - [ ] Critério 1
     - [ ] Critério 2
   - Casos Extremos:
     - [Caso extremo 1]
     - [Caso extremo 2]
```

#### 3. Arquitetura do Sistema
```markdown
## Arquitetura de Alto Nível
\```mermaid
graph TB
    subgraph "Frontend"
        UI[Interface do Usuário]
        State[Gerenciamento de Estado]
    end
    
    subgraph "Backend"
        API[Camada de API]
        BL[Lógica de Negócio]
        DB[(Banco de Dados)]
    end
    
    subgraph "Externo"
        EXT[Serviços Externos]
    end
    
    UI --> API
    API --> BL
    BL --> DB
    BL --> EXT
    State --> UI
\```

## Quebra de Componentes
- **Componentes Frontend**:
  - [Componente 1]: [Propósito]
  - [Componente 2]: [Propósito]

- **Serviços Backend**:
  - [Serviço 1]: [Propósito]
  - [Serviço 2]: [Propósito]

- **Modelos de Dados**:
  - [Modelo 1]: [Campos e relacionamentos]
  - [Modelo 2]: [Campos e relacionamentos]
```

#### 4. Especificações Técnicas
```markdown
## Design de API
\```mermaid
sequenceDiagram
    participant U as Usuário
    participant F as Frontend
    participant A as API
    participant D as Banco de Dados
    participant E as Serviço Externo
    
    U->>F: Inicia Ação
    F->>A: POST /api/endpoint
    A->>D: Consultar Dados
    D-->>A: Retornar Dados
    A->>E: Chamar API Externa
    E-->>A: Resposta
    A-->>F: Resultado Processado
    F-->>U: Exibir Resultado
\```

## Endpoints
- **POST /api/[recurso]**
  - Request: `{campo1: tipo, campo2: tipo}`
  - Response: `{status: string, data: {...}}`
  - Erros: `400 Bad Request`, `401 Unauthorized`

## Fluxo de Dados
\```mermaid
flowchart TD
    A[Dados de Entrada] --> B{Validação}
    B -->|Válido| C[Processamento]
    B -->|Inválido| D[Resposta de Erro]
    C --> E[Transformar]
    E --> F[Armazenar]
    F --> G[Retornar Sucesso]
\```
```

#### 5. Estratégia de Implementação
```markdown
## Fases de Desenvolvimento
\```mermaid
graph LR
    A[Fundamento] --> B[Funcionalidades Principais]
    B --> C[Integração]
    C --> D[Teste]
    D --> E[Implantação]
    
    A -.- F[Esquema do Banco de Dados<br/>Framework de API<br/>Autenticação]
    B -.- G[Lógica de Negócio<br/>Endpoints de API<br/>UI Básica]
    C -.- H[Serviços Externos<br/>Integração Completa de UI<br/>Tratamento de Erro]
    D -.- I[Testes Unitários<br/>Testes de Integração<br/>Testes de Performance]
    E -.- J[Documentação<br/>Monitoramento<br/>Lançamento]
\```

## Prioridade de Implementação
1. **Fundamento**: Infraestrutura principal e configuração
2. **Funcionalidades MVP**: Funcionalidade mínima viável
3. **Funcionalidades Aprimoradas**: Capacidades adicionais
4. **Polimento**: Melhorias de performance e UX
5. **Pronto para Produção**: Teste completo e implantação
```

### Fase 3: Desafio e Validação

#### Análise do Advogado do Diabo
```yaml
desafios:
  riscos_tecnicos:
    - risco: "Performance em escala"
      mitigacao: "Implementar camada de cache"
    
    - risco: "Confiabilidade de API de terceiros"
      mitigacao: "Construir mecanismos de fallback"
  
  riscos_de_negocio:
    - risco: "Adoção pelo usuário"
      mitigacao: "Lançamento em fases com loops de feedback"
    
    - risco: "Expansão de escopo"
      mitigacao: "Definição rigorosa de MVP"
  
  casos_extremos:
    - cenario: "Sem conectividade de rede"
      tratamento: "Modo offline com sincronização"
    
    - cenario: "Atualizações concorrentes"
      tratamento: "Bloqueio otimista"
```

#### Critérios de Sucesso
```markdown
## Definição de Pronto
- [ ] Todas as histórias de usuário implementadas
- [ ] Cobertura de teste > 80%
- [ ] Benchmarks de performance atendidos
- [ ] Revisão de segurança aprovada
- [ ] Documentação completa

## Resultados Mensuráveis
- Métrica 1: [Valor alvo]
- Métrica 2: [Valor alvo]
- Satisfação do usuário: [Pontuação alvo]
```

### Fase 4: Validação e Saída

#### Lista de Verificação Pré-Implementação
```
VALIDAR pressupostos:
  - Viabilidade técnica confirmada
  - Disponibilidade de recursos verificada
  - Dependências identificadas
  - Riscos documentados com mitigações

REVISAR com stakeholders:
  - Alinhamento de negócio confirmado
  - Abordagem técnica aprovada
  - Cronograma aceitável
  - Métricas de sucesso acordadas
```

#### Formato de Saída
O PRD final deve ser estruturado como:

1. **Resumo Executivo** (1 página)
2. **Requisitos Detalhados** (com diagramas)
3. **Arquitetura Técnica** (com diagramas)
4. **Plano de Implementação** (com cronograma)
5. **Apêndices** (pesquisa, alternativas consideradas)

### Comandos de Validação

```bash
# Verificar completude do PRD
grep -E "(TODO|TBD|FIXME)" prd_gerado.md

# Verificar sintaxe de diagrama
mermaid-cli -i prd_gerado.md -o diagramas_prd.pdf

# Validar estrutura
python validar_estrutura_prd.py prd_gerado.md
```

## Anti-Padrões a Evitar
- ❌ Requisitos vagos sem critérios de aceitação
- ❌ Casos extremos e cenários de erro ausentes
- ❌ Diagramas que não correspondem ao texto
- ❌ Jargão técnico sem explicação
- ❌ Cronogramas irreais
- ❌ Sem métricas de sucesso

## Indicadores de Sucesso
- ✅ Outro desenvolvedor poderia implementar apenas com este PRD
- ✅ Todos os stakeholders entendem o plano
- ✅ Riscos são identificados com mitigações
- ✅ Caminho claro do estado atual para o estado desejado
- ✅ Diagramas esclarecem em vez de confundir

## Exemplo de Uso do Template

Entrada: "Construir um sistema de notificação para nosso app"

A saída incluiria:
- Diagramas de fluxo do usuário para diferentes tipos de notificação
- Arquitetura do sistema mostrando padrões pub/sub
- Diagramas de sequência para entrega em tempo real
- Esquema de banco de dados para preferências de notificação
- Especificações de API para endpoints de notificação
- Fases de implementação e prioridades
- Casos extremos como usuários offline, limitação de taxa
- Métricas de sucesso como taxa de entrega, engajamento do usuário

O PRD resultante se torna a entrada `$ARGUMENTS` para PRPs de implementação como BASE_PRP ou SPEC_PRP.
