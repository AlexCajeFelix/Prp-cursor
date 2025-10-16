# CLAUDE.md

Este arquivo fornece orientação abrangente ao Claude Code ao trabalhar com código Python neste repositório.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)

A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)

Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Princípios de Design

- **Inversão de Dependência**: Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
- **Princípio Aberto/Fechado**: Entidades de software devem ser abertas para extensão mas fechadas para modificação.
- **Responsabilidade Única**: Cada função, classe e módulo deve ter um propósito claro.
- **Falhar Rápido**: Verifique erros potenciais cedo e lance exceções imediatamente quando problemas ocorrerem.

## 🧱 Estrutura de Código e Modularidade

### Limites de Arquivo e Função

- **Nunca crie um arquivo com mais de 500 linhas de código**. Se aproximando deste limite, refatore dividindo em módulos.
- **Funções devem ter menos de 50 linhas** com uma única responsabilidade clara.
- **Classes devem ter menos de 100 linhas** e representar um único conceito ou entidade.
- **Organize código em módulos claramente separados**, agrupados por funcionalidade ou responsabilidade.
- **Comprimento de linha deve ser máximo de 100 caracteres** regra ruff no pyproject.toml

### Arquitetura do Projeto

Siga arquitetura vertical slice rigorosa com testes vivendo ao lado do código que eles testam:

```
src/project/
    __init__.py
    main.py
    tests/
        test_main.py
    conftest.py

    # Módulos principais
    database/
        __init__.py
        connection.py
        models.py
        tests/
            test_connection.py
            test_models.py
        conftest.py

    services/
        __init__.py
        user_service.py
        auth_service.py
        tests/
            test_user_service.py
            test_auth_service.py
        conftest.py

    api/
        __init__.py
        routes/
            __init__.py
            users.py
            auth.py
        tests/
            test_routes.py
        conftest.py
```

## 🐍 Padrões Python

### Type Hints (OBRIGATÓRIO)

```python
# ✅ Sempre use type hints
from typing import List, Dict, Optional, Union
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True

def get_user(user_id: int) -> Optional[User]:
    """Busca usuário por ID."""
    # implementação
    pass

def create_users(users: List[Dict[str, str]]) -> List[User]:
    """Cria múltiplos usuários."""
    # implementação
    pass
```

### Estruturas de Dados

```python
# ✅ Use dataclasses para estruturas simples
@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# ✅ Use Pydantic para validação de dados
from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    name: str
    email: str
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Email inválido')
        return v.lower()
```

### Tratamento de Erros

```python
# ✅ Tratamento específico de erros
class UserNotFoundError(Exception):
    """Exceção levantada quando usuário não é encontrado."""
    pass

class UserService:
    def get_user(self, user_id: int) -> User:
        try:
            user = self.repository.get(user_id)
            if not user:
                raise UserNotFoundError(f"Usuário {user_id} não encontrado")
            return user
        except DatabaseError as e:
            logger.error(f"Erro de banco de dados: {e}")
            raise ServiceError("Erro interno do serviço") from e
```

### Context Managers

```python
# ✅ Use context managers para recursos
from contextlib import contextmanager

@contextmanager
def database_transaction():
    """Context manager para transações de banco de dados."""
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Uso
with database_transaction() as session:
    user = User(name="João", email="joao@example.com")
    session.add(user)
```

## 🔧 Ferramentas de Desenvolvimento

### Ruff (Linting e Formatação)

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

### MyPy (Verificação de Tipos)

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
```

### Pytest (Testes)

```python
# conftest.py
import pytest
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db_session() -> Generator[Session, None, None]:
    """Fixture para sessão de banco de dados de teste."""
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
```

## 🧪 Testes

### Estrutura de Testes

```python
# tests/test_user_service.py
import pytest
from unittest.mock import Mock, patch
from services.user_service import UserService
from models.user import User

class TestUserService:
    """Testes para UserService."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.mock_repository = Mock()
        self.service = UserService(repository=self.mock_repository)
    
    def test_get_user_success(self):
        """Testa busca bem-sucedida de usuário."""
        # Given
        user_id = 1
        expected_user = User(id=user_id, name="João", email="joao@example.com")
        self.mock_repository.get.return_value = expected_user
        
        # When
        result = self.service.get_user(user_id)
        
        # Then
        assert result == expected_user
        self.mock_repository.get.assert_called_once_with(user_id)
    
    def test_get_user_not_found(self):
        """Testa busca de usuário inexistente."""
        # Given
        user_id = 999
        self.mock_repository.get.return_value = None
        
        # When & Then
        with pytest.raises(UserNotFoundError):
            self.service.get_user(user_id)
    
    @pytest.mark.asyncio
    async def test_create_user_async(self):
        """Testa criação assíncrona de usuário."""
        # Given
        user_data = {"name": "Maria", "email": "maria@example.com"}
        expected_user = User(id=1, **user_data)
        self.mock_repository.create.return_value = expected_user
        
        # When
        result = await self.service.create_user_async(user_data)
        
        # Then
        assert result == expected_user
        self.mock_repository.create.assert_called_once_with(user_data)
```

### Fixtures e Mocks

```python
# conftest.py
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_user():
    """Fixture para usuário mock."""
    return User(
        id=1,
        name="João Silva",
        email="joao@example.com",
        is_active=True
    )

@pytest.fixture
def mock_database():
    """Fixture para banco de dados mock."""
    with patch('services.user_service.get_database') as mock_db:
        yield mock_db

@pytest.fixture
def sample_users():
    """Fixture para lista de usuários de exemplo."""
    return [
        User(id=1, name="João", email="joao@example.com"),
        User(id=2, name="Maria", email="maria@example.com"),
        User(id=3, name="Pedro", email="pedro@example.com"),
    ]
```

## 🗄️ Banco de Dados

### SQLAlchemy (ORM)

```python
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
```

### Alembic (Migrações)

```python
# migrations/env.py
from alembic import context
from sqlalchemy import engine_from_config, pool
from models import Base

def run_migrations_online():
    """Execute migrações em modo online."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_database_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )
        
        with context.begin_transaction():
            context.run_migrations()
```

## 🌐 APIs e Web

### FastAPI

```python
# api/routes/users.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from services.user_service import UserService
from dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

class UserCreate(BaseModel):
    name: str
    email: str

@router.get("/", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    service: UserService = Depends(get_user_service)
):
    """Lista usuários com paginação."""
    users = await service.get_users(skip=skip, limit=limit)
    return users

@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    """Cria novo usuário."""
    try:
        user = await service.create_user(user_data.dict())
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    """Busca usuário por ID."""
    try:
        user = await service.get_user(user_id)
        return user
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
```

### Dependency Injection

```python
# dependencies.py
from functools import lru_cache
from services.user_service import UserService
from repositories.user_repository import UserRepository

@lru_cache()
def get_user_repository() -> UserRepository:
    """Retorna instância singleton do repositório de usuários."""
    return UserRepository()

def get_user_service(
    repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    """Retorna instância do serviço de usuários."""
    return UserService(repository=repository)
```

## 📊 Logging e Monitoramento

### Logging Estruturado

```python
# utils/logging.py
import logging
import json
from typing import Dict, Any

class StructuredFormatter(logging.Formatter):
    """Formatador de log estruturado."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if hasattr(record, 'extra_data'):
            log_data.update(record.extra_data)
        
        return json.dumps(log_data, ensure_ascii=False)

def setup_logging():
    """Configura logging estruturado."""
    handler = logging.StreamHandler()
    handler.setFormatter(StructuredFormatter())
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
```

### Métricas e Observabilidade

```python
# utils/metrics.py
from prometheus_client import Counter, Histogram, generate_latest
import time
from functools import wraps

# Métricas
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')

def track_metrics(func):
    """Decorator para rastrear métricas de função."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            REQUEST_COUNT.labels(method='GET', endpoint=func.__name__).inc()
            return result
        finally:
            duration = time.time() - start_time
            REQUEST_DURATION.observe(duration)
    return wrapper
```

## 🚀 Performance e Otimização

### Async/Await

```python
# ✅ Use async/await para I/O
import asyncio
import aiohttp

async def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """Busca dados do usuário de forma assíncrona."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"/api/users/{user_id}") as response:
            return await response.json()

async def fetch_multiple_users(user_ids: List[int]) -> List[Dict[str, Any]]:
    """Busca múltiplos usuários em paralelo."""
    tasks = [fetch_user_data(user_id) for user_id in user_ids]
    return await asyncio.gather(*tasks)
```

### Caching

```python
# utils/cache.py
from functools import lru_cache
import redis
from typing import Optional

class CacheService:
    """Serviço de cache com Redis."""
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    async def get(self, key: str) -> Optional[str]:
        """Busca valor do cache."""
        return await self.redis.get(key)
    
    async def set(self, key: str, value: str, ttl: int = 3600):
        """Armazena valor no cache."""
        await self.redis.setex(key, ttl, value)

# Cache em memória
@lru_cache(maxsize=128)
def expensive_calculation(n: int) -> int:
    """Cálculo caro com cache."""
    # Simulação de cálculo pesado
    return sum(i ** 2 for i in range(n))
```

## 🛡️ Segurança

### Validação de Entrada

```python
# security/validation.py
import re
from typing import Any
from pydantic import BaseModel, validator

class SecureUserInput(BaseModel):
    """Modelo para entrada segura de usuário."""
    username: str
    email: str
    password: str
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
            raise ValueError('Username deve ter 3-20 caracteres alfanuméricos')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Senha deve ter pelo menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Senha deve conter pelo menos uma letra maiúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('Senha deve conter pelo menos um número')
        return v
```

### Autenticação e Autorização

```python
# security/auth.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica senha."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Gera hash da senha."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Cria token de acesso JWT."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

## 🚫 Anti-Padrões

### ❌ Evite

```python
# ❌ Funções muito longas
def process_user_data():
    # 200+ linhas de código

# ❌ Classes com muitas responsabilidades
class MegaService:
    def handle_users(self): pass
    def handle_orders(self): pass
    def handle_payments(self): pass

# ❌ Tratamento genérico de exceções
try:
    # código
except Exception as e:
    print(f"Erro: {e}")

# ❌ Mutable default arguments
def bad_function(items=[]):
    items.append("novo item")
    return items
```

### ✅ Faça

```python
# ✅ Funções pequenas e focadas
def validate_email(email: str) -> bool:
    """Valida formato de email."""
    return "@" in email and "." in email.split("@")[1]

def format_user_name(user: User) -> str:
    """Formata nome do usuário."""
    return f"{user.first_name} {user.last_name}".strip()

# ✅ Classes com responsabilidade única
class UserService:
    def create_user(self, user_data: UserCreate) -> User: pass
    def get_user(self, user_id: int) -> User: pass

class OrderService:
    def create_order(self, order_data: OrderCreate) -> Order: pass
    def get_order(self, order_id: int) -> Order: pass

# ✅ Tratamento específico de exceções
try:
    user = service.get_user(user_id)
except UserNotFoundError:
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
except DatabaseError as e:
    logger.error(f"Erro de banco: {e}")
    raise HTTPException(status_code=500, detail="Erro interno")

# ✅ None como default
def good_function(items: Optional[List[str]] = None) -> List[str]:
    if items is None:
        items = []
    items.append("novo item")
    return items
```

## 📚 Recursos Adicionais

- [Documentação Python Oficial](https://docs.python.org/3/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Lembre-se**: Foque em código limpo, testável e bem tipado. Use as ferramentas modernas do Python para melhor experiência de desenvolvimento e manutenibilidade.
