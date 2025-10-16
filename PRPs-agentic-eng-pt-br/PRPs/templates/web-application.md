# [Nome da Aplicação Web]

**Tipo:** Aplicação Web Completa
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [X horas]
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
[Descreva claramente o que a aplicação web fará, qual problema resolve e para quem é destinada]

### Objetivos
- [Objetivo principal da aplicação]
- [Objetivos secundários]
- [Métricas de sucesso]

### Justificativa
[Por que esta aplicação é necessária? Qual problema ela resolve?]

## ⚙️ Requisitos Funcionais

### Funcionalidades Principais
1. **[Funcionalidade Principal 1]**
   - Descrição: [Detalhes específicos da funcionalidade]
   - Critérios de aceitação: 
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

2. **[Funcionalidade Principal 2]**
   - Descrição: [Detalhes específicos da funcionalidade]
   - Critérios de aceitação:
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

3. **[Funcionalidade Principal 3]**
   - Descrição: [Detalhes específicos da funcionalidade]
   - Critérios de aceitação:
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

### Casos de Uso
- **Usuário anônimo:** [O que usuários não logados podem fazer]
- **Usuário autenticado:** [O que usuários logados podem fazer]
- **Administrador:** [Funcionalidades administrativas]

### Fluxos de Navegação
1. **Fluxo Principal:** [Descreva o fluxo mais importante]
2. **Fluxo Secundário:** [Descreva outros fluxos importantes]

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Frontend:** [React/Vue/Angular/Svelte + versões]
- **Backend:** [Node.js/Python/Java/.NET + versões]
- **Banco de Dados:** [PostgreSQL/MySQL/MongoDB + versões]
- **Estilização:** [CSS/Tailwind/Styled Components + versões]
- **Build Tool:** [Vite/Webpack/Parcel + versões]

### Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React/Vue)   │◄──►│   (API)         │◄──►│   (PostgreSQL)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Padrões de Código
- **Linguagem:** [TypeScript/JavaScript + versão]
- **Framework:** [React/Vue/Angular + versão]
- **Convenções:** [ESLint/Prettier configurados]
- **Testes:** [Jest/Vitest + Testing Library]
- **Roteamento:** [React Router/Vue Router + versão]
- **Estado:** [Redux/Zustand/Pinia + versão]

## 📁 Estrutura de Arquivos

```
projeto-web/
├── src/
│   ├── components/          # Componentes reutilizáveis
│   │   ├── ui/             # Componentes de UI básicos
│   │   ├── forms/          # Componentes de formulário
│   │   └── layout/         # Componentes de layout
│   ├── pages/              # Páginas da aplicação
│   │   ├── Home/           # Página inicial
│   │   ├── Login/          # Página de login
│   │   └── Dashboard/      # Dashboard principal
│   ├── services/           # Serviços e APIs
│   │   ├── api/            # Chamadas para API
│   │   ├── auth/           # Autenticação
│   │   └── storage/        # Gerenciamento de dados
│   ├── hooks/              # Custom hooks (React)
│   ├── utils/              # Utilitários
│   ├── types/              # Definições de tipos
│   ├── styles/             # Estilos globais
│   └── assets/             # Imagens, ícones, etc.
├── public/                 # Arquivos estáticos
├── tests/                  # Testes automatizados
│   ├── unit/              # Testes unitários
│   ├── integration/       # Testes de integração
│   └── e2e/               # Testes end-to-end
├── docs/                   # Documentação
└── config/                 # Configurações
```

## 📦 Entregáveis Esperados

### Código
- [ ] Estrutura de pastas criada
- [ ] Componentes principais implementados
- [ ] Páginas principais criadas
- [ ] Sistema de roteamento configurado
- [ ] Gerenciamento de estado implementado
- [ ] Integração com API backend
- [ ] Sistema de autenticação (se necessário)
- [ ] Responsividade implementada

### Funcionalidades
- [ ] [Funcionalidade 1] implementada e funcionando
- [ ] [Funcionalidade 2] implementada e funcionando
- [ ] [Funcionalidade 3] implementada e funcionando
- [ ] Navegação entre páginas funcionando
- [ ] Formulários validados e funcionais
- [ ] Tratamento de erros implementado

### Testes
- [ ] Testes unitários para componentes principais
- [ ] Testes de integração para fluxos críticos
- [ ] Testes e2e para jornada do usuário principal
- [ ] Cobertura de testes >= 80%

### Documentação
- [ ] README com instruções de instalação e uso
- [ ] Documentação dos componentes principais
- [ ] Guia de contribuição
- [ ] Documentação da API (se aplicável)

## ✅ Critérios de Qualidade

### Código
- [ ] Código limpo e bem estruturado
- [ ] Componentes reutilizáveis e modulares
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções ESLint/Prettier
- [ ] Sem código duplicado
- [ ] TypeScript configurado (se aplicável)

### Performance
- [ ] Tempo de carregamento inicial < 3 segundos
- [ ] Lazy loading implementado onde apropriado
- [ ] Otimização de imagens
- [ ] Bundle size otimizado
- [ ] Caching adequado implementado

### Segurança
- [ ] Validação de inputs no frontend e backend
- [ ] Sanitização de dados
- [ ] HTTPS obrigatório
- [ ] Tokens de autenticação seguros
- [ ] Proteção contra XSS e CSRF

### Usabilidade
- [ ] Interface responsiva (mobile, tablet, desktop)
- [ ] Navegação intuitiva
- [ ] Feedback visual adequado
- [ ] Tratamento de erros user-friendly
- [ ] Loading states implementados
- [ ] Acessibilidade básica (ARIA labels, contraste)

### SEO (se aplicável)
- [ ] Meta tags configuradas
- [ ] URLs amigáveis
- [ ] Sitemap gerado
- [ ] Open Graph tags
- [ ] Performance Core Web Vitals

## 📚 Exemplos e Referências

### Exemplos de Uso
```typescript
// Exemplo de componente principal
import React from 'react';
import { useNavigate } from 'react-router-dom';

interface HomePageProps {
  user?: User;
}

const HomePage: React.FC<HomePageProps> = ({ user }) => {
  const navigate = useNavigate();
  
  return (
    <div className="home-page">
      <h1>Bem-vindo{user ? `, ${user.name}` : ''}!</h1>
      {/* Resto da implementação */}
    </div>
  );
};

export default HomePage;
```

### Referências
- [Documentação do React](https://react.dev/)
- [Documentação do TypeScript](https://www.typescriptlang.org/)
- [Guia de Acessibilidade](https://www.w3.org/WAI/WCAG21/quickref/)
- [Padrões de Design System](https://designsystemsrepo.com/)

## 🔄 Considerações Adicionais

### Deploy
- [ ] Configuração para deploy em [Vercel/Netlify/AWS]
- [ ] Variáveis de ambiente configuradas
- [ ] Pipeline de CI/CD configurado
- [ ] Monitoramento básico implementado

### Manutenibilidade
- [ ] Logs estruturados implementados
- [ ] Error tracking configurado
- [ ] Analytics básico (se necessário)
- [ ] Documentação de troubleshooting

### Escalabilidade
- [ ] Estrutura preparada para crescimento
- [ ] Componentes otimizados para reutilização
- [ ] Performance otimizada para grandes volumes
- [ ] Arquitetura preparada para microserviços (se aplicável)
