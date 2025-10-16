# Exemplos de PRPs

Este diretório contém exemplos práticos de PRPs preenchidos para diferentes tipos de projetos. Use estes exemplos como referência para criar seus próprios PRPs.

## 📁 Estrutura dos Exemplos

```
examples/
├── web-app-todo/          # Aplicação web de lista de tarefas
├── api-user-management/   # API para gerenciamento de usuários
├── database-ecommerce/    # Schema de banco para e-commerce
├── microservice-payment/  # Microserviço de pagamentos
├── component-user-card/   # Componente de cartão de usuário
└── README.md             # Este arquivo
```

## 🚀 Como Usar os Exemplos

### 1. Explorar os Exemplos
Navegue pelos diretórios para ver diferentes tipos de PRPs:
- **web-app-todo/**: Exemplo completo de aplicação web
- **api-user-management/**: API REST para gerenciamento de usuários
- **database-ecommerce/**: Schema de banco para sistema de e-commerce
- **microservice-payment/**: Microserviço de processamento de pagamentos
- **component-user-card/**: Componente React reutilizável

### 2. Copiar e Personalizar
```bash
# Copiar um exemplo como base
cp -r examples/web-app-todo/ meu-projeto/

# Editar o PRP para suas necessidades
cd meu-projeto/
# Editar o arquivo .md com seus requisitos específicos
```

### 3. Validar o PRP
```bash
# Validar estrutura do PRP
python scripts/validate_prp.py meu-projeto/prp.md
```

### 4. Gerar Código
```bash
# Gerar código usando o Cursor
./scripts/generate_from_prp.sh meu-projeto/prp.md ./output --validate --test
```

## 📚 Tipos de Exemplos Disponíveis

### Web Application
- **Arquivo**: `web-app-todo/prp.md`
- **Descrição**: Aplicação web completa para gerenciamento de tarefas
- **Tecnologias**: React, Node.js, PostgreSQL
- **Complexidade**: Média

### API Service
- **Arquivo**: `api-user-management/prp.md`
- **Descrição**: API REST para gerenciamento de usuários
- **Tecnologias**: Node.js, Express, MongoDB
- **Complexidade**: Média

### Database Schema
- **Arquivo**: `database-ecommerce/prp.md`
- **Descrição**: Schema completo para sistema de e-commerce
- **Tecnologias**: PostgreSQL
- **Complexidade**: Alta

### Microservice
- **Arquivo**: `microservice-payment/prp.md`
- **Descrição**: Microserviço para processamento de pagamentos
- **Tecnologias**: Node.js, Docker, Kubernetes
- **Complexidade**: Alta

### Frontend Component
- **Arquivo**: `component-user-card/prp.md`
- **Descrição**: Componente React reutilizável para exibir usuários
- **Tecnologias**: React, TypeScript, Styled Components
- **Complexidade**: Baixa

## 🎯 Como Criar Seu Próprio PRP

### 1. Escolha o Template Apropriado
Baseado no tipo de projeto que você quer criar:

- **Aplicação Web Completa**: Use `templates/web-application.md`
- **API/Serviço**: Use `templates/api-service.md`
- **Schema de Banco**: Use `templates/database-schema.md`
- **Microserviço**: Use `templates/microservice.md`
- **Componente Frontend**: Use `templates/frontend-component.md`

### 2. Preencha Todas as Seções
Siga a estrutura do template e preencha:

- ✅ **Contexto do Projeto**: Seja claro sobre o objetivo
- ✅ **Requisitos Funcionais**: Detalhe cada funcionalidade
- ✅ **Requisitos Técnicos**: Especifique tecnologias e padrões
- ✅ **Estrutura de Arquivos**: Defina organização do projeto
- ✅ **Entregáveis**: Liste tudo que deve ser criado
- ✅ **Critérios de Qualidade**: Defina padrões de qualidade

### 3. Use Exemplos Concretos
Em vez de escrever:
```
Implementar autenticação de usuários
```

Escreva:
```
Implementar sistema de autenticação com:
- Login via email/senha
- Registro de novos usuários
- Recuperação de senha via email
- JWT tokens para sessões
- Middleware de autenticação
- Proteção de rotas privadas
```

### 4. Valide Antes de Usar
```bash
# Sempre valide seu PRP antes de gerar código
python scripts/validate_prp.py meu-prp.md
```

## 💡 Dicas para PRPs Eficazes

### Seja Específico
- Use exemplos concretos
- Defina critérios de aceitação claros
- Especifique tecnologias exatas (com versões)

### Forneça Contexto
- Explique o problema a ser resolvido
- Inclua limitações e restrições
- Mencione dependências externas

### Considere Casos Extremos
- Cenários de erro
- Dados inválidos
- Limites de performance
- Casos de uso não óbvios

### Mantenha Foco
- Um PRP por funcionalidade/projeto
- Evite escopo muito amplo
- Quebre projetos grandes em PRPs menores

## 🔧 Ferramentas Úteis

### Validação
```bash
# Validar um PRP específico
python scripts/validate_prp.py examples/web-app-todo/prp.md

# Validar todos os exemplos
python scripts/validate_prp.py examples/
```

### Geração de Código
```bash
# Gerar com validação e testes
./scripts/generate_from_prp.sh examples/web-app-todo/prp.md ./output --validate --test --install

# Gerar apenas código
./scripts/generate_from_prp.sh examples/api-user-management/prp.md ./api-output
```

### Análise
```bash
# Verificar estrutura dos templates
find templates/ -name "*.md" -exec echo "=== {} ===" \; -exec head -20 {} \;
```

## 📖 Próximos Passos

1. **Explore os Exemplos**: Comece olhando os exemplos que mais se parecem com seu projeto
2. **Copie um Template**: Use um template como base para seu PRP
3. **Personalize**: Adapte o template para suas necessidades específicas
4. **Valide**: Sempre valide antes de gerar código
5. **Execute**: Use o Cursor para gerar código baseado no PRP
6. **Itere**: Melhore o PRP baseado nos resultados

## 🤝 Contribuindo com Exemplos

Se você criou um PRP útil que gostaria de compartilhar:

1. Crie um diretório em `examples/` com nome descritivo
2. Inclua o arquivo PRP preenchido
3. Adicione um README explicando o exemplo
4. Teste se o PRP é válido
5. Faça um pull request

## ❓ Perguntas Frequentes

### Q: Posso modificar os templates?
R: Sim! Os templates são apenas guias. Adapte conforme necessário.

### Q: O que fazer se meu PRP for muito complexo?
R: Quebre em PRPs menores. Cada PRP deve ter foco em uma funcionalidade específica.

### Q: Como sei se meu PRP está bom o suficiente?
R: Use o validador e tente gerar código. Se o resultado não for satisfatório, adicione mais detalhes.

### Q: Posso usar PRPs para projetos não-web?
R: Absolutamente! Os templates podem ser adaptados para qualquer tipo de projeto.
