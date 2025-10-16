# [Nome do Microserviço]

**Tipo:** Microserviço
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [X horas]
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
[Descreva claramente o que este microserviço fará, qual domínio de negócio atende e como se integra com outros serviços]

### Objetivos
- [Objetivo principal do microserviço]
- [Objetivos de integração]
- [Objetivos de performance]

### Justificativa
[Por que este microserviço é necessário? Qual problema resolve? Como contribui para a arquitetura geral?]

## ⚙️ Requisitos Funcionais

### Funcionalidades Principais
1. **[Funcionalidade Principal 1]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Input:** [Dados de entrada]
   - **Output:** [Dados de saída]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

2. **[Funcionalidade Principal 2]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Input:** [Dados de entrada]
   - **Output:** [Dados de saída]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

3. **[Funcionalidade Principal 3]**
   - **Descrição:** [O que esta funcionalidade faz]
   - **Input:** [Dados de entrada]
   - **Output:** [Dados de saída]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

### Integrações
- **Serviços Consumidos:** [Lista de serviços que este microserviço consome]
- **Serviços Clientes:** [Lista de serviços que consomem este microserviço]
- **APIs Externas:** [APIs de terceiros utilizadas]
- **Message Queues:** [Filas de mensagens utilizadas]

### Comunicação
- **Protocolo:** [HTTP/REST, GraphQL, gRPC, Message Queue]
- **Formato de Dados:** [JSON, Protocol Buffers, XML]
- **Autenticação:** [JWT, OAuth2, API Key, mTLS]

## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Runtime:** [Node.js/Python/Java/Go/.NET + versões]
- **Framework:** [Express/FastAPI/Spring Boot/Gin/ASP.NET Core + versões]
- **Banco de Dados:** [PostgreSQL/MySQL/MongoDB + versões]
- **Message Queue:** [RabbitMQ/Apache Kafka/Redis + versões]
- **Cache:** [Redis/Memcached + versões]
- **Service Discovery:** [Consul/Eureka/Kubernetes DNS]

### Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   API Gateway   │    │   Load Balancer │    │   Service       │
│                 │◄──►│                 │◄──►│   Registry      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Microservice  │
                       │   (This Service)│
                       └─────────────────┘
                              │
                              ▼
         ┌─────────────────┬─────────────────┬─────────────────┐
         │   Database      │   Message       │   Cache         │
         │                 │   Queue         │   Layer         │
         └─────────────────┴─────────────────┴─────────────────┘
```

### Padrões de Código
- **Linguagem:** [TypeScript/JavaScript/Python/Java/Go/C# + versão]
- **Framework:** [Express/FastAPI/Spring Boot/Gin/ASP.NET Core + versão]
- **Convenções:** [ESLint/Black/Checkstyle configurados]
- **Testes:** [Jest/Mocha/pytest/JUnit + versões]
- **Documentação:** [Swagger/OpenAPI 3.0]
- **Logging:** [Winston/Pino/Log4j + versões]
- **Monitoring:** [Prometheus/Grafana/New Relic]

## 📁 Estrutura de Arquivos

```
microservice/
├── src/
│   ├── controllers/        # Controladores das rotas
│   │   ├── health.ts       # Health check
│   │   ├── [feature].ts    # Controladores específicos
│   │   └── index.ts        # Router principal
│   ├── services/          # Lógica de negócio
│   │   ├── [domain]/       # Serviços por domínio
│   │   ├── external/       # Integrações externas
│   │   └── messaging/      # Processamento de mensagens
│   ├── models/            # Modelos de dados
│   │   ├── entities/       # Entidades de domínio
│   │   ├── dtos/          # Data Transfer Objects
│   │   └── schemas/       # Schemas de validação
│   ├── infrastructure/    # Camada de infraestrutura
│   │   ├── database/       # Configuração do banco
│   │   ├── messaging/      # Configuração de mensageria
│   │   ├── cache/          # Configuração de cache
│   │   └── monitoring/     # Configuração de monitoramento
│   ├── middleware/        # Middlewares customizados
│   │   ├── auth.ts         # Autenticação
│   │   ├── validation.ts   # Validação
│   │   ├── error.ts        # Tratamento de erros
│   │   ├── logging.ts      # Logging
│   │   └── rate-limit.ts   # Rate limiting
│   ├── config/            # Configurações
│   │   ├── app.ts          # Config da aplicação
│   │   ├── database.ts     # Config do banco
│   │   ├── messaging.ts    # Config de mensageria
│   │   └── monitoring.ts   # Config de monitoramento
│   └── utils/             # Utilitários
│       ├── logger.ts       # Logger
│       ├── validator.ts    # Validador
│       └── helpers.ts      # Funções auxiliares
├── tests/                 # Testes automatizados
│   ├── unit/             # Testes unitários
│   ├── integration/      # Testes de integração
│   ├── e2e/              # Testes end-to-end
│   └── load/             # Testes de carga
├── k8s/                  # Configurações Kubernetes
│   ├── deployment.yaml   # Deployment
│   ├── service.yaml      # Service
│   ├── configmap.yaml    # ConfigMap
│   └── ingress.yaml      # Ingress
├── docker/               # Configurações Docker
│   ├── Dockerfile        # Dockerfile
│   ├── docker-compose.yml # Compose para desenvolvimento
│   └── .dockerignore     # Arquivos ignorados
├── scripts/              # Scripts auxiliares
│   ├── deploy.sh         # Script de deploy
│   ├── test.sh           # Script de testes
│   └── migrate.sh        # Script de migração
└── docs/                 # Documentação
    ├── api/              # Documentação da API
    ├── architecture/     # Documentação arquitetural
    └── deployment/       # Guias de deploy
```

## 📦 Entregáveis Esperados

### Código
- [ ] Estrutura de pastas criada
- [ ] Configuração do servidor implementada
- [ ] Middlewares essenciais configurados
- [ ] Modelos de dados definidos
- [ ] Controladores implementados
- [ ] Serviços de domínio criados
- [ ] Integrações externas implementadas
- [ ] Sistema de mensageria configurado
- [ ] Cache implementado
- [ ] Monitoramento configurado

### Funcionalidades
- [ ] [Funcionalidade 1] implementada e funcionando
- [ ] [Funcionalidade 2] implementada e funcionando
- [ ] [Funcionalidade 3] implementada e funcionando
- [ ] Health check endpoint funcionando
- [ ] Métricas de observabilidade expostas
- [ ] Circuit breaker implementado
- [ ] Retry mechanism configurado
- [ ] Graceful shutdown implementado

### Testes
- [ ] Testes unitários para serviços principais
- [ ] Testes de integração para APIs
- [ ] Testes de contratos (Contract Testing)
- [ ] Testes de carga e performance
- [ ] Testes de falha (Chaos Engineering)
- [ ] Cobertura de testes >= 80%

### Infraestrutura
- [ ] Dockerfile otimizado criado
- [ ] Configurações Kubernetes criadas
- [ ] CI/CD pipeline configurado
- [ ] Monitoring e alerting configurados
- [ ] Logs centralizados implementados
- [ ] Tracing distribuído configurado

### Documentação
- [ ] Documentação Swagger/OpenAPI completa
- [ ] README com instruções de instalação
- [ ] Guia de desenvolvimento
- [ ] Documentação arquitetural
- [ ] Runbooks operacionais
- [ ] Guia de troubleshooting

## ✅ Critérios de Qualidade

### Código
- [ ] Código limpo e bem estruturado
- [ ] Princípios SOLID aplicados
- [ ] Design patterns apropriados utilizados
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções de linting
- [ ] Sem código duplicado
- [ ] Tratamento adequado de exceções

### Performance
- [ ] Tempo de resposta < 100ms para operações simples
- [ ] Tempo de resposta < 500ms para operações complexas
- [ ] Throughput adequado para carga esperada
- [ ] Cache implementado onde apropriado
- [ ] Connection pooling configurado
- [ ] Otimização de recursos

### Confiabilidade
- [ ] Circuit breaker implementado
- [ ] Retry mechanism configurado
- [ ] Timeout adequado configurado
- [ ] Graceful degradation implementado
- [ ] Bulkhead pattern aplicado
- [ ] Chaos engineering testado

### Observabilidade
- [ ] Logs estruturados implementados
- [ ] Métricas de negócio e técnica coletadas
- [ ] Health checks implementados
- [ ] Distributed tracing configurado
- [ ] Error tracking implementado
- [ ] Performance monitoring ativo

### Segurança
- [ ] Autenticação robusta implementada
- [ ] Autorização baseada em roles/permissões
- [ ] Validação rigorosa de inputs
- [ ] Sanitização de dados
- [ ] Rate limiting implementado
- [ ] HTTPS obrigatório
- [ ] Secrets management configurado

### Escalabilidade
- [ ] Stateless design
- [ ] Horizontal scaling suportado
- [ ] Database sharding (se necessário)
- [ ] Message queuing para async processing
- [ ] Cache distribuído
- [ ] Auto-scaling configurado

## 📚 Exemplos e Referências

### Exemplo de Service Principal
```typescript
// Exemplo de serviço de domínio
import { Injectable } from '@nestjs/common';
import { EventEmitter2 } from '@nestjs/event-emitter';
import { Logger } from '@nestjs/common';

@Injectable()
export class OrderService {
  private readonly logger = new Logger(OrderService.name);

  constructor(
    private readonly orderRepository: OrderRepository,
    private readonly paymentService: PaymentService,
    private readonly eventEmitter: EventEmitter2
  ) {}

  async createOrder(orderData: CreateOrderDTO): Promise<Order> {
    try {
      this.logger.log('Creating new order', { userId: orderData.userId });
      
      // Validar dados
      await this.validateOrderData(orderData);
      
      // Criar order
      const order = await this.orderRepository.create(orderData);
      
      // Processar pagamento
      const payment = await this.paymentService.processPayment({
        orderId: order.id,
        amount: order.total,
        method: orderData.paymentMethod
      });
      
      // Emitir evento
      this.eventEmitter.emit('order.created', {
        orderId: order.id,
        userId: order.userId,
        total: order.total
      });
      
      this.logger.log('Order created successfully', { orderId: order.id });
      return order;
      
    } catch (error) {
      this.logger.error('Failed to create order', error);
      throw error;
    }
  }
}
```

### Referências
- [Microservices Patterns](https://microservices.io/)
- [12-Factor App](https://12factor.net/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Prometheus Monitoring](https://prometheus.io/docs/)
- [Distributed Tracing](https://opentelemetry.io/docs/)

## 🔄 Considerações Adicionais

### Service Mesh
- [ ] Istio/Linkerd configurado (se aplicável)
- [ ] Service-to-service communication segura
- [ ] Traffic management implementado
- [ ] Observabilidade centralizada

### Data Management
- [ ] Database per service implementado
- [ ] Event sourcing (se aplicável)
- [ ] CQRS pattern (se aplicável)
- [ ] Saga pattern para transações distribuídas

### Deployment Strategy
- [ ] Blue-green deployment configurado
- [ ] Canary deployment implementado
- [ ] Rolling updates configurados
- [ ] Rollback procedures testadas

### Disaster Recovery
- [ ] Backup strategies implementadas
- [ ] Multi-region deployment (se necessário)
- [ ] Failover procedures documentadas
- [ ] RTO/RPO definidos e testados
