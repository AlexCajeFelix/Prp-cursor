# [Nome da API Service]

**Tipo:** Serviço de API REST/GraphQL
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [X horas]
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
[Descreva claramente o que a API fará, quais dados manipulará e qual problema resolve]

### Objetivos
- [Objetivo principal da API]
- [Objetivos secundários]
- [Métricas de performance esperadas]

### Justificativa
[Por que esta API é necessária? Qual problema ela resolve? Quem a utilizará?]

## ⚙️ Requisitos Funcionais

### Endpoints Principais
1. **[Endpoint 1 - Nome Descritivo]**
   - **Método:** [GET/POST/PUT/DELETE]
   - **Rota:** `/api/v1/[rota]`
   - **Descrição:** [O que este endpoint faz]
   - **Parâmetros:** [Query params, path params, body]
   - **Resposta:** [Estrutura da resposta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

2. **[Endpoint 2 - Nome Descritivo]**
   - **Método:** [GET/POST/PUT/DELETE]
   - **Rota:** `/api/v1/[rota]`
   - **Descrição:** [O que este endpoint faz]
   - **Parâmetros:** [Query params, path params, body]
   - **Resposta:** [Estrutura da resposta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

3. **[Endpoint 3 - Nome Descritivo]**
   - **Método:** [GET/POST/PUT/DELETE]
   - **Rota:** `/api/v1/[rota]`
   - **Descrição:** [O que este endpoint faz]
   - **Parâmetros:** [Query params, path params, body]
   - **Resposta:** [Estrutura da resposta]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

### Autenticação e Autorização
- **Método:** [JWT/OAuth2/API Key/Bearer Token]
- **Níveis de acesso:** [Público/Autenticado/Admin]
- **Rate limiting:** [Limites por IP/usuário]

### Validação de Dados
- **Input validation:** [Biblioteca de validação]
- **Sanitização:** [Métodos de sanitização]
- **Schema validation:** [JSON Schema/joi/yup]

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Runtime:** [Node.js/Python/Java/.NET + versões]
- **Framework:** [Express/FastAPI/Spring Boot/.NET Core + versões]
- **Banco de Dados:** [PostgreSQL/MySQL/MongoDB + versões]
- **ORM/ODM:** [Prisma/TypeORM/Mongoose/Entity Framework + versões]
- **Cache:** [Redis/Memcached + versões]
- **Message Queue:** [RabbitMQ/Apache Kafka + versões]

### Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   API Gateway   │    │   Database      │
│                 │◄──►│                 │◄──►│   (Primary)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   API Service   │◄──►│   Cache Layer   │
                       │   (This App)    │    │   (Redis)       │
                       └─────────────────┘    └─────────────────┘
```

### Padrões de Código
- **Linguagem:** [TypeScript/JavaScript/Python/Java/C# + versão]
- **Framework:** [Express/FastAPI/Spring Boot/.NET Core + versão]
- **Convenções:** [ESLint/Black/Checkstyle configurados]
- **Testes:** [Jest/Mocha/pytest/JUnit + versões]
- **Documentação:** [Swagger/OpenAPI 3.0]
- **Logging:** [Winston/Pino/Log4j + versões]

## 📁 Estrutura de Arquivos

```
api-service/
├── src/
│   ├── controllers/        # Controladores das rotas
│   │   ├── auth/          # Autenticação
│   │   ├── users/         # Gerenciamento de usuários
│   │   └── [entity]/      # Entidades específicas
│   ├── services/          # Lógica de negócio
│   │   ├── auth/          # Serviços de autenticação
│   │   ├── users/         # Serviços de usuários
│   │   └── [entity]/      # Serviços específicos
│   ├── models/            # Modelos de dados
│   │   ├── User.ts        # Modelo de usuário
│   │   ├── [Entity].ts    # Outras entidades
│   │   └── index.ts       # Exportações
│   ├── middleware/        # Middlewares customizados
│   │   ├── auth.ts        # Middleware de autenticação
│   │   ├── validation.ts  # Validação de dados
│   │   ├── error.ts       # Tratamento de erros
│   │   └── logging.ts     # Logging
│   ├── routes/            # Definição de rotas
│   │   ├── auth.ts        # Rotas de autenticação
│   │   ├── users.ts       # Rotas de usuários
│   │   └── index.ts       # Router principal
│   ├── utils/             # Utilitários
│   │   ├── database.ts    # Conexão com banco
│   │   ├── cache.ts       # Gerenciamento de cache
│   │   ├── crypto.ts      # Funções criptográficas
│   │   └── helpers.ts     # Funções auxiliares
│   ├── types/             # Definições de tipos
│   └── config/            # Configurações
│       ├── database.ts    # Config do banco
│       ├── auth.ts        # Config de autenticação
│       └── app.ts         # Config da aplicação
├── tests/                 # Testes automatizados
│   ├── unit/             # Testes unitários
│   ├── integration/      # Testes de integração
│   └── e2e/              # Testes end-to-end
├── docs/                 # Documentação
│   ├── api/              # Documentação da API
│   └── deployment/       # Guias de deploy
├── migrations/           # Migrações do banco
├── seeds/                # Dados iniciais
└── scripts/              # Scripts auxiliares
```

## 📦 Entregáveis Esperados

### Código
- [ ] Estrutura de pastas criada
- [ ] Configuração do servidor implementada
- [ ] Middlewares essenciais configurados
- [ ] Modelos de dados definidos
- [ ] Controladores implementados
- [ ] Serviços de negócio criados
- [ ] Sistema de autenticação implementado
- [ ] Validação de dados configurada
- [ ] Tratamento de erros padronizado
- [ ] Sistema de logging implementado

### Funcionalidades
- [ ] [Endpoint 1] implementado e funcionando
- [ ] [Endpoint 2] implementado e funcionando
- [ ] [Endpoint 3] implementado e funcionando
- [ ] Autenticação e autorização funcionando
- [ ] Validação de dados implementada
- [ ] Rate limiting configurado
- [ ] CORS configurado adequadamente
- [ ] Health check endpoint funcionando

### Testes
- [ ] Testes unitários para serviços principais
- [ ] Testes de integração para endpoints
- [ ] Testes de autenticação e autorização
- [ ] Testes de validação de dados
- [ ] Testes de tratamento de erros
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
- [ ] Código limpo e bem estruturado
- [ ] Separação clara de responsabilidades
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções de linting
- [ ] Sem código duplicado
- [ ] Tratamento adequado de exceções

### Performance
- [ ] Tempo de resposta < 200ms para operações simples
- [ ] Tempo de resposta < 1s para operações complexas
- [ ] Cache implementado onde apropriado
- [ ] Otimização de queries no banco
- [ ] Compressão de respostas habilitada
- [ ] Connection pooling configurado

### Segurança
- [ ] Autenticação robusta implementada
- [ ] Autorização baseada em roles/permissões
- [ ] Validação rigorosa de inputs
- [ ] Sanitização de dados
- [ ] Proteção contra SQL injection
- [ ] Rate limiting implementado
- [ ] HTTPS obrigatório
- [ ] Headers de segurança configurados

### Observabilidade
- [ ] Logs estruturados implementados
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
- [ ] Cache distribuído (se aplicável)
- [ ] Message queuing (se necessário)

## 📚 Exemplos e Referências

### Exemplos de Endpoints
```typescript
// Exemplo de controller
import { Request, Response } from 'express';
import { UserService } from '../services/UserService';
import { validateCreateUser } from '../middleware/validation';

export class UserController {
  constructor(private userService: UserService) {}

  async createUser(req: Request, res: Response): Promise<void> {
    try {
      const userData = req.body;
      const user = await this.userService.createUser(userData);
      
      res.status(201).json({
        success: true,
        data: user,
        message: 'Usuário criado com sucesso'
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        error: 'Erro interno do servidor'
      });
    }
  }
}
```

### Referências
- [OpenAPI Specification](https://swagger.io/specification/)
- [REST API Best Practices](https://restfulapi.net/)
- [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security/)
- [Database Design Best Practices](https://www.postgresql.org/docs/current/ddl.html)

## 🔄 Considerações Adicionais

### Deploy e Infraestrutura
- [ ] Configuração para deploy em [AWS/GCP/Azure]
- [ ] Dockerfile e docker-compose criados
- [ ] Variáveis de ambiente documentadas
- [ ] Pipeline de CI/CD configurado
- [ ] Monitoramento de produção implementado

### Versionamento
- [ ] Versionamento da API implementado
- [ ] Backward compatibility considerada
- [ ] Migration strategy definida
- [ ] Deprecation policy documentada

### Backup e Recuperação
- [ ] Estratégia de backup do banco de dados
- [ ] Procedimentos de recuperação documentados
- [ ] Disaster recovery plan
- [ ] Data retention policy definida
