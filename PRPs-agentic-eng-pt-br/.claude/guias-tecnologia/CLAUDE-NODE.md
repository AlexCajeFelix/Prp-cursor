# CLAUDE.md

Este arquivo fornece orientação abrangente ao Claude Code ao trabalhar com aplicações Node.js 23.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)
A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)
Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Princípios de Design
- **Arquitetura Modular**: Construa com módulos pequenos e focados que fazem uma coisa bem
- **Callbacks Error-First**: Sempre manipule erros como primeiro parâmetro em callbacks
- **Async por Padrão**: Use async/await para todas as operações de I/O
- **Falhar Rápido**: Valide entradas cedo e lance erros significativos imediatamente
- **Segurança Primeiro**: Nunca confie na entrada do usuário, sempre valide e sanitize

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
find . -name "*.js"

# ✅ Use rg com filtragem de arquivo
rg --files | rg "\.js$"
# ou
rg --files -g "*.js"
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

## 🚀 Recursos-Chave do Node.js 23

### Melhorias de Performance
- **V8 Engine atualizado**: Melhor performance de JavaScript
- **Streams otimizados**: Melhor manipulação de dados grandes
- **Worker Threads aprimorados**: Melhor paralelização de CPU

### Recursos Principais
- **ES Modules nativos**: Suporte completo para import/export
- **Top-level await**: Await no nível superior de módulos
- **Test Runner integrado**: Ferramenta de teste nativa
- **Web Streams API**: APIs web padrão para streams

### TypeScript Integration (OBRIGATÓRIO)
- **Tipos rigorosos**: Use `strict: true` no tsconfig.json
- **Tipagem de API**: Sempre defina tipos para APIs e interfaces
- **Generics**: Use generics para funções reutilizáveis
- **Validação de Runtime**: Combine TypeScript com Zod para validação

```typescript
// ✅ Exemplo de função Node.js com TypeScript rigoroso
interface User {
  id: string;
  name: string;
  email: string;
}

interface CreateUserRequest {
  name: string;
  email: string;
}

export async function createUser(userData: CreateUserRequest): Promise<User> {
  // Validação de entrada
  if (!userData.email.includes('@')) {
    throw new Error('Email inválido');
  }
  
  // Implementação
  const user: User = {
    id: generateId(),
    name: userData.name,
    email: userData.email.toLowerCase(),
  };
  
  await saveUser(user);
  return user;
}
```

## 📁 Estrutura de Arquivos e Organização

### Arquitetura Modular (OBRIGATÓRIO)

Organize por funcionalidades e responsabilidades:

```
src/
├── modules/
│   ├── users/
│   │   ├── controllers/
│   │   │   └── userController.ts
│   │   ├── services/
│   │   │   └── userService.ts
│   │   ├── repositories/
│   │   │   └── userRepository.ts
│   │   ├── models/
│   │   │   └── user.ts
│   │   ├── routes/
│   │   │   └── userRoutes.ts
│   │   ├── tests/
│   │   │   └── userService.test.ts
│   │   └── index.ts
│   ├── auth/
│   │   ├── controllers/
│   │   ├── services/
│   │   └── routes/
│   └── products/
│       ├── controllers/
│       ├── services/
│       └── routes/
├── shared/
│   ├── middleware/
│   ├── utils/
│   ├── types/
│   └── config/
├── app.ts
└── server.ts
```

### Convenções de Nomenclatura

```typescript
// ✅ Arquivos: kebab-case
// user-service.ts, auth-controller.ts

// ✅ Classes: PascalCase
export class UserService {}
export class AuthController {}

// ✅ Funções/Variáveis: camelCase
export function createUser() {}
export const userRepository = {};

// ✅ Constantes: SCREAMING_SNAKE_CASE
export const API_ENDPOINTS = {
  USERS: '/api/users',
  AUTH: '/api/auth'
};

// ✅ Tipos/Interfaces: PascalCase
interface UserData {}
type UserStatus = 'active' | 'inactive';
```

## 🎯 Padrões de API

### Express.js com TypeScript

```typescript
// controllers/userController.ts
import { Request, Response, NextFunction } from 'express';
import { UserService } from '../services/userService';
import { CreateUserRequest, User } from '../types/user';

export class UserController {
  constructor(private userService: UserService) {}

  async createUser(req: Request<{}, User, CreateUserRequest>, res: Response, next: NextFunction) {
    try {
      const userData = req.body;
      const user = await this.userService.createUser(userData);
      res.status(201).json(user);
    } catch (error) {
      next(error);
    }
  }

  async getUser(req: Request<{ id: string }>, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;
      const user = await this.userService.getUser(id);
      
      if (!user) {
        return res.status(404).json({ message: 'Usuário não encontrado' });
      }
      
      res.json(user);
    } catch (error) {
      next(error);
    }
  }
}
```

### Middleware de Erro

```typescript
// middleware/errorHandler.ts
import { Request, Response, NextFunction } from 'express';

interface AppError extends Error {
  statusCode?: number;
  isOperational?: boolean;
}

export function errorHandler(
  error: AppError,
  req: Request,
  res: Response,
  next: NextFunction
) {
  const statusCode = error.statusCode || 500;
  const message = error.isOperational ? error.message : 'Erro interno do servidor';

  console.error('Error:', {
    message: error.message,
    stack: error.stack,
    url: req.url,
    method: req.method,
  });

  res.status(statusCode).json({
    error: {
      message,
      statusCode,
      timestamp: new Date().toISOString(),
    },
  });
}

export function asyncHandler(fn: Function) {
  return (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
}
```

## 🔄 Gerenciamento de Estado

### Padrão de Serviço

```typescript
// services/userService.ts
import { UserRepository } from '../repositories/userRepository';
import { User, CreateUserRequest } from '../types/user';
import { AppError } from '../utils/errors';

export class UserService {
  constructor(private userRepository: UserRepository) {}

  async createUser(userData: CreateUserRequest): Promise<User> {
    // Validação de negócio
    const existingUser = await this.userRepository.findByEmail(userData.email);
    if (existingUser) {
      throw new AppError('Email já está em uso', 400);
    }

    // Criação do usuário
    const user = await this.userRepository.create(userData);
    return user;
  }

  async getUser(id: string): Promise<User | null> {
    return await this.userRepository.findById(id);
  }

  async updateUser(id: string, userData: Partial<CreateUserRequest>): Promise<User> {
    const user = await this.userRepository.findById(id);
    if (!user) {
      throw new AppError('Usuário não encontrado', 404);
    }

    return await this.userRepository.update(id, userData);
  }

  async deleteUser(id: string): Promise<void> {
    const user = await this.userRepository.findById(id);
    if (!user) {
      throw new AppError('Usuário não encontrado', 404);
    }

    await this.userRepository.delete(id);
  }
}
```

### Padrão de Repositório

```typescript
// repositories/userRepository.ts
import { User, CreateUserRequest } from '../types/user';
import { Database } from '../config/database';

export class UserRepository {
  constructor(private db: Database) {}

  async create(userData: CreateUserRequest): Promise<User> {
    const query = `
      INSERT INTO users (id, name, email, created_at)
      VALUES ($1, $2, $3, $4)
      RETURNING *
    `;
    
    const values = [
      generateId(),
      userData.name,
      userData.email,
      new Date(),
    ];

    const result = await this.db.query(query, values);
    return this.mapRowToUser(result.rows[0]);
  }

  async findById(id: string): Promise<User | null> {
    const query = 'SELECT * FROM users WHERE id = $1';
    const result = await this.db.query(query, [id]);
    
    if (result.rows.length === 0) {
      return null;
    }
    
    return this.mapRowToUser(result.rows[0]);
  }

  async findByEmail(email: string): Promise<User | null> {
    const query = 'SELECT * FROM users WHERE email = $1';
    const result = await this.db.query(query, [email]);
    
    if (result.rows.length === 0) {
      return null;
    }
    
    return this.mapRowToUser(result.rows[0]);
  }

  private mapRowToUser(row: any): User {
    return {
      id: row.id,
      name: row.name,
      email: row.email,
      createdAt: row.created_at,
    };
  }
}
```

## 🔗 Banco de Dados

### Configuração de Conexão

```typescript
// config/database.ts
import { Pool } from 'pg';
import { config } from 'dotenv';

config();

export class Database {
  private pool: Pool;

  constructor() {
    this.pool = new Pool({
      host: process.env.DB_HOST,
      port: parseInt(process.env.DB_PORT || '5432'),
      database: process.env.DB_NAME,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,
    });

    this.pool.on('error', (err) => {
      console.error('Erro inesperado no pool de conexões:', err);
    });
  }

  async query(text: string, params?: any[]) {
    const start = Date.now();
    try {
      const result = await this.pool.query(text, params);
      const duration = Date.now() - start;
      console.log('Query executada', { text, duration, rows: result.rowCount });
      return result;
    } catch (error) {
      console.error('Erro na query:', { text, error });
      throw error;
    }
  }

  async getClient() {
    return await this.pool.connect();
  }

  async close() {
    await this.pool.end();
  }
}
```

### Migrações

```typescript
// migrations/001_create_users_table.ts
export const up = async (db: Database) => {
  await db.query(`
    CREATE TABLE IF NOT EXISTS users (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      name VARCHAR(100) NOT NULL,
      email VARCHAR(255) UNIQUE NOT NULL,
      password_hash VARCHAR(255) NOT NULL,
      is_active BOOLEAN DEFAULT true,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
  `);

  await db.query(`
    CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    CREATE INDEX IF NOT EXISTS idx_users_active ON users(is_active);
  `);
};

export const down = async (db: Database) => {
  await db.query('DROP TABLE IF EXISTS users CASCADE;');
};
```

## 🧪 Testes

### Estrutura de Testes

```typescript
// tests/userService.test.ts
import { describe, it, expect, beforeEach, jest } from '@jest/globals';
import { UserService } from '../src/services/userService';
import { UserRepository } from '../src/repositories/userRepository';
import { CreateUserRequest } from '../src/types/user';

describe('UserService', () => {
  let userService: UserService;
  let mockUserRepository: jest.Mocked<UserRepository>;

  beforeEach(() => {
    mockUserRepository = {
      create: jest.fn(),
      findById: jest.fn(),
      findByEmail: jest.fn(),
      update: jest.fn(),
      delete: jest.fn(),
    } as any;

    userService = new UserService(mockUserRepository);
  });

  describe('createUser', () => {
    it('deve criar usuário com sucesso', async () => {
      // Given
      const userData: CreateUserRequest = {
        name: 'João Silva',
        email: 'joao@example.com',
      };
      
      const expectedUser = {
        id: 'user-123',
        name: 'João Silva',
        email: 'joao@example.com',
        createdAt: new Date(),
      };

      mockUserRepository.findByEmail.mockResolvedValue(null);
      mockUserRepository.create.mockResolvedValue(expectedUser);

      // When
      const result = await userService.createUser(userData);

      // Then
      expect(result).toEqual(expectedUser);
      expect(mockUserRepository.findByEmail).toHaveBeenCalledWith(userData.email);
      expect(mockUserRepository.create).toHaveBeenCalledWith(userData);
    });

    it('deve lançar erro quando email já existe', async () => {
      // Given
      const userData: CreateUserRequest = {
        name: 'João Silva',
        email: 'joao@example.com',
      };

      mockUserRepository.findByEmail.mockResolvedValue({
        id: 'existing-user',
        name: 'Usuário Existente',
        email: 'joao@example.com',
        createdAt: new Date(),
      });

      // When & Then
      await expect(userService.createUser(userData))
        .rejects
        .toThrow('Email já está em uso');
    });
  });
});
```

### Testes de Integração

```typescript
// tests/integration/user.test.ts
import request from 'supertest';
import { app } from '../src/app';
import { Database } from '../src/config/database';

describe('User API Integration Tests', () => {
  let db: Database;

  beforeAll(async () => {
    db = new Database();
    await db.query('DELETE FROM users'); // Limpar dados de teste
  });

  afterAll(async () => {
    await db.close();
  });

  describe('POST /api/users', () => {
    it('deve criar usuário com dados válidos', async () => {
      const userData = {
        name: 'Maria Silva',
        email: 'maria@example.com',
      };

      const response = await request(app)
        .post('/api/users')
        .send(userData)
        .expect(201);

      expect(response.body).toMatchObject({
        id: expect.any(String),
        name: userData.name,
        email: userData.email,
        createdAt: expect.any(String),
      });
    });

    it('deve retornar erro 400 para email inválido', async () => {
      const userData = {
        name: 'João Silva',
        email: 'email-invalido',
      };

      const response = await request(app)
        .post('/api/users')
        .send(userData)
        .expect(400);

      expect(response.body.error.message).toContain('Email inválido');
    });
  });
});
```

## 🔧 Ferramentas e Configuração

### ESLint e Prettier

```json
// .eslintrc.json
{
  "extends": [
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "no-console": "warn"
  }
}
```

### TypeScript Config

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

### Package.json Scripts

```json
{
  "scripts": {
    "dev": "nodemon src/server.ts",
    "build": "tsc",
    "start": "node dist/server.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src/**/*.ts",
    "lint:fix": "eslint src/**/*.ts --fix",
    "format": "prettier --write src/**/*.ts"
  }
}
```

## 📊 Logging e Monitoramento

### Winston Logger

```typescript
// utils/logger.ts
import winston from 'winston';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'user-api' },
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
  ],
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.simple()
    )
  }));
}

export default logger;
```

### Health Check

```typescript
// routes/health.ts
import { Router } from 'express';
import { Database } from '../config/database';

const router = Router();

router.get('/health', async (req, res) => {
  try {
    // Verificar conexão com banco
    await db.query('SELECT 1');
    
    res.status(200).json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      memory: process.memoryUsage(),
    });
  } catch (error) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message,
    });
  }
});

export default router;
```

## 🚫 Anti-Padrões

### ❌ Evite

```typescript
// ❌ Callback hell
fs.readFile(file1, (err1, data1) => {
  fs.readFile(file2, (err2, data2) => {
    fs.readFile(file3, (err3, data3) => {
      // callback hell
    });
  });
});

// ❌ Promises não tratadas
createUser(userData); // Sem await ou .catch()

// ❌ Tratamento genérico de erros
try {
  // código
} catch (error) {
  console.log(error); // Muito genérico
}

// ❌ Módulos muito grandes
// user-service.ts com 500+ linhas
```

### ✅ Faça

```typescript
// ✅ Async/await
async function processFiles() {
  try {
    const [data1, data2, data3] = await Promise.all([
      fs.promises.readFile(file1),
      fs.promises.readFile(file2),
      fs.promises.readFile(file3),
    ]);
    
    return { data1, data2, data3 };
  } catch (error) {
    logger.error('Erro ao processar arquivos:', error);
    throw error;
  }
}

// ✅ Tratamento adequado de promises
try {
  const user = await createUser(userData);
  return user;
} catch (error) {
  if (error instanceof ValidationError) {
    throw new BadRequestError(error.message);
  }
  throw new InternalServerError('Erro interno do servidor');
}

// ✅ Tratamento específico de erros
try {
  const user = await userService.getUser(id);
  return user;
} catch (error) {
  if (error instanceof UserNotFoundError) {
    throw new NotFoundError('Usuário não encontrado');
  }
  throw error;
}

// ✅ Módulos pequenos e focados
// user-service.ts com responsabilidades específicas
// user-validator.ts para validações
// user-repository.ts para acesso a dados
```

## 📚 Recursos Adicionais

- [Documentação Node.js Oficial](https://nodejs.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Express.js Guide](https://expressjs.com/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Winston Logger](https://github.com/winstonjs/winston)

---

**Lembre-se**: Foque em código limpo, testável e bem tipado. Use async/await para operações assíncronas e sempre trate erros adequadamente. Mantenha módulos pequenos e com responsabilidades claras.
