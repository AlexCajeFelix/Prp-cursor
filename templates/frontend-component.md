# [Nome do Componente Frontend]

**Tipo:** Componente de Interface
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [X horas]
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
[Descreva claramente o que este componente faz, onde será usado e qual problema resolve na interface]

### Objetivos
- [Objetivo principal do componente]
- [Objetivos de usabilidade]
- [Objetivos de reutilização]

### Justificativa
[Por que este componente é necessário? Qual problema de UI/UX resolve? Como se integra com o design system?]

## ⚙️ Requisitos Funcionais

### Funcionalidades Principais
1. **[Funcionalidade Principal 1]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Comportamento:** [Como o componente se comporta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

2. **[Funcionalidade Principal 2]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Comportamento:** [Como o componente se comporta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

3. **[Funcionalidade Principal 3]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Comportamento:** [Como o componente se comporta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

### Estados do Componente
- **Estado Inicial:** [Como o componente aparece inicialmente]
- **Estados de Loading:** [Estados de carregamento]
- **Estados de Erro:** [Como erros são exibidos]
- **Estados de Sucesso:** [Feedback de sucesso]
- **Estados Vazios:** [Quando não há dados]

### Interações
- **Click/Tap:** [O que acontece ao clicar]
- **Hover/Focus:** [Estados visuais de interação]
- **Keyboard Navigation:** [Navegação por teclado]
- **Touch Gestures:** [Gestos em dispositivos móveis]

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Framework:** [React/Vue/Angular/Svelte + versão]
- **Linguagem:** [TypeScript/JavaScript + versão]
- **Styling:** [CSS Modules/Styled Components/Tailwind CSS + versão]
- **State Management:** [Redux/Zustand/Pinia/Vuex + versão]
- **Testing:** [Jest/Vitest/Testing Library + versões]

### Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Component     │    │   Props/Events  │    │   Styling       │
│   Logic         │◄──►│   Interface     │◄──►│   System        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   State         │    │   Validation    │    │   Accessibility │
│   Management    │    │   & Error       │    │   Features      │
│                 │    │   Handling      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Padrões de Código
- **Linguagem:** [TypeScript/JavaScript + versão]
- **Framework:** [React/Vue/Angular/Svelte + versão]
- **Convenções:** [ESLint/Prettier configurados]
- **Testes:** [Jest/Vitest + Testing Library]
- **Styling:** [CSS Modules/Styled Components/Tailwind]
- **Storybook:** [Documentação interativa]

## 📁 Estrutura de Arquivos

```
component/
├── [ComponentName]/
│   ├── index.tsx          # Componente principal
│   ├── [ComponentName].tsx # Implementação do componente
│   ├── [ComponentName].types.ts # Definições de tipos
│   ├── [ComponentName].styles.ts # Estilos do componente
│   ├── [ComponentName].hooks.ts # Custom hooks (se necessário)
│   ├── [ComponentName].utils.ts # Utilitários específicos
│   ├── [ComponentName].test.tsx # Testes do componente
│   ├── [ComponentName].stories.tsx # Storybook stories
│   └── README.md          # Documentação do componente
├── __tests__/             # Testes adicionais
│   ├── integration/       # Testes de integração
│   └── e2e/              # Testes end-to-end
└── docs/                 # Documentação
    ├── design.md         # Especificações de design
    ├── usage.md          # Guia de uso
    └── examples.md       # Exemplos de uso
```

## 📦 Entregáveis Esperados

### Código
- [ ] Componente principal implementado
- [ ] Props interface definida
- [ ] Event handlers implementados
- [ ] State management configurado
- [ ] Custom hooks criados (se necessário)
- [ ] Utilitários implementados
- [ ] Estilos aplicados e responsivos
- [ ] Acessibilidade implementada

### Funcionalidades
- [ ] [Funcionalidade 1] implementada e funcionando
- [ ] [Funcionalidade 2] implementada e funcionando
- [ ] [Funcionalidade 3] implementada e funcionando
- [ ] Todos os estados visuais implementados
- [ ] Interações funcionando corretamente
- [ ] Validação de dados implementada
- [ ] Tratamento de erros implementado

### Testes
- [ ] Testes unitários para lógica do componente
- [ ] Testes de renderização
- [ ] Testes de interação do usuário
- [ ] Testes de acessibilidade
- [ ] Testes visuais (se aplicável)
- [ ] Cobertura de testes >= 80%

### Documentação
- [ ] Storybook stories criadas
- [ ] Documentação de props
- [ ] Exemplos de uso
- [ ] Guia de customização
- [ ] Especificações de design
- [ ] README com instruções

## ✅ Critérios de Qualidade

### Código
- [ ] Componente reutilizável e modular
- [ ] Props bem definidas e tipadas
- [ ] Código limpo e bem estruturado
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções de linting
- [ ] Performance otimizada
- [ ] Bundle size otimizado

### Design e UX
- [ ] Design consistente com design system
- [ ] Responsividade implementada
- [ ] Estados visuais claros
- [ ] Feedback adequado para interações
- [ ] Loading states implementados
- [ ] Error states bem definidos
- [ ] Empty states considerados

### Acessibilidade
- [ ] ARIA labels implementados
- [ ] Navegação por teclado funcional
- [ ] Contraste adequado
- [ ] Screen reader friendly
- [ ] Focus management implementado
- [ ] Semantic HTML utilizado
- [ ] Alt texts para imagens

### Performance
- [ ] Renderização otimizada
- [ ] Lazy loading implementado (se aplicável)
- [ ] Memoização aplicada onde necessário
- [ ] Bundle size otimizado
- [ ] Tempo de renderização < 16ms
- [ ] Sem memory leaks

### Compatibilidade
- [ ] Funciona em navegadores modernos
- [ ] Responsivo em mobile/tablet/desktop
- [ ] Touch gestures implementados (mobile)
- [ ] Fallbacks para funcionalidades não suportadas
- [ ] Cross-browser testing realizado

## 📚 Exemplos e Referências

### Exemplo de Implementação React
```typescript
// [ComponentName].tsx
import React, { useState, useCallback } from 'react';
import { ComponentNameProps } from './[ComponentName].types';
import { StyledComponent } from './[ComponentName].styles';

export const ComponentName: React.FC<ComponentNameProps> = ({
  label,
  value,
  onChange,
  disabled = false,
  error,
  ...props
}) => {
  const [isFocused, setIsFocused] = useState(false);

  const handleChange = useCallback((newValue: string) => {
    if (!disabled && onChange) {
      onChange(newValue);
    }
  }, [disabled, onChange]);

  const handleFocus = useCallback(() => {
    setIsFocused(true);
  }, []);

  const handleBlur = useCallback(() => {
    setIsFocused(false);
  }, []);

  return (
    <StyledComponent
      focused={isFocused}
      error={!!error}
      disabled={disabled}
      {...props}
    >
      <label htmlFor={props.id} className="component-label">
        {label}
      </label>
      <input
        id={props.id}
        value={value}
        onChange={(e) => handleChange(e.target.value)}
        onFocus={handleFocus}
        onBlur={handleBlur}
        disabled={disabled}
        aria-describedby={error ? `${props.id}-error` : undefined}
        aria-invalid={!!error}
      />
      {error && (
        <div id={`${props.id}-error`} className="component-error" role="alert">
          {error}
        </div>
      )}
    </StyledComponent>
  );
};
```

### Exemplo de Storybook
```typescript
// [ComponentName].stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ComponentName } from './[ComponentName]';

const meta: Meta<typeof ComponentName> = {
  title: 'Components/[ComponentName]',
  component: ComponentName,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    onChange: { action: 'changed' },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    label: 'Nome do Campo',
    placeholder: 'Digite aqui...',
  },
};

export const WithError: Story = {
  args: {
    label: 'Nome do Campo',
    value: 'Valor inválido',
    error: 'Este campo é obrigatório',
  },
};

export const Disabled: Story = {
  args: {
    label: 'Nome do Campo',
    value: 'Valor fixo',
    disabled: true,
  },
};
```

### Referências
- [React Documentation](https://react.dev/)
- [Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Material Design Guidelines](https://material.io/design)
- [Storybook Documentation](https://storybook.js.org/docs/)

## 🔄 Considerações Adicionais

### Design System Integration
- [ ] Tokens de design utilizados
- [ ] Componentes base reutilizados
- [ ] Temas suportados (light/dark)
- [ ] Breakpoints consistentes
- [ ] Typography scale aplicada

### Internationalization
- [ ] Textos externalizados
- [ ] RTL support (se necessário)
- [ ] Localização de datas/números
- [ ] Pluralização adequada

### Analytics e Tracking
- [ ] Eventos de interação trackados
- [ ] Métricas de uso implementadas
- [ ] Error tracking configurado
- [ ] Performance monitoring

### Versionamento
- [ ] Versionamento semântico
- [ ] Breaking changes documentados
- [ ] Migration guide (se necessário)
- [ ] Deprecation warnings
