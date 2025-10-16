name: "Template PRP TypeScript v3 - Focado em Implementação com Padrões de Precisão"
description: |

---

## Objetivo

**Meta da Funcionalidade**: [Estado final específico e mensurável do que precisa ser construído]

**Entregável**: [Artefato concreto - componente React, rota de API, integração, etc.]

**Definição de Sucesso**: [Como você saberá que isso está completo e funcionando]

## Persona do Usuário (se aplicável)

**Usuário Alvo**: [Tipo específico de usuário - desenvolvedor, usuário final, admin, etc.]

**Caso de Uso**: [Cenário principal quando esta funcionalidade será usada]

**Jornada do Usuário**: [Fluxo passo a passo de como o usuário interage com esta funcionalidade]

**Pontos de Dor Resolvidos**: [Frustrações específicas do usuário que esta funcionalidade resolve]

## Por que

- [Valor de negócio e impacto no usuário]
- [Integração com funcionalidades existentes]
- [Problemas que isso resolve e para quem]

## O que

[Comportamento visível ao usuário e requisitos técnicos]

### Critérios de Sucesso

- [ ] [Resultados específicos e mensuráveis]

## Todo o Contexto Necessário

### Verificação de Completude do Contexto

_Antes de escrever este PRP, valide: "Se alguém não soubesse nada sobre esta base de código, teria tudo o que é necessário para implementar isso com sucesso?"_

### Documentação e Referências

```yaml
# DEVE LER - Inclua estes na sua janela de contexto
- url: [URL completa com âncora de seção]
  why: [Métodos/conceitos específicos necessários para implementação]
  critical: [Insights-chave que previnem erros comuns de implementação]

- file: [caminho/exato/para/arquivo/padrão.tsx]
  why: [Padrão específico a seguir - estrutura de componente, uso de hook, etc.]
  pattern: [Breve descrição de qual padrão extrair]
  gotcha: [Restrições ou limitações conhecidas a evitar]

- docfile: [PRPs/ai_docs/typescript_specific.md]
  why: [Documentação personalizada para padrões complexos TypeScript/Next.js]
  section: [Seção específica se o documento for grande]
```

### Árvore atual da base de código (execute `tree` na raiz do projeto) para obter uma visão geral da base de código

```bash

```

### Árvore desejada da base de código com arquivos a serem adicionados e responsabilidade do arquivo

```bash

```

### Peculiaridades Conhecidas da nossa base de código e Biblioteca

```typescript
// CRÍTICO: [Nome da biblioteca] requer [configuração específica]
// Exemplo: Next.js 15 App Router - Handlers de rota devem exportar funções nomeadas
// Exemplo: diretiva 'use client' deve estar no topo do arquivo, afeta toda a árvore de componentes
// Exemplo: Server Components não podem usar APIs do navegador ou event handlers
// Exemplo: Usamos modo strict do TypeScript e requeremos tipagem adequada
```

## Blueprint de Implementação

### Modelos de dados e estrutura

Crie os modelos de dados principais, garantimos segurança de tipos e consistência.

```typescript
Exemplos:
 - schemas Zod para validação
 - interfaces/tipos TypeScript
 - tipos de esquema de banco de dados
 - tipos de resposta de API
 - tipos de props de componente

```

### Tarefas de Implementação (ordenadas por dependências)

```yaml
Tarefa 1: CRIAR lib/types/{domain}.types.ts
  - IMPLEMENTAR: Interfaces e tipos TypeScript para modelos de domínio
  - SEGUIR padrão: lib/types/existing.types.ts (estrutura de interface, padrões de exportação)
  - NOMENCLATURA: PascalCase para interfaces, camelCase para propriedades
  - LOCALIZAÇÃO: Definições de tipo em lib/types/

Tarefa 2: CRIAR components/{domain}/{ComponentName}.tsx
  - IMPLEMENTAR: Componente React com interface de props TypeScript adequada
  - SEGUIR padrão: components/existing/ExistingComponent.tsx (estrutura de componente, tipagem de props)
  - NOMENCLATURA: PascalCase para componentes, camelCase para props, kebab-case para classes CSS
  - DEPENDÊNCIAS: Importar tipos da Tarefa 1
  - LOCALIZAÇÃO: Camada de componente em components/{domain}/

Tarefa 3: CRIAR app/api/{resource}/route.ts
  - IMPLEMENTAR: Handlers de rota de API Next.js (GET, POST, etc.)
  - SEGUIR padrão: app/api/existing/route.ts (manipulação de request/response, padrões de erro)
  - NOMENCLATURA: Exportações nomeadas (GET, POST, PUT, DELETE), tipagem TypeScript adequada
  - DEPENDÊNCIAS: Importar tipos e componentes de tarefas anteriores
  - LOCALIZAÇÃO: Rotas de API em app/api/{resource}/

Tarefa 4: CRIAR app/{feature}/page.tsx
  - IMPLEMENTAR: Componente de página Next.js usando componentes de domínio
  - SEGUIR padrão: app/existing-page/page.tsx (estrutura de página, metadata, error boundaries)
  - NOMENCLATURA: Exportação padrão, exportação de metadata adequada, props de página TypeScript
  - DEPENDÊNCIAS: Importar componentes da Tarefa 2, tipos da Tarefa 1
  - LOCALIZAÇÃO: Rotas de página em app/{feature}/

Tarefa 5: CRIAR hooks/use{DomainAction}.ts
  - IMPLEMENTAR: Hooks React personalizados para gerenciamento de estado e chamadas de API
  - SEGUIR padrão: hooks/useExisting.ts (estrutura de hook, generics TypeScript, tratamento de erro)
  - NOMENCLATURA: use{ActionName} com tipos de retorno TypeScript adequados
  - DEPENDÊNCIAS: Importar tipos da Tarefa 1, endpoints de API da Tarefa 3
  - LOCALIZAÇÃO: Hooks personalizados em hooks/

Tarefa 6: CRIAR __tests__/{component}.test.tsx
  - IMPLEMENTAR: Testes Jest/Testing Library para componentes e hooks
  - SEGUIR padrão: __tests__/existing.test.tsx (estrutura de teste, padrões de mock)
  - NOMENCLATURA: blocos describe, convenções de nomenclatura de teste, tipagem de teste TypeScript
  - COBERTURA: Todos os componentes e hooks com casos de teste positivos e negativos
  - LOCALIZAÇÃO: Testes junto ao código que eles testam
```

### Padrões de Implementação e Detalhes-Chave

```typescript
// Mostrar padrões críticos e peculiaridades - mantenha conciso, foque em detalhes não óbvios

// Exemplo: Padrão de componente
interface {Domain}Props {
  // PADRÃO: Interfaces TypeScript rigorosas (seguir lib/types/existing.types.ts)
  data: {Domain}Data;
  onAction?: (id: string) => void;
}

export function {Domain}Component({ data, onAction }: {Domain}Props) {
  // PADRÃO: Padrões de Client/Server component (verificar componentes existentes)
  // PECULIARIDADE: 'use client' necessário para event handlers, useState, useEffect
  // CRÍTICO: Server Components para busca de dados, Client Components para interatividade

  return (
    // PADRÃO: Abordagem de estilo consistente (ver components/ui/)
    <div className="existing-class-pattern">
      {/* Seguir padrões de composição de componente existentes */}
    </div>
  );
}

// Exemplo: Padrão de rota de API
export async function GET(request: Request): Promise<Response> {
  // PADRÃO: Validação de request e tratamento de erro (ver app/api/existing/route.ts)
  // PECULIARIDADE: [Restrição específica do TypeScript ou requisito do Next.js]
  // RETORNAR: Objeto Response com tipagem TypeScript adequada
}

// Exemplo: Padrão de hook personalizado
export function use{Domain}Action(): {Domain}ActionResult {
  // PADRÃO: Estrutura de hook com generics TypeScript (ver hooks/useExisting.ts)
  // PECULIARIDADE: [Regras de hook React e requisitos de tipagem TypeScript]
}
```

### Pontos de Integração

```yaml
BANCO DE DADOS:
  - migration: "Adicionar tabela 'feature_data' com índices adequados"
  - client: "@/lib/database/client"
  - padrão: "createClient() para client components, createServerClient() para server components"

CONFIG:
  - adicionar a: .env.local
  - padrão: "NEXT_PUBLIC_* para variáveis de env do client-side"
  - padrão: "FEATURE_TIMEOUT = process.env.FEATURE_TIMEOUT || '30000'"

ROTAS:
  - estrutura de arquivo: app/feature-name/page.tsx
  - rotas de api: app/api/feature-name/route.ts
  - middleware: middleware.ts (nível raiz)
```

## Loop de Validação

### Nível 1: Sintaxe e Estilo (Feedback Imediato)

```bash
# Execute após cada criação de arquivo - corrija antes de prosseguir
npm run lint                    # Verificações ESLint com regras TypeScript
npx tsc --noEmit               # Verificação de tipos TypeScript (sem saída JS)
npm run format                 # Formatação Prettier

# Validação em todo o projeto
npm run lint:fix               # Auto-correção de problemas de linting
npm run type-check             # Validação TypeScript completa

# Esperado: Zero erros. Se existirem erros, LEIA a saída e corrija antes de prosseguir.
```

### Nível 2: Testes Unitários (Validação de Componente)

```bash
# Teste cada componente/hook conforme é criado
npm test -- __tests__/{domain}.test.tsx
npm test -- __tests__/use{Hook}.test.ts

# Suíte completa de testes para áreas afetadas
npm test -- components/{domain}/
npm test -- hooks/

# Validação de cobertura (se disponível)
npm test -- --coverage --watchAll=false

# Esperado: Todos os testes passam. Se falhando, depurar causa raiz e corrigir implementação.
```

### Nível 3: Teste de Integração (Validação do Sistema)

```bash
# Validação do servidor de desenvolvimento
npm run dev &
sleep 5  # Permitir tempo de inicialização do Next.js

# Validação de carregamento de página
curl -I http://localhost:3000/{feature-page}
# Esperado: Resposta 200 OK

# Validação de endpoint de API
curl -X POST http://localhost:3000/api/{resource} \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}' \
  | jq .  # Imprimir resposta JSON formatada

# Validação de build de produção
npm run build
# Esperado: Build bem-sucedido sem erros ou avisos TypeScript

# Validação de renderização de componente (se SSR/SSG)
curl http://localhost:3000/{page} | grep -q "expected-content"

# Esperado: Todas as integrações funcionando, respostas adequadas, sem erros de hidratação
```

### Nível 4: Validação Criativa e Específica do Domínio

```bash
# Validação Específica TypeScript/Next.js:

# Performance de build de produção
npm run build && npm run analyze  # Analisador de bundle se disponível

# Validação de segurança de tipos
npx tsc --noEmit --strict        # Verificação TypeScript rigorosa

# Verificações específicas do Next.js
npm run lint:next                # Regras de linting do Next.js se disponível

# Exemplos de Validação do Servidor MCP:
# Playwright MCP (para teste E2E)
playwright-mcp --test-user-flows --browser chromium

# Performance MCP (para auditorias Lighthouse)
lighthouse-mcp --url http://localhost:3000 --audit performance

# Accessibility MCP (para teste a11y)
axe-mcp --scan http://localhost:3000/{pages}

# Validação TypeScript/React Personalizada
# Testes de integração React Testing Library
# Testes de regressão visual Storybook (se disponível)
# Conformidade com modo strict TypeScript

# Esperado: Todas as validações criativas passam, padrões de performance/acessibilidade atendidos
```

## Lista de Verificação Final de Validação

### Validação Técnica

- [ ] Todos os 4 níveis de validação completados com sucesso
- [ ] Todos os testes passam: `npm test`
- [ ] Sem erros de linting: `npm run lint`
- [ ] Sem erros de tipo: `npx tsc --noEmit`
- [ ] Sem problemas de formatação: `npm run format --check`
- [ ] Build de produção bem-sucedido: `npm run build`

### Validação da Funcionalidade

- [ ] Todos os critérios de sucesso da seção "O que" atendidos
- [ ] Teste manual bem-sucedido: [comandos específicos do Nível 3]
- [ ] Casos de erro tratados graciosamente com tipos de erro TypeScript adequados
- [ ] Pontos de integração funcionam conforme especificado
- [ ] Requisitos da persona do usuário satisfeitos (se aplicável)

### Validação da Qualidade do Código

- [ ] Segue padrões e convenções de nomenclatura TypeScript/React existentes
- [ ] Colocação de arquivo corresponde à estrutura da árvore da base de código desejada
- [ ] Anti-padrões evitados (verificar contra seção Anti-Padrões)
- [ ] Dependências adequadamente gerenciadas com tipagens TypeScript corretas
- [ ] Mudanças de configuração adequadamente integradas

### Específico TypeScript/Next.js

- [ ] Interfaces e tipos TypeScript adequados definidos
- [ ] Padrões de Server/Client component seguidos corretamente
- [ ] Diretivas 'use client' usadas adequadamente
- [ ] Rotas de API seguem padrões Next.js App Router
- [ ] Sem incompatibilidades de hidratação entre renderização server/client

### Documentação e Implantação

- [ ] Código é auto-documentado com tipos TypeScript claros
- [ ] Interfaces de props adequadamente documentadas
- [ ] Variáveis de ambiente documentadas se novas forem adicionadas

---

## Anti-Padrões a Evitar

- ❌ Não criar novos padrões quando os existentes funcionam
- ❌ Não pular validação porque "deveria funcionar"
- ❌ Não ignorar testes falhando - corrija-os
- ❌ Não usar 'use client' desnecessariamente - abrace Server Components
- ❌ Não codificar valores que deveriam ser configuração
- ❌ Não capturar todas as exceções - seja específico
