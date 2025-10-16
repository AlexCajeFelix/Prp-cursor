# CLAUDE.md

Este arquivo fornece orientação abrangente ao Claude Code ao trabalhar com aplicações Next.js 15 com React 19 e TypeScript.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)
A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)
Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Princípios de Design
- **Inversão de Dependência**: Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
- **Princípio Aberto/Fechado**: Entidades de software devem ser abertas para extensão mas fechadas para modificação.
- **Arquitetura Vertical Slice**: Organize por funcionalidades, não camadas
- **Componente-First**: Construa com componentes reutilizáveis e compostos com responsabilidade única
- **Falhar Rápido**: Valide entradas cedo, lance erros imediatamente

## 🤖 Diretrizes para Assistente de IA

### Consciência de Contexto
- Ao implementar funcionalidades, sempre verifique padrões existentes primeiro
- Prefira composição sobre herança em todos os designs
- Use utilitários existentes antes de criar novos
- Verifique funcionalidades similares em outros domínios/funcionalidades

### Armadilhas Comuns a Evitar
- Criar funcionalidade duplicada
- Sobrescrever testes existentes
- Modificar frameworks principais sem instrução explícita
- Adicionar dependências sem verificar alternativas existentes

### Padrões de Fluxo de Trabalho
- Preferencialmente criar testes ANTES da implementação (TDD)
- Use "pensar duro" para decisões de arquitetura
- Quebre tarefas complexas em unidades menores e testáveis
- Valide entendimento antes da implementação

### Requisitos de Comandos de Pesquisa
**CRÍTICO**: Sempre use `rg` (ripgrep) em vez de comandos tradicionais `grep` e `find`:

```bash
# ❌ Não use grep
grep -r "pattern" .

# ✅ Use rg em vez disso
rg "pattern"

# ❌ Não use find com name
find . -name "*.tsx"

# ✅ Use rg com filtragem de arquivo
rg --files | rg "\.tsx$"
# ou
rg --files -g "*.tsx"
```

**Regras de Aplicação:**
```
(
    r"^grep\b(?!.*\|)",
    "Use 'rg' (ripgrep) em vez de 'grep' para melhor performance e recursos",
),
(
    r"^find\s+\S+\s+-name\b",
    "Use 'rg --files | rg pattern' ou 'rg --files -g pattern' em vez de 'find -name' para melhor performance",
),
```

## 🧱 Estrutura de Código e Modularidade

### Limites de Arquivo e Componente
- **Nunca crie um arquivo com mais de 500 linhas de código.** Se aproximando deste limite, refatore dividindo em módulos ou arquivos auxiliares.
- **Componentes devem ter menos de 200 linhas** para melhor manutenibilidade.
- **Funções devem ser curtas e focadas, sub 50 linhas** e ter uma única responsabilidade.
- **Organize código em módulos claramente separados**, agrupados por funcionalidade ou responsabilidade.

## 🚀 Recursos-Chave do Next.js 15 e React 19

### Recursos Principais do Next.js 15
- **Turbopack**: Bundler rápido para desenvolvimento (estável)
- **App Router**: Roteador baseado em sistema de arquivos com layouts e roteamento aninhado
- **Server Components**: React Server Components para performance
- **Server Actions**: Funções de servidor type-safe
- **Parallel Routes**: Renderização concorrente de múltiplas páginas
- **Intercepting Routes**: Experiências tipo modal

### Recursos do React 19
- **React Compiler**: Elimina necessidade de `useMemo`, `useCallback` e `React.memo`
- **Actions**: Manipule operações async com estados pending integrados
- **API use()**: Busca de dados simplificada e consumo de contexto
- **Metadata de Documento**: Suporte nativo para tags SEO
- **Suspense Aprimorado**: Melhores estados de carregamento e error boundaries

### Integração TypeScript (OBRIGATÓRIO)
- **DEVE usar `ReactElement` em vez de `JSX.Element`** para tipos de retorno
- **DEVE importar tipos de 'react'** explicitamente
- **NUNCA use namespace `JSX.Element`** - use tipos React diretamente

```typescript
// ✅ Correto
import { ReactElement } from 'react';

function MyComponent(): ReactElement {
  return <div>Hello</div>;
}

// ❌ Incorreto
function MyComponent(): JSX.Element {
  return <div>Hello</div>;
}
```

## 📁 Estrutura de Arquivos e Organização

### Arquitetura Vertical Slice (OBRIGATÓRIO)

Organize por funcionalidades, não por tipo de arquivo:

```
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── globals.css
│   ├── loading.tsx
│   ├── error.tsx
│   ├── not-found.tsx
│   └── (dashboard)/
│       ├── layout.tsx
│       ├── page.tsx
│       └── users/
│           ├── page.tsx
│           ├── [id]/
│           │   └── page.tsx
│           └── create/
│               └── page.tsx
├── components/
│   ├── ui/
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   └── modal.tsx
│   ├── forms/
│   │   ├── user-form.tsx
│   │   └── login-form.tsx
│   └── layout/
│       ├── header.tsx
│       ├── sidebar.tsx
│       └── footer.tsx
├── features/
│   ├── users/
│   │   ├── components/
│   │   │   ├── user-list.tsx
│   │   │   └── user-card.tsx
│   │   ├── hooks/
│   │   │   └── use-users.ts
│   │   ├── services/
│   │   │   └── user-service.ts
│   │   ├── types/
│   │   │   └── user.types.ts
│   │   └── index.ts
│   └── auth/
│       ├── components/
│       ├── hooks/
│       └── services/
├── lib/
│   ├── utils.ts
│   ├── validations.ts
│   ├── api.ts
│   └── database.ts
├── types/
│   ├── global.d.ts
│   └── api.types.ts
└── middleware.ts
```

### Convenções de Nomenclatura

```typescript
// ✅ Arquivos de página: page.tsx
// app/users/page.tsx

// ✅ Arquivos de layout: layout.tsx
// app/(dashboard)/layout.tsx

// ✅ Componentes: kebab-case
// user-card.tsx, login-form.tsx

// ✅ Hooks: camelCase com prefixo 'use'
// useUsers.ts, useAuth.ts

// ✅ Serviços: kebab-case com sufixo
// user-service.ts, auth-service.ts

// ✅ Tipos: kebab-case
// user.types.ts, api.types.ts
```

## 🎯 Padrões de Componentes

### Server Components (Padrão)

Use Server Components para busca de dados e conteúdo estático:

```typescript
// ✅ Server Component - busca de dados
import { User } from '@/types/user.types';
import { UserCard } from '@/components/user-card';

async function UserList(): Promise<ReactElement> {
  // Busca de dados no servidor
  const users = await fetch('https://api.example.com/users')
    .then(res => res.json()) as User[];
  
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}

export default UserList;
```

### Client Components

Use Client Components apenas quando necessário (interatividade, estado, eventos):

```typescript
'use client';

// ✅ Client Component - interatividade
import { ReactElement, useState } from 'react';
import { User } from '@/types/user.types';

interface UserCardProps {
  user: User;
  onEdit?: (user: User) => void;
}

export function UserCard({ user, onEdit }: UserCardProps): ReactElement {
  const [isEditing, setIsEditing] = useState(false);
  
  const handleEdit = () => {
    setIsEditing(true);
    onEdit?.(user);
  };
  
  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <h3 className="text-lg font-semibold">{user.name}</h3>
      <p className="text-gray-600">{user.email}</p>
      {onEdit && (
        <button
          onClick={handleEdit}
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Editar
        </button>
      )}
    </div>
  );
}
```

### Server Actions

```typescript
// ✅ Server Action para mutações
'use server';

import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';

interface CreateUserData {
  name: string;
  email: string;
}

export async function createUser(formData: FormData): Promise<void> {
  const name = formData.get('name') as string;
  const email = formData.get('email') as string;
  
  // Validação
  if (!name || !email) {
    throw new Error('Nome e email são obrigatórios');
  }
  
  // Criar usuário
  const userData: CreateUserData = { name, email };
  await fetch('https://api.example.com/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData),
  });
  
  // Revalidar cache e redirecionar
  revalidatePath('/users');
  redirect('/users');
}
```

### Formulários com Server Actions

```typescript
// ✅ Formulário com Server Action
import { createUser } from '@/actions/user-actions';

export function UserForm(): ReactElement {
  return (
    <form action={createUser} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium">
          Nome
        </label>
        <input
          type="text"
          id="name"
          name="name"
          required
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>
      
      <div>
        <label htmlFor="email" className="block text-sm font-medium">
          Email
        </label>
        <input
          type="email"
          id="email"
          name="email"
          required
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>
      
      <button
        type="submit"
        className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
      >
        Criar Usuário
      </button>
    </form>
  );
}
```

## 🔄 Gerenciamento de Estado

### Estado Local (useState/useReducer)

```typescript
'use client';

import { ReactElement, useState, useReducer } from 'react';

// ✅ Estado simples
export function Counter(): ReactElement {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Contagem: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Incrementar
      </button>
    </div>
  );
}

// ✅ Estado complexo com useReducer
interface CounterState {
  count: number;
  step: number;
}

type CounterAction = 
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStep'; step: number };

function counterReducer(state: CounterState, action: CounterAction): CounterState {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'setStep':
      return { ...state, step: action.step };
    default:
      return state;
  }
}

export function AdvancedCounter(): ReactElement {
  const [state, dispatch] = useReducer(counterReducer, { count: 0, step: 1 });
  
  return (
    <div>
      <p>Contagem: {state.count}</p>
      <input
        type="number"
        value={state.step}
        onChange={e => dispatch({ type: 'setStep', step: Number(e.target.value) })}
      />
      <button onClick={() => dispatch({ type: 'increment' })}>
        +{state.step}
      </button>
      <button onClick={() => dispatch({ type: 'decrement' })}>
        -{state.step}
      </button>
    </div>
  );
}
```

### Context API

```typescript
'use client';

import { ReactElement, createContext, useContext, useState, ReactNode } from 'react';

interface User {
  id: string;
  name: string;
  email: string;
}

interface AuthContextType {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }): ReactElement {
  const [user, setUser] = useState<User | null>(null);
  
  const login = (userData: User) => {
    setUser(userData);
  };
  
  const logout = () => {
    setUser(null);
  };
  
  const isAuthenticated = user !== null;
  
  return (
    <AuthContext.Provider value={{ user, login, logout, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de AuthProvider');
  }
  return context;
}
```

## 🔗 Busca de Dados

### Server Components com fetch

```typescript
// ✅ Busca de dados em Server Component
interface User {
  id: string;
  name: string;
  email: string;
}

async function UserProfile({ userId }: { userId: string }): Promise<ReactElement> {
  // Busca de dados no servidor
  const user = await fetch(`https://api.example.com/users/${userId}`, {
    cache: 'force-cache', // Cache estático
    next: { revalidate: 3600 }, // Revalidar a cada hora
  }).then(res => res.json()) as User;
  
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h1 className="text-2xl font-bold">{user.name}</h1>
      <p className="text-gray-600">{user.email}</p>
    </div>
  );
}
```

### Client Components com SWR

```typescript
'use client';

import { ReactElement } from 'react';
import useSWR from 'swr';

const fetcher = (url: string) => fetch(url).then(res => res.json());

interface UserProfileProps {
  userId: string;
}

export function UserProfile({ userId }: UserProfileProps): ReactElement {
  const { data: user, error, isLoading } = useSWR(
    `/api/users/${userId}`,
    fetcher
  );
  
  if (isLoading) return <div>Carregando...</div>;
  if (error) return <div>Erro ao carregar usuário</div>;
  if (!user) return <div>Usuário não encontrado</div>;
  
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h1 className="text-2xl font-bold">{user.name}</h1>
      <p className="text-gray-600">{user.email}</p>
    </div>
  );
}
```

## 🎨 Estilização

### Tailwind CSS (Recomendado)

```typescript
// ✅ Componente com Tailwind
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({ 
  variant = 'primary', 
  size = 'md', 
  children, 
  onClick,
  disabled = false 
}: ButtonProps): ReactElement {
  const baseClasses = "inline-flex items-center justify-center font-medium rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2";
  
  const variantClasses = {
    primary: "bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500",
    secondary: "bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500",
    danger: "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500"
  };
  
  const sizeClasses = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2 text-base",
    lg: "px-6 py-3 text-lg"
  };
  
  const disabledClasses = disabled ? "opacity-50 cursor-not-allowed" : "";
  
  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${disabledClasses}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}
```

### CSS Modules

```typescript
// ✅ Componente com CSS Modules
import styles from './Button.module.css';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  children: ReactNode;
}

export function Button({ variant = 'primary', children }: ButtonProps): ReactElement {
  return (
    <button className={`${styles.button} ${styles[variant]}`}>
      {children}
    </button>
  );
}
```

## 🧪 Testes

### Testes de Componente

```typescript
// ✅ Teste de componente com React Testing Library
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('deve renderizar com texto correto', () => {
    render(<Button>Clique aqui</Button>);
    
    expect(screen.getByRole('button', { name: 'Clique aqui' })).toBeInTheDocument();
  });
  
  it('deve chamar onClick quando clicado', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Clique aqui</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('deve estar desabilitado quando disabled é true', () => {
    render(<Button disabled>Botão Desabilitado</Button>);
    
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

### Testes de Página

```typescript
// ✅ Teste de página Next.js
import { render, screen } from '@testing-library/react';
import HomePage from '@/app/page';

// Mock do fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      { id: '1', name: 'João Silva', email: 'joao@example.com' }
    ]),
  })
) as jest.Mock;

describe('HomePage', () => {
  it('deve renderizar lista de usuários', async () => {
    render(await HomePage());
    
    expect(screen.getByText('João Silva')).toBeInTheDocument();
    expect(screen.getByText('joao@example.com')).toBeInTheDocument();
  });
});
```

## 🔧 Ferramentas e Configuração

### Next.js Config

```typescript
// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  experimental: {
    turbo: {
      rules: {
        '*.svg': {
          loaders: ['@svgr/webpack'],
          as: '*.js',
        },
      },
    },
  },
  images: {
    domains: ['example.com'],
  },
  typescript: {
    ignoreBuildErrors: false,
  },
  eslint: {
    ignoreDuringBuilds: false,
  },
};

export default nextConfig;
```

### TypeScript Config

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## 🚫 Anti-Padrões

### ❌ Evite

```typescript
// ❌ Componente muito grande
function MegaComponent() {
  // 500+ linhas de código
}

// ❌ Props drilling excessivo
function Parent() {
  return <Child1 data={data} />;
}

// ❌ Estado global desnecessário
const [localState, setLocalState] = useState(); // Deveria ser local

// ❌ useEffect para busca de dados em Server Component
function ServerComponent() {
  useEffect(() => {
    fetchData(); // ❌ Use fetch diretamente
  }, []);
}

// ❌ JSX.Element em vez de ReactElement
function MyComponent(): JSX.Element { // ❌
  return <div>Hello</div>;
}
```

### ✅ Faça

```typescript
// ✅ Componentes pequenos e focados
function UserCard({ user }: { user: User }): ReactElement {
  return <div>{user.name}</div>;
}

// ✅ Context para estado compartilhado
function App(): ReactElement {
  return (
    <UserProvider>
      <UserList />
    </UserProvider>
  );
}

// ✅ Busca de dados direta em Server Component
async function UserList(): Promise<ReactElement> {
  const users = await fetchUsers(); // ✅
  return <div>{users.map(user => <UserCard key={user.id} user={user} />)}</div>;
}

// ✅ ReactElement para tipos de retorno
function MyComponent(): ReactElement { // ✅
  return <div>Hello</div>;
}
```

## 📚 Recursos Adicionais

- [Documentação Next.js 15](https://nextjs.org/docs)
- [React 19 Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

---

**Lembre-se**: Foque em código limpo, legível e testável. Use Server Components por padrão e Client Components apenas quando necessário. Deixe o React Compiler lidar com otimizações de performance. Use TypeScript rigorosamente com `ReactElement` para tipos de retorno.
