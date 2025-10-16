Abaixo está o guia completo **CLAUDE-RUST.md**, modelado após os arquivos específicos de linguagem em seu repositório.
Todos os números de versão, ferramentas e links de melhores práticas estão atualizados em **Rust 1.88 (2025-06-26)**.

---

````markdown
# CLAUDE-RUST.md

Este arquivo fornece orientação abrangente ao **Claude Code** ao trabalhar com projetos Rust 1.88+.

## Filosofia Central de Desenvolvimento

### KISS e YAGNI
Mantenha cada abstração mínima e evite generalização especulativa. Prefira construções idiomáticas do Rust (iteradores, traits, pattern-matching) sobre frameworks feitos à mão.  
As abstrações de custo zero do Rust já fornecem performance sem complexidade extra.

### Concorrência Sem Medo
Aproveite a propriedade do Rust e traits `Send`/`Sync` para escrever código concorrente livre de race conditions. Use `tokio` ou `async-std` para I/O assíncrono; não crie threads OS brutas a menos que o profiling prove um benefício.

### Segurança Opt-in
Blocos `unsafe` devem ser *excepcionais* e extensivamente documentados:

```rust
// SEGURANÇA: `ptr` vem de Box::into_raw e é não-nulo.
unsafe { Box::from_raw(ptr) };
````

Cada `unsafe` requer:

1. **Por que** é necessário
2. Invariantes que chamadores devem manter
3. Prova MIRI ou Kani em `#[cfg(test)]` se viável

---

## 🤖 Diretrizes para Assistente de IA

* **Consciência de Contexto:** Inspecione `Cargo.toml`, módulos existentes e membros do workspace antes de introduzir novas crates ou funcionalidades.
* **Guarda contra Duplicação:** Nenhuma definição duplicada de trait ou tipo—reutilize ou estenda as existentes.
* **Perguntar vs Assumir:** Quando existe ambiguidade de caminho, solicite esclarecimento; nunca adivinhe localizações de arquivo.
* **TDD Preferido:** Escreva testes unitários falhando antes de implementar comportamento.

---

## 🚀 Recursos-Chave do Rust 1.88 (Junho 2025)

| Domínio                                         | Novo Desde 1.74                                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Edition 2024**                               | Padrão para `cargo new`; habilita `let-else` mais curto e lifetimes de pattern melhoradas. |
| **`async fn` em traits**                       | Estável → definições de trait assíncronas ergonômicas.                                                            |
| **`impl Trait` em `let`**                      | Permite tipos opacos em bindings locais para melhor inferência de tipo.                                       |
| **`cargo [lints]`**                            | Configure lints rustc e Clippy diretamente em `Cargo.toml`.                      |
| **Driver nativo libSQL (`libsql-client` 0.2)** | Wrapper assíncrono de primeira classe para SQLite 3.46—ideal para DB local *Rustash*.                                |

---

## 🏗️ Estrutura do Projeto (Workspace-First)

```
rustash/
├── Cargo.toml           # Manifesto do workspace
├── crates/
│   ├── cli/             # Interface de linha de comando (binário)
│   │   └── src/main.rs
│   ├── core/            # Lógica de negócio (crate de biblioteca)
│   │   └── src/lib.rs
│   ├── desktop/         # GUI Tauri (binário)
│   ├── macros/          # Macros procedurais (biblioteca)
│   └── utils/           # Auxiliares reutilizáveis
└── xtask/               # Comandos cargo customizados (apenas dev)
```

*Cada crate permanece sob **200 linhas de código** por arquivo; divida em módulos quando se aproximando do limite.*

---

## 🎯 Configuração Cargo (RIGOROSA)

```toml
[workspace]
members = ["crates/*", "xtask"]

[workspace.package]
edition = "2024"
rust-version = "1.88"

[workspace.lints.rust]
unsafe_code = "forbid"
unused = "deny"

[workspace.lints.clippy]
pedantic        = "warn"
nursery         = "warn"
unwrap_used     = "deny"
expect_used     = "deny"
```

*`rustc --deny warnings` é o padrão em CI.*

---

## 🦀 Padrões Rust Idiomáticos

### Ownership e Borrowing

```rust
// ✅ Ownership claro e borrowing explícito
pub struct User {
    pub id: UserId,
    pub name: String,
    pub email: String,
}

impl User {
    // Toma ownership do nome e email
    pub fn new(id: UserId, name: String, email: String) -> Self {
        Self { id, name, email }
    }
    
    // Borrowing para leitura
    pub fn name(&self) -> &str {
        &self.name
    }
    
    // Borrowing mutável para modificação
    pub fn update_email(&mut self, email: String) {
        self.email = email;
    }
}

// ✅ Uso de referências para evitar clones desnecessários
pub fn find_user_by_name(users: &[User], name: &str) -> Option<&User> {
    users.iter().find(|user| user.name() == name)
}
```

### Error Handling

```rust
// ✅ Tipos de erro específicos com thiserror
use thiserror::Error;

#[derive(Error, Debug)]
pub enum UserError {
    #[error("Usuário com ID {0} não encontrado")]
    NotFound(UserId),
    
    #[error("Email {0} já está em uso")]
    EmailAlreadyExists(String),
    
    #[error("Erro de validação: {0}")]
    Validation(String),
    
    #[error("Erro de banco de dados: {0}")]
    Database(#[from] sqlx::Error),
}

// ✅ Result types para operações que podem falhar
pub async fn create_user(
    db: &Database,
    name: String,
    email: String,
) -> Result<User, UserError> {
    // Validação
    if name.trim().is_empty() {
        return Err(UserError::Validation("Nome não pode estar vazio".to_string()));
    }
    
    if !email.contains('@') {
        return Err(UserError::Validation("Email inválido".to_string()));
    }
    
    // Verificar se email já existe
    if db.user_exists_by_email(&email).await? {
        return Err(UserError::EmailAlreadyExists(email));
    }
    
    // Criar usuário
    let user = User::new(UserId::new(), name, email);
    db.save_user(&user).await?;
    
    Ok(user)
}
```

### Async/Await

```rust
// ✅ Uso idiomático de async/await
use tokio::time::{sleep, Duration};

pub async fn process_users(users: Vec<User>) -> Result<Vec<ProcessedUser>, UserError> {
    let mut results = Vec::new();
    
    // Processar usuários em paralelo
    let futures: Vec<_> = users
        .into_iter()
        .map(|user| process_single_user(user))
        .collect();
    
    let processed_users = futures::future::try_join_all(futures).await?;
    results.extend(processed_users);
    
    Ok(results)
}

async fn process_single_user(user: User) -> Result<ProcessedUser, UserError> {
    // Simular processamento assíncrono
    sleep(Duration::from_millis(100)).await;
    
    let processed = ProcessedUser {
        id: user.id,
        name: user.name().to_uppercase(),
        email: user.email().to_lowercase(),
    };
    
    Ok(processed)
}
```

### Traits e Generics

```rust
// ✅ Traits para abstração
pub trait UserRepository {
    async fn save(&self, user: &User) -> Result<(), UserError>;
    async fn find_by_id(&self, id: UserId) -> Result<Option<User>, UserError>;
    async fn find_by_email(&self, email: &str) -> Result<Option<User>, UserError>;
    async fn delete(&self, id: UserId) -> Result<(), UserError>;
}

// ✅ Implementação concreta
pub struct DatabaseUserRepository {
    pool: sqlx::PgPool,
}

#[async_trait::async_trait]
impl UserRepository for DatabaseUserRepository {
    async fn save(&self, user: &User) -> Result<(), UserError> {
        sqlx::query!(
            "INSERT INTO users (id, name, email) VALUES ($1, $2, $3)",
            user.id.as_uuid(),
            user.name(),
            user.email()
        )
        .execute(&self.pool)
        .await?;
        
        Ok(())
    }
    
    async fn find_by_id(&self, id: UserId) -> Result<Option<User>, UserError> {
        let row = sqlx::query!(
            "SELECT id, name, email FROM users WHERE id = $1",
            id.as_uuid()
        )
        .fetch_optional(&self.pool)
        .await?;
        
        Ok(row.map(|row| User {
            id: UserId::from(row.id),
            name: row.name,
            email: row.email,
        }))
    }
    
    async fn find_by_email(&self, email: &str) -> Result<Option<User>, UserError> {
        let row = sqlx::query!(
            "SELECT id, name, email FROM users WHERE email = $1",
            email
        )
        .fetch_optional(&self.pool)
        .await?;
        
        Ok(row.map(|row| User {
            id: UserId::from(row.id),
            name: row.name,
            email: row.email,
        }))
    }
    
    async fn delete(&self, id: UserId) -> Result<(), UserError> {
        sqlx::query!(
            "DELETE FROM users WHERE id = $1",
            id.as_uuid()
        )
        .execute(&self.pool)
        .await?;
        
        Ok(())
    }
}
```

## 🧪 Testes

### Testes Unitários

```rust
// ✅ Testes unitários bem estruturados
#[cfg(test)]
mod tests {
    use super::*;
    use mockall::predicate::*;
    use mockall::mock;

    // Mock do repositório
    mock! {
        UserRepository {}
        
        #[async_trait]
        impl UserRepository for UserRepository {
            async fn save(&self, user: &User) -> Result<(), UserError>;
            async fn find_by_id(&self, id: UserId) -> Result<Option<User>, UserError>;
            async fn find_by_email(&self, email: &str) -> Result<Option<User>, UserError>;
            async fn delete(&self, id: UserId) -> Result<(), UserError>;
        }
    }

    #[tokio::test]
    async fn test_create_user_success() {
        // Given
        let mut mock_repo = MockUserRepository::new();
        let user_id = UserId::new();
        let user = User::new(user_id, "João Silva".to_string(), "joao@example.com".to_string());
        
        mock_repo
            .expect_save()
            .with(eq(user.clone()))
            .times(1)
            .returning(|_| Ok(()));
        
        // When
        let result = create_user(&mock_repo, "João Silva".to_string(), "joao@example.com".to_string()).await;
        
        // Then
        assert!(result.is_ok());
        let created_user = result.unwrap();
        assert_eq!(created_user.name(), "João Silva");
        assert_eq!(created_user.email(), "joao@example.com");
    }

    #[tokio::test]
    async fn test_create_user_email_already_exists() {
        // Given
        let mut mock_repo = MockUserRepository::new();
        
        mock_repo
            .expect_find_by_email()
            .with(eq("joao@example.com"))
            .times(1)
            .returning(|_| Ok(Some(User::new(
                UserId::new(),
                "Usuário Existente".to_string(),
                "joao@example.com".to_string()
            ))));
        
        // When
        let result = create_user(&mock_repo, "João Silva".to_string(), "joao@example.com".to_string()).await;
        
        // Then
        assert!(result.is_err());
        match result.unwrap_err() {
            UserError::EmailAlreadyExists(email) => {
                assert_eq!(email, "joao@example.com");
            }
            _ => panic!("Erro esperado não encontrado"),
        }
    }

    #[test]
    fn test_user_validation() {
        // Given
        let user = User::new(
            UserId::new(),
            "João Silva".to_string(),
            "joao@example.com".to_string()
        );
        
        // When & Then
        assert_eq!(user.name(), "João Silva");
        assert_eq!(user.email(), "joao@example.com");
        
        // Test update
        let mut user = user;
        user.update_email("novo@example.com".to_string());
        assert_eq!(user.email(), "novo@example.com");
    }
}
```

### Testes de Integração

```rust
// ✅ Testes de integração com banco de dados
#[cfg(test)]
mod integration_tests {
    use super::*;
    use sqlx::PgPool;

    async fn setup_test_db() -> PgPool {
        let database_url = std::env::var("DATABASE_URL")
            .unwrap_or_else(|_| "postgresql://localhost/rustash_test".to_string());
        
        let pool = PgPool::connect(&database_url).await.unwrap();
        
        // Limpar tabela de teste
        sqlx::query("DELETE FROM users").execute(&pool).await.unwrap();
        
        pool
    }

    #[tokio::test]
    async fn test_user_crud_operations() {
        // Given
        let pool = setup_test_db().await;
        let repo = DatabaseUserRepository { pool };
        
        let user_id = UserId::new();
        let user = User::new(
            user_id,
            "João Silva".to_string(),
            "joao@example.com".to_string()
        );
        
        // When - Create
        repo.save(&user).await.unwrap();
        
        // Then - Read
        let found_user = repo.find_by_id(user_id).await.unwrap();
        assert!(found_user.is_some());
        let found_user = found_user.unwrap();
        assert_eq!(found_user.name(), "João Silva");
        assert_eq!(found_user.email(), "joao@example.com");
        
        // When - Find by email
        let found_by_email = repo.find_by_email("joao@example.com").await.unwrap();
        assert!(found_by_email.is_some());
        
        // When - Delete
        repo.delete(user_id).await.unwrap();
        
        // Then - Verify deletion
        let deleted_user = repo.find_by_id(user_id).await.unwrap();
        assert!(deleted_user.is_none());
    }
}
```

## 🔧 Ferramentas e Configuração

### Clippy Configuration

```toml
# .clippy.toml
avoid-breaking-exported-api = false
cognitive-complexity-threshold = 30
too-many-arguments-threshold = 7
type-complexity-threshold = 300
single-char-lifetime-names = false
```

### CI/CD Pipeline

```yaml
# .github/workflows/rust.yml
name: Rust CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        rust: [stable, beta, nightly]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Install Rust
      uses: actions-rs/toolchain@v1
      with:
        toolchain: ${{ matrix.rust }}
        components: rustfmt, clippy
        override: true
    
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: |
          ~/.cargo/registry
          ~/.cargo/git
          target
        key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.lock') }}
    
    - name: Check formatting
      run: cargo fmt --all -- --check
    
    - name: Run clippy
      run: cargo clippy --all-targets --all-features -- -D warnings
    
    - name: Run tests
      run: cargo test --all
    
    - name: Run integration tests
      run: cargo test --test '*'
      env:
        DATABASE_URL: postgresql://localhost/rustash_test
```

## 🚫 Anti-Padrões

### ❌ Evite

```rust
// ❌ Uso excessivo de clone()
let users: Vec<User> = all_users.clone().into_iter().map(|u| {
    u.clone().update_name(u.name().clone().to_uppercase())
}).collect();

// ❌ Panic em produção
let user = users[index]; // Pode panic!

// ❌ Uso de unwrap() em produção
let user = users.first().unwrap(); // Pode panic!

// ❌ Código unsafe desnecessário
unsafe {
    let ptr = users.as_ptr();
    // Manipulação manual de memória desnecessária
}
```

### ✅ Faça

```rust
// ✅ Use referências e iteradores eficientemente
let users: Vec<String> = all_users
    .iter()
    .map(|u| u.name().to_uppercase())
    .collect();

// ✅ Tratamento seguro de erros
if let Some(user) = users.get(index) {
    // Usar user
}

// ✅ Use expect() com mensagens claras ou Result
let user = users.first()
    .expect("Lista de usuários não pode estar vazia");

// ✅ Use safe Rust por padrão
let users: Vec<User> = all_users
    .into_iter()
    .map(|u| u.update_name(u.name().to_uppercase()))
    .collect();
```

## 📚 Recursos Adicionais

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Async Book](https://rust-lang.github.io/async-book/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- [Clippy Lints](https://doc.rust-lang.org/clippy/lints.html)

---

**Lembre-se**: Foque em código seguro, performático e idiomático. Use o sistema de tipos do Rust para prevenir bugs em tempo de compilação. Prefira composição sobre herança e mantenha abstrações simples e focadas.
