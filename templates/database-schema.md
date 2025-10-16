# [Nome do Schema de Banco de Dados]

**Tipo:** Schema de Banco de Dados
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [X horas]
**Versão:** 1.0

## 🎯 Contexto do Projeto

### Descrição Geral
[Descreva claramente qual sistema de dados será modelado, quais entidades principais existem e qual problema o banco resolve]

### Objetivos
- [Objetivo principal do schema]
- [Objetivos de performance]
- [Objetivos de escalabilidade]

### Justificativa
[Por que este schema é necessário? Quais dados precisam ser armazenados? Como será utilizado?]

## ⚙️ Requisitos Funcionais

### Entidades Principais
1. **[Entidade 1 - Nome Descritivo]**
   - **Descrição:** [O que esta entidade representa]
   - **Propósito:** [Para que será usada]
   - **Relacionamentos:** [Como se relaciona com outras entidades]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

2. **[Entidade 2 - Nome Descritivo]**
   - **Descrição:** [O que esta entidade representa]
   - **Propósito:** [Para que será usada]
   - **Relacionamentos:** [Como se relaciona com outras entidades]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

3. **[Entidade 3 - Nome Descritivo]**
   - **Descrição:** [O que esta entidade representa]
   - **Propósito:** [Para que será usada]
   - **Relacionamentos:** [Como se relaciona com outras entidades]
   - **Critérios de aceitação:**
     - [ ] [Critério 1]
     - [ ] [Critério 2]
     - [ ] [Critério 3]

### Relacionamentos
- **[Relacionamento 1]:** [Tipo: 1:1, 1:N, N:N] entre [Entidade A] e [Entidade B]
- **[Relacionamento 2]:** [Tipo: 1:1, 1:N, N:N] entre [Entidade C] e [Entidade D]
- **[Relacionamento 3]:** [Tipo: 1:1, 1:N, N:N] entre [Entidade E] e [Entidade F]

### Operações Principais
- **Inserção:** [Quais dados serão inseridos frequentemente]
- **Consulta:** [Quais consultas serão mais comuns]
- **Atualização:** [Quais dados serão atualizados frequentemente]
- **Exclusão:** [Política de exclusão de dados]

## 🔧 Requisitos Técnicos

### Sistema de Banco de Dados
- **Tipo:** [PostgreSQL/MySQL/MongoDB/SQLite + versão]
- **Versão:** [Versão específica]
- **Encoding:** [UTF-8/Latin1/etc]
- **Collation:** [Collation específica]

### Arquitetura de Dados
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │    │   Database      │    │   Backup        │
│   Layer         │◄──►│   Server        │◄──►│   System        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Read          │
                       │   Replicas      │
                       └─────────────────┘
```

### Padrões de Implementação
- **ORM/ODM:** [Prisma/TypeORM/Mongoose/Entity Framework + versão]
- **Migrations:** [Sistema de migração utilizado]
- **Constraints:** [Tipos de constraints implementados]
- **Indexes:** [Estratégia de indexação]
- **Triggers:** [Triggers necessários]

## 📁 Estrutura de Arquivos

```
database-schema/
├── migrations/           # Arquivos de migração
│   ├── 001_initial.sql  # Migração inicial
│   ├── 002_users.sql    # Criação da tabela users
│   └── 003_relations.sql # Relacionamentos
├── seeds/               # Dados iniciais
│   ├── users.sql        # Dados de usuários
│   ├── categories.sql   # Dados de categorias
│   └── sample_data.sql  # Dados de exemplo
├── models/              # Modelos de dados
│   ├── User.ts          # Modelo de usuário
│   ├── [Entity].ts      # Outros modelos
│   └── index.ts         # Exportações
├── schemas/             # Definições de schema
│   ├── user.sql         # Schema da tabela users
│   ├── [entity].sql     # Outros schemas
│   └── relations.sql    # Relacionamentos
├── indexes/             # Definições de índices
│   ├── primary.sql      # Índices primários
│   ├── performance.sql  # Índices de performance
│   └── unique.sql       # Índices únicos
├── constraints/         # Constraints
│   ├── foreign_keys.sql # Chaves estrangeiras
│   ├── checks.sql       # Check constraints
│   └── triggers.sql     # Triggers
└── docs/               # Documentação
    ├── er_diagram.md    # Diagrama ER
    ├── data_dictionary.md # Dicionário de dados
    └── performance.md   # Considerações de performance
```

## 📦 Entregáveis Esperados

### Schema
- [ ] Tabelas principais criadas
- [ ] Relacionamentos implementados
- [ ] Constraints aplicados
- [ ] Índices otimizados criados
- [ ] Triggers implementados (se necessário)
- [ ] Views criadas (se necessário)
- [ ] Procedures/functions criadas (se necessário)

### Migrações
- [ ] Migração inicial criada
- [ ] Migrações incrementais documentadas
- [ ] Rollback procedures definidas
- [ ] Versionamento implementado
- [ ] Dados de seed criados

### Modelos
- [ ] Modelos de dados implementados
- [ ] Validações de dados configuradas
- [ ] Relacionamentos mapeados
- [ ] Hooks/callbacks implementados
- [ ] Serialização configurada

### Funcionalidades
- [ ] CRUD básico funcionando para todas as entidades
- [ ] Consultas complexas implementadas
- [ ] Relacionamentos funcionando corretamente
- [ ] Constraints sendo respeitadas
- [ ] Performance otimizada

### Testes
- [ ] Testes de integração do schema
- [ ] Testes de migração
- [ ] Testes de constraints
- [ ] Testes de performance
- [ ] Testes de rollback
- [ ] Cobertura de testes >= 80%

### Documentação
- [ ] Diagrama ER criado
- [ ] Dicionário de dados completo
- [ ] Documentação das migrações
- [ ] Guia de performance
- [ ] Exemplos de consultas
- [ ] README com instruções

## ✅ Critérios de Qualidade

### Design do Schema
- [ ] Normalização adequada (3NF ou superior)
- [ ] Nomes descritivos e consistentes
- [ ] Tipos de dados apropriados
- [ ] Constraints de integridade implementadas
- [ ] Relacionamentos bem definidos
- [ ] Sem redundância desnecessária

### Performance
- [ ] Índices otimizados para consultas frequentes
- [ ] Queries otimizadas
- [ ] Particionamento implementado (se necessário)
- [ ] Cache strategy definida
- [ ] Connection pooling configurado
- [ ] Tempo de resposta < 100ms para consultas simples

### Segurança
- [ ] Controle de acesso implementado
- [ ] Dados sensíveis criptografados
- [ ] Validação de inputs rigorosa
- [ ] Logs de auditoria implementados
- [ ] Backup seguro configurado
- [ ] Recovery procedures testadas

### Manutenibilidade
- [ ] Migrações versionadas
- [ ] Documentação completa
- [ ] Código limpo e comentado
- [ ] Testes automatizados
- [ ] Monitoring implementado
- [ ] Alertas configurados

### Escalabilidade
- [ ] Design preparado para crescimento
- [ ] Sharding strategy (se necessário)
- [ ] Read replicas configuradas
- [ ] Horizontal scaling considerado
- [ ] Data archiving strategy
- [ ] Performance monitoring

## 📚 Exemplos e Referências

### Exemplo de Schema SQL
```sql
-- Exemplo de tabela principal
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT users_email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    CONSTRAINT users_phone_format CHECK (phone ~* '^\+?[1-9]\d{1,14}$')
);

-- Índices de performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_active ON users(is_active) WHERE is_active = true;

-- Trigger para updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
```

### Referências
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Database Design Best Practices](https://www.postgresql.org/docs/current/ddl.html)
- [SQL Performance Tuning](https://www.postgresql.org/docs/current/performance-tips.html)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)

## 🔄 Considerações Adicionais

### Backup e Recovery
- [ ] Estratégia de backup implementada
- [ ] Point-in-time recovery configurado
- [ ] Backup testing procedures
- [ ] Disaster recovery plan
- [ ] Data retention policy

### Monitoring e Alertas
- [ ] Query performance monitoring
- [ ] Resource usage tracking
- [ ] Error rate monitoring
- [ ] Capacity planning
- [ ] Automated alerting

### Versionamento e Deploy
- [ ] Migration versioning system
- [ ] Zero-downtime deployment
- [ ] Rollback procedures
- [ ] Blue-green deployment (se aplicável)
- [ ] Database schema validation

### Compliance e Governança
- [ ] Data privacy compliance (GDPR/LGPD)
- [ ] Audit trail implementation
- [ ] Data classification
- [ ] Access control policies
- [ ] Data lineage tracking
