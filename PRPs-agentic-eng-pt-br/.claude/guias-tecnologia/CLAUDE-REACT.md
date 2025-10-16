# CLAUDE.md

Este arquivo fornece orientação ao Claude Code ao trabalhar com aplicações React 19.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)

A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)

Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Arquitetura Componente-First

Construa com componentes reutilizáveis e compostos. Cada componente deve ter uma única responsabilidade clara e ser autocontido com seus próprios estilos, testes e lógica co-localizados.

### Performance por Padrão

Com o compilador do React 19, otimizações manuais são em grande parte desnecessárias. Foque em código limpo e legível e deixe o compilador lidar com otimizações de performance.

### Princípios de Design (DEVE SEGUIR)

- **Arquitetura Vertical Slice**: DEVE organizar por funcionalidades, não camadas
- **Composição sobre Herança**: DEVE usar o modelo de composição do React
- **Falhar Rápido**: DEVE validar entradas cedo com Zod, lançar erros imediatamente

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

## 🚀 Recursos-Chave do React 19

### Otimizações Automáticas

- **Compilador React**: Elimina necessidade de `useMemo`, `useCallback` e `React.memo`
- Deixe o compilador lidar com performance - escreva código limpo e legível

### Recursos Principais

- **Server Components**: Use para busca de dados e conteúdo estático
- **Actions**: Manipule operações async com estados pending integrados
- **API use()**: Busca de dados simplificada e consumo de contexto
- **Metadata de Documento**: Suporte nativo para tags SEO
- **Suspense Aprimorado**: Melhores estados de carregamento e error boundaries

### Integração TypeScript React 19 (OBRIGATÓRIO)

- **Tipos Rigorosos**: Use `strict: true` no tsconfig.json
- **Tipagem de Props**: Sempre defina interfaces TypeScript para props de componente
- **Generics**: Use generics para componentes reutilizáveis
- **Validação de Runtime**: Combine TypeScript com Zod para validação

```typescript
// ✅ Exemplo de componente React 19 com TypeScript rigoroso
interface UserCardProps {
  user: {
    id: string;
    name: string;
    email: string;
  };
  onEdit?: (userId: string) => void;
}

export function UserCard({ user, onEdit }: UserCardProps) {
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      {onEdit && (
        <button onClick={() => onEdit(user.id)}>
          Editar
        </button>
      )}
    </div>
  );
}
```

## 📁 Estrutura de Arquivos e Organização

### Arquitetura Vertical Slice (OBRIGATÓRIO)

Organize por funcionalidades, não por tipo de arquivo:

```
src/
├── features/
│   ├── user-management/
│   │   ├── components/
│   │   │   ├── UserList.tsx
│   │   │   ├── UserForm.tsx
│   │   │   └── UserCard.tsx
│   │   ├── hooks/
│   │   │   ├── useUsers.ts
│   │   │   └── useUserForm.ts
│   │   ├── services/
│   │   │   └── userService.ts
│   │   ├── types/
│   │   │   └── user.types.ts
│   │   └── index.ts
│   ├── dashboard/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── services/
│   └── auth/
│       ├── components/
│       ├── hooks/
│       └── services/
├── shared/
│   ├── components/
│   │   ├── ui/
│   │   └── layout/
│   ├── hooks/
│   ├── utils/
│   └── types/
└── app/
    ├── layout.tsx
    ├── page.tsx
    └── globals.css
```

### Convenções de Nomenclatura

```typescript
// ✅ Componentes: PascalCase
export function UserProfile() {}

// ✅ Hooks: camelCase com prefixo 'use'
export function useUserData() {}

// ✅ Tipos/Interfaces: PascalCase
interface UserProfileProps {}
type UserStatus = 'active' | 'inactive';

// ✅ Constantes: SCREAMING_SNAKE_CASE
export const API_ENDPOINTS = {
  USERS: '/api/users',
  AUTH: '/api/auth'
};

// ✅ Utilitários: camelCase
export function formatUserName() {}
```

## 🎯 Padrões de Componentes

### Server Components (Padrão)

Use Server Components para busca de dados e conteúdo estático:

```typescript
// ✅ Server Component - busca de dados
async function UserList() {
  const users = await fetchUsers();
  
  return (
    <div>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}
```

### Client Components

Use Client Components apenas quando necessário (interatividade, estado, eventos):

```typescript
'use client';

// ✅ Client Component - interatividade
import { useState } from 'react';

export function Counter() {
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
```

### Composição de Componentes

```typescript
// ✅ Composição sobre herança
interface ModalProps {
  children: React.ReactNode;
  isOpen: boolean;
  onClose: () => void;
}

export function Modal({ children, isOpen, onClose }: ModalProps) {
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {children}
      </div>
    </div>
  );
}

// Uso composicional
<Modal isOpen={showModal} onClose={() => setShowModal(false)}>
  <UserForm onSubmit={handleSubmit} />
</Modal>
```

## 🔄 Gerenciamento de Estado

### Estado Local (useState/useReducer)

```typescript
// ✅ Estado simples
const [count, setCount] = useState(0);

// ✅ Estado complexo
const [state, dispatch] = useReducer(userReducer, initialState);

function userReducer(state: UserState, action: UserAction): UserState {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    case 'SET_USERS':
      return { ...state, users: action.payload, loading: false };
    default:
      return state;
  }
}
```

### Estado Global (Context/Zustand)

```typescript
// ✅ Context para estado global
interface AppContextType {
  user: User | null;
  setUser: (user: User | null) => void;
}

const AppContext = createContext<AppContextType | null>(null);

export function useApp() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp deve ser usado dentro de AppProvider');
  }
  return context;
}
```

## 🔗 Busca de Dados

### Server Components com fetch

```typescript
// ✅ Busca de dados em Server Component
async function UserProfile({ userId }: { userId: string }) {
  const user = await fetch(`/api/users/${userId}`).then(r => r.json());
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

### Client Components com SWR/React Query

```typescript
'use client';

// ✅ Busca de dados em Client Component
import useSWR from 'swr';

export function UserProfile({ userId }: { userId: string }) {
  const { data: user, error, isLoading } = useSWR(
    `/api/users/${userId}`,
    fetcher
  );
  
  if (isLoading) return <div>Carregando...</div>;
  if (error) return <div>Erro ao carregar usuário</div>;
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

## 🎨 Estilização

### Tailwind CSS (Recomendado)

```typescript
// ✅ Componente com Tailwind
export function Button({ variant, children, ...props }: ButtonProps) {
  const baseClasses = "px-4 py-2 rounded font-medium transition-colors";
  const variantClasses = {
    primary: "bg-blue-600 text-white hover:bg-blue-700",
    secondary: "bg-gray-200 text-gray-900 hover:bg-gray-300",
    danger: "bg-red-600 text-white hover:bg-red-700"
  };
  
  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]}`}
      {...props}
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

export function Button({ children, ...props }: ButtonProps) {
  return (
    <button className={styles.button} {...props}>
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
import { Counter } from './Counter';

describe('Counter', () => {
  it('deve incrementar contagem quando botão é clicado', () => {
    render(<Counter />);
    
    const button = screen.getByRole('button', { name: /incrementar/i });
    const count = screen.getByText(/contagem: 0/i);
    
    fireEvent.click(button);
    
    expect(screen.getByText(/contagem: 1/i)).toBeInTheDocument();
  });
});
```

### Testes de Hook

```typescript
// ✅ Teste de hook customizado
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('deve incrementar contagem', () => {
    const { result } = renderHook(() => useCounter());
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
});
```

## 🔧 Ferramentas e Configuração

### ESLint e Prettier

```json
// .eslintrc.json
{
  "extends": [
    "next/core-web-vitals",
    "@typescript-eslint/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn"
  }
}
```

### TypeScript Config

```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}
```

## 🚫 Anti-Padrões

### ❌ Evite

```typescript
// ❌ Componentes muito grandes
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
```

### ✅ Faça

```typescript
// ✅ Componentes pequenos e focados
function UserCard({ user }: { user: User }) {
  return <div>{user.name}</div>;
}

// ✅ Context para estado compartilhado
function App() {
  return (
    <UserProvider>
      <UserList />
    </UserProvider>
  );
}

// ✅ Busca de dados direta em Server Component
async function UserList() {
  const users = await fetchUsers(); // ✅
  return <div>{users.map(user => <UserCard key={user.id} user={user} />)}</div>;
}
```

## 📚 Recursos Adicionais

- [Documentação Oficial do React 19](https://react.dev)
- [Next.js 15 App Router](https://nextjs.org/docs/app)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

---

**Lembre-se**: Foque em código limpo, legível e testável. Deixe o React Compiler lidar com otimizações de performance. Use TypeScript rigorosamente para melhor experiência de desenvolvimento.
