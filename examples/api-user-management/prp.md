# User Management API

**Tipo:** Serviço de API REST
**Complexidade:** Média
**Tempo Estimado:** 12 horas
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
API REST para gerenciamento completo de usuários em um sistema de aplicação web. A API fornece endpoints para autenticação, CRUD de usuários, gerenciamento de perfis e funcionalidades de segurança como recuperação de senha e verificação de email.

### Objetivos
- Fornecer API REST robusta para gerenciamento de usuários
- Implementar sistema de autenticação JWT seguro
- Permitir operações CRUD completas de usuários
- Implementar funcionalidades de segurança avançadas
- Garantir alta disponibilidade e performance

### Justificativa
Sistemas modernos precisam de uma base sólida de gerenciamento de usuários que seja segura, escalável e fácil de integrar. Esta API serve como base para qualquer aplicação que precise gerenciar usuários de forma profissional.

## ⚙️ Requisitos Funcionais

### Endpoints Principais
1. **Autenticação de Usuários**
   - **Método:** POST
   - **Rota:** `/api/v1/auth/login`
   - **Descrição:** Autentica usuário com email e senha
   - **Parâmetros:** `{ email: string, password: string }`
   - **Resposta:** `{ token: string, user: User, expiresIn: number }`
   - **Critérios de aceitação:**
     - [ ] Valida credenciais corretas
     - [ ] Retorna JWT token válido
     - [ ] Retorna dados do usuário (sem senha)
     - [ ] Rejeita credenciais inválidas
     - [ ] Implementa rate limiting

2. **Registro de Usuários**
   - **Método:** POST
   - **Rota:** `/api/v1/auth/register`
   - **Descrição:** Cria novo usuário no sistema
   - **Parâmetros:** `{ name: string, email: string, password: string }`
   - **Resposta:** `{ user: User, message: string }`
   - **Critérios de aceitação:**
     - [ ] Valida formato de email único
     - [ ] Valida força da senha
     - [ ] Hash da senha com bcrypt
     - [ ] Envia email de verificação
     - [ ] Previne duplicação de emails

3. **Gerenciamento de Perfil**
   - **Método:** GET/PUT
   - **Rota:** `/api/v1/users/profile`
   - **Descrição:** Obtém e atualiza perfil do usuário autenticado
   - **Parâmetros:** `{ name?: string, email?: string, bio?: string }`
   - **Resposta:** `{ user: User }`
   - **Critérios de aceitação:**
     - [ ] Requer autenticação JWT
     - [ ] Permite atualização de dados pessoais
     - [ ] Valida novos dados antes de salvar
     - [ ] Retorna dados atualizados
     - [ ] Protege dados sensíveis

4. **Recuperação de Senha**
   - **Método:** POST
   - **Rota:** `/api/v1/auth/forgot-password`
   - **Descrição:** Inicia processo de recuperação de senha
   - **Parâmetros:** `{ email: string }`
   - **Resposta:** `{ message: string }`
   - **Critérios de aceitação:**
     - [ ] Valida existência do email
     - [ ] Gera token de reset único
     - [ ] Envia email com link de reset
     - [ ] Token expira em 1 hora
     - [ ] Não revela se email existe

5. **Reset de Senha**
   - **Método:** POST
   - **Rota:** `/api/v1/auth/reset-password`
   - **Descrição:** Define nova senha usando token de reset
   - **Parâmetros:** `{ token: string, newPassword: string }`
   - **Resposta:** `{ message: string }`
   - **Critérios de aceitação:**
     - [ ] Valida token de reset
     - [ ] Valida nova senha
     - [ ] Atualiza senha no banco
     - [ ] Invalida token após uso
     - [ ] Força novo login

### Autenticação e Autorização
- **Método:** JWT (JSON Web Tokens)
- **Níveis de acesso:** Público, Autenticado, Admin
- **Rate limiting:** 100 requests/min por IP, 10 requests/min para auth

### Validação de Dados
- **Input validation:** Joi para validação de schemas
- **Sanitização:** Sanitização automática de inputs
- **Schema validation:** Schemas Joi para todos os endpoints

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Runtime:** Node.js 20.0
- **Framework:** Express 4.18
- **Banco de Dados:** MongoDB 6.0
- **ORM/ODM:** Mongoose 7.0
- **Cache:** Redis 7.0
- **Message Queue:** Bull Queue (Redis-based)

### Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   Express API   │    │   MongoDB       │
│   (Nginx)       │◄──►│   Server        │◄──►│   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Redis Cache   │    │   Email Queue   │
                       │   & Sessions    │    │   (Bull)        │
                       └─────────────────┘    └─────────────────┘
```

### Padrões de Código
- **Linguagem:** TypeScript 5.0
- **Framework:** Express 4.18
- **Convenções:** ESLint + Prettier configurados
- **Testes:** Jest + Supertest
- **Documentação:** Swagger/OpenAPI 3.0
- **Logging:** Winston
- **Validation:** Joi
- **Security:** Helmet, bcrypt, jsonwebtoken

## 📁 Estrutura de Arquivos

```
user-management-api/
├── src/
│   ├── controllers/        # Controladores das rotas
│   │   ├── authController.ts
│   │   ├── userController.ts
│   │   └── index.ts
│   ├── services/          # Lógica de negócio
│   │   ├── authService.ts
│   │   ├── userService.ts
│   │   ├── emailService.ts
│   │   └── tokenService.ts
│   ├── models/            # Modelos de dados
│   │   ├── User.ts
│   │   ├── Token.ts
│   │   └── index.ts
│   ├── middleware/        # Middlewares customizados
│   │   ├── auth.ts
│   │   ├── validation.ts
│   │   ├── errorHandler.ts
│   │   ├── rateLimiter.ts
│   │   └── logging.ts
│   ├── routes/            # Definição de rotas
│   │   ├── auth.ts
│   │   ├── users.ts
│   │   └── index.ts
│   ├── utils/             # Utilitários
│   │   ├── database.ts
│   │   ├── redis.ts
│   │   ├── jwt.ts
│   │   ├── bcrypt.ts
│   │   └── validation.ts
│   ├── types/             # Definições de tipos
│   │   ├── auth.ts
│   │   ├── user.ts
│   │   └── api.ts
│   ├── config/            # Configurações
│   │   ├── database.ts
│   │   ├── redis.ts
│   │   ├── jwt.ts
│   │   └── app.ts
│   └── app.ts             # Configuração da aplicação
├── tests/                 # Testes automatizados
│   ├── unit/             # Testes unitários
│   ├── integration/      # Testes de integração
│   └── e2e/              # Testes end-to-end
├── docs/                 # Documentação
│   ├── api/              # Documentação da API
│   └── deployment/       # Guias de deploy
├── scripts/              # Scripts auxiliares
│   ├── seed.js           # Dados iniciais
│   └── migrate.js        # Migrações
└── docker/               # Configurações Docker
    ├── Dockerfile
    └── docker-compose.yml
```

## 📦 Entregáveis Esperados

### Código
- [ ] Estrutura de pastas criada
- [ ] Configuração do servidor Express implementada
- [ ] Middlewares essenciais configurados (auth, validation, error)
- [ ] Modelos de dados Mongoose criados
- [ ] Controladores implementados
- [ ] Serviços de negócio criados
- [ ] Sistema de autenticação JWT implementado
- [ ] Validação de dados com Joi configurada
- [ ] Tratamento de erros padronizado
- [ ] Sistema de logging com Winston implementado

### Funcionalidades
- [ ] Endpoint de login funcionando
- [ ] Endpoint de registro funcionando
- [ ] Gerenciamento de perfil implementado
- [ ] Recuperação de senha implementada
- [ ] Reset de senha funcionando
- [ ] Rate limiting configurado
- [ ] CORS configurado adequadamente
- [ ] Health check endpoint funcionando
- [ ] Validação de dados rigorosa
- [ ] Cache Redis implementado

### Testes
- [ ] Testes unitários para serviços principais
- [ ] Testes de integração para endpoints
- [ ] Testes de autenticação e autorização
- [ ] Testes de validação de dados
- [ ] Testes de rate limiting
- [ ] Testes de recuperação de senha
- [ ] Cobertura de testes >= 80%

### Documentação
- [ ] Documentação Swagger/OpenAPI completa
- [ ] README com instruções de instalação
- [ ] Guia de desenvolvimento
- [ ] Documentação dos endpoints
- [ ] Exemplos de uso da API
- [ ] Guia de deploy

## ✅ Critérios de Qualidade

### Código
- [ ] Código TypeScript bem tipado
- [ ] Separação clara de responsabilidades
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções de linting
- [ ] Sem código duplicado
- [ ] Tratamento adequado de exceções

### Performance
- [ ] Tempo de resposta < 100ms para operações simples
- [ ] Tempo de resposta < 500ms para operações complexas
- [ ] Cache Redis implementado onde apropriado
- [ ] Otimização de queries no MongoDB
- [ ] Connection pooling configurado
- [ ] Compressão de respostas habilitada

### Segurança
- [ ] Autenticação JWT robusta implementada
- [ ] Senhas hasheadas com bcrypt
- [ ] Validação rigorosa de inputs
- [ ] Sanitização de dados
- [ ] Rate limiting implementado
- [ ] HTTPS obrigatório
- [ ] Headers de segurança configurados
- [ ] Proteção contra ataques comuns

### Observabilidade
- [ ] Logs estruturados com Winston
- [ ] Métricas de performance coletadas
- [ ] Health checks implementados
- [ ] Error tracking configurado
- [ ] Monitoring de recursos
- [ ] Alertas configurados

### Escalabilidade
- [ ] Stateless design
- [ ] Configuração via variáveis de ambiente
- [ ] Suporte a horizontal scaling
- [ ] Database connection pooling
- [ ] Cache distribuído com Redis
- [ ] Message queuing para emails

## 📚 Exemplos e Referências

### Exemplo de Controller de Autenticação
```typescript
// src/controllers/authController.ts
import { Request, Response } from 'express';
import { AuthService } from '../services/authService';
import { validateLogin, validateRegister } from '../middleware/validation';

export class AuthController {
  constructor(private authService: AuthService) {}

  async login(req: Request, res: Response): Promise<void> {
    try {
      const { email, password } = req.body;
      
      const result = await this.authService.login(email, password);
      
      res.json({
        success: true,
        data: {
          token: result.token,
          user: result.user,
          expiresIn: result.expiresIn
        }
      });
    } catch (error) {
      res.status(401).json({
        success: false,
        error: 'Credenciais inválidas'
      });
    }
  }

  async register(req: Request, res: Response): Promise<void> {
    try {
      const { name, email, password } = req.body;
      
      const user = await this.authService.register({ name, email, password });
      
      res.status(201).json({
        success: true,
        data: user,
        message: 'Usuário criado com sucesso'
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        error: error.message
      });
    }
  }

  async forgotPassword(req: Request, res: Response): Promise<void> {
    try {
      const { email } = req.body;
      
      await this.authService.forgotPassword(email);
      
      res.json({
        success: true,
        message: 'Email de recuperação enviado'
      });
    } catch (error) {
      // Sempre retorna sucesso para não revelar se email existe
      res.json({
        success: true,
        message: 'Email de recuperação enviado'
      });
    }
  }
}
```

### Exemplo de Modelo de Usuário
```typescript
// src/models/User.ts
import mongoose, { Document, Schema } from 'mongoose';
import bcrypt from 'bcryptjs';

export interface IUser extends Document {
  name: string;
  email: string;
  password: string;
  isEmailVerified: boolean;
  lastLogin?: Date;
  createdAt: Date;
  updatedAt: Date;
  comparePassword(candidatePassword: string): Promise<boolean>;
}

const UserSchema = new Schema<IUser>({
  name: {
    type: String,
    required: [true, 'Nome é obrigatório'],
    trim: true,
    minlength: [2, 'Nome deve ter pelo menos 2 caracteres'],
    maxlength: [50, 'Nome deve ter no máximo 50 caracteres']
  },
  email: {
    type: String,
    required: [true, 'Email é obrigatório'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
      'Email deve ter formato válido'
    ]
  },
  password: {
    type: String,
    required: [true, 'Senha é obrigatória'],
    minlength: [8, 'Senha deve ter pelo menos 8 caracteres'],
    select: false // Não incluir senha em queries por padrão
  },
  isEmailVerified: {
    type: Boolean,
    default: false
  },
  lastLogin: {
    type: Date
  }
}, {
  timestamps: true
});

// Hash da senha antes de salvar
UserSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  
  try {
    const salt = await bcrypt.genSalt(12);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// Método para comparar senhas
UserSchema.methods.comparePassword = async function(candidatePassword: string): Promise<boolean> {
  return bcrypt.compare(candidatePassword, this.password);
};

// Índices para performance
UserSchema.index({ email: 1 });
UserSchema.index({ createdAt: -1 });

export const User = mongoose.model<IUser>('User', UserSchema);
```

### Referências
- [Express.js Documentation](https://expressjs.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [JWT.io](https://jwt.io/)
- [Joi Validation](https://joi.dev/)

## 🔄 Considerações Adicionais

### Deploy e Infraestrutura
- [ ] Configuração para deploy em AWS/GCP/Azure
- [ ] Dockerfile e docker-compose criados
- [ ] Variáveis de ambiente documentadas
- [ ] Pipeline de CI/CD configurado
- [ ] Monitoramento de produção implementado

### Versionamento
- [ ] Versionamento da API implementado (/api/v1/)
- [ ] Backward compatibility considerada
- [ ] Migration strategy definida
- [ ] Deprecation policy documentada

### Backup e Recuperação
- [ ] Estratégia de backup do MongoDB
- [ ] Procedimentos de recuperação documentados
- [ ] Disaster recovery plan
- [ ] Data retention policy definida

### Compliance
- [ ] GDPR compliance (se aplicável)
- [ ] Audit trail implementado
- [ ] Data encryption at rest
- [ ] Secure password policies
