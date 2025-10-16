# CLAUDE.md

Este arquivo fornece orientação abrangente ao Claude Code ao trabalhar com código Java neste repositório.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)

A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)

Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Princípios de Design

- **Inversão de Dependência**: Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
- **Princípio Aberto/Fechado**: Entidades de software devem ser abertas para extensão mas fechadas para modificação.
- **Responsabilidade Única**: Cada classe, método e módulo deve ter um propósito claro.
- **Falhar Rápido**: Valide entradas cedo e lance exceções imediatamente quando problemas ocorrerem.

## 🧱 Estrutura de Código e Modularidade

### Limites de Arquivo e Método

- **Nunca crie um arquivo de classe com mais de 500 linhas**. Se aproximando deste limite, refatore extraindo classes.
- **Métodos devem ter menos de 50 linhas** para melhor compreensão de IA e manutenibilidade.
- **Classes devem focar em um conceito** - siga o Princípio de Responsabilidade Única.
- **Complexidade ciclomática não deve exceder 10** por método (regra SonarQube).

### Estrutura do Projeto (Layout Padrão Maven)

```
project-root/
├── pom.xml
├── CLAUDE.md
├── .claude/
│   └── commands/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/company/project/
│   │   │       ├── controller/
│   │   │       ├── service/
│   │   │       ├── repository/
│   │   │       ├── entity/
│   │   │       ├── dto/
│   │   │       ├── exception/
│   │   │       ├── config/
│   │   │       └── util/
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── application-prod.yml
│   │       └── logback-spring.xml
│   └── test/
│       ├── java/
│       │   └── com/company/project/
│       └── resources/
└── target/
```

## 🛠️ Configuração Maven

### Configuração POM Essencial

```xml
<properties>
    <!-- Versão Java -->
    > Inserir versões específicas do projeto

    <!-- Versões Spring -->
    > Inserir versões específicas do projeto

    <!-- Versões de Plugin -->
    > Inserir versões específicas do projeto
</properties>
```

### Comandos Maven

```bash
# Limpar e compilar
mvn clean compile

# Executar testes
mvn test

# Executar testes com cobertura
mvn clean test jacoco:report

# Empacotar aplicação
mvn clean package

# Executar análise SonarQube
mvn clean verify sonar:sonar

# Verificar atualizações de dependências
mvn versions:display-dependency-updates

# Aplicar estilo de código
mvn spotbugs:check checkstyle:check
```

## ☕ Padrões Java

### Classes e Objetos

```java
// ✅ Classe bem estruturada com responsabilidade única
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, length = 100)
    private String name;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    // Construtores
    public User() {}
    
    public User(String name, String email) {
        this.name = Objects.requireNonNull(name, "Nome não pode ser nulo");
        this.email = Objects.requireNonNull(email, "Email não pode ser nulo");
        this.createdAt = LocalDateTime.now();
    }
    
    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { 
        this.name = Objects.requireNonNull(name, "Nome não pode ser nulo");
    }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { 
        this.email = Objects.requireNonNull(email, "Email não pode ser nulo");
    }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    
    // Métodos de negócio
    public boolean isActive() {
        return createdAt.isAfter(LocalDateTime.now().minusYears(1));
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;
        User user = (User) o;
        return Objects.equals(id, user.id) && 
               Objects.equals(email, user.email);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(id, email);
    }
    
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", createdAt=" + createdAt +
                '}';
    }
}
```

### DTOs (Data Transfer Objects)

```java
// ✅ DTO para transferência de dados
public class UserDto {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime createdAt;
    
    // Construtores
    public UserDto() {}
    
    public UserDto(User user) {
        this.id = user.getId();
        this.name = user.getName();
        this.email = user.getEmail();
        this.createdAt = user.getCreatedAt();
    }
    
    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}

// ✅ DTO para criação de usuário
public class CreateUserDto {
    @NotBlank(message = "Nome é obrigatório")
    @Size(max = 100, message = "Nome deve ter no máximo 100 caracteres")
    private String name;
    
    @NotBlank(message = "Email é obrigatório")
    @Email(message = "Email deve ter formato válido")
    private String email;
    
    // Construtores, getters e setters
    public CreateUserDto() {}
    
    public CreateUserDto(String name, String email) {
        this.name = name;
        this.email = email;
    }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
```

### Tratamento de Exceções

```java
// ✅ Exceções customizadas
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long userId) {
        super("Usuário com ID " + userId + " não encontrado");
    }
}

public class DuplicateEmailException extends RuntimeException {
    public DuplicateEmailException(String email) {
        super("Email " + email + " já está em uso");
    }
}

// ✅ Handler global de exceções
@ControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException ex) {
        logger.warn("Usuário não encontrado: {}", ex.getMessage());
        
        ErrorResponse error = new ErrorResponse(
            "USER_NOT_FOUND",
            ex.getMessage(),
            LocalDateTime.now()
        );
        
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(DuplicateEmailException.class)
    public ResponseEntity<ErrorResponse> handleDuplicateEmail(DuplicateEmailException ex) {
        logger.warn("Email duplicado: {}", ex.getMessage());
        
        ErrorResponse error = new ErrorResponse(
            "DUPLICATE_EMAIL",
            ex.getMessage(),
            LocalDateTime.now()
        );
        
        return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationErrors(MethodArgumentNotValidException ex) {
        logger.warn("Erro de validação: {}", ex.getMessage());
        
        List<String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> error.getField() + ": " + error.getDefaultMessage())
            .collect(Collectors.toList());
        
        ErrorResponse error = new ErrorResponse(
            "VALIDATION_ERROR",
            "Erro de validação nos dados fornecidos",
            LocalDateTime.now(),
            errors
        );
        
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        logger.error("Erro interno do servidor", ex);
        
        ErrorResponse error = new ErrorResponse(
            "INTERNAL_ERROR",
            "Erro interno do servidor",
            LocalDateTime.now()
        );
        
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}

// ✅ Classe de resposta de erro
public class ErrorResponse {
    private String code;
    private String message;
    private LocalDateTime timestamp;
    private List<String> details;
    
    public ErrorResponse(String code, String message, LocalDateTime timestamp) {
        this.code = code;
        this.message = message;
        this.timestamp = timestamp;
    }
    
    public ErrorResponse(String code, String message, LocalDateTime timestamp, List<String> details) {
        this(code, message, timestamp);
        this.details = details;
    }
    
    // Getters
    public String getCode() { return code; }
    public String getMessage() { return message; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public List<String> getDetails() { return details; }
}
```

## 🌐 Spring Boot Patterns

### Controllers

```java
// ✅ Controller REST bem estruturado
@RestController
@RequestMapping("/api/v1/users")
@Validated
public class UserController {
    
    private static final Logger logger = LoggerFactory.getLogger(UserController.class);
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping
    public ResponseEntity<List<UserDto>> getAllUsers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(required = false) String name) {
        
        logger.info("Buscando usuários - página: {}, tamanho: {}, nome: {}", page, size, name);
        
        List<User> users = userService.findAllUsers(page, size, name);
        List<UserDto> userDtos = users.stream()
            .map(UserDto::new)
            .collect(Collectors.toList());
        
        return ResponseEntity.ok(userDtos);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<UserDto> getUserById(@PathVariable Long id) {
        logger.info("Buscando usuário com ID: {}", id);
        
        User user = userService.findUserById(id);
        UserDto userDto = new UserDto(user);
        
        return ResponseEntity.ok(userDto);
    }
    
    @PostMapping
    public ResponseEntity<UserDto> createUser(@Valid @RequestBody CreateUserDto createUserDto) {
        logger.info("Criando usuário: {}", createUserDto.getName());
        
        User user = userService.createUser(createUserDto);
        UserDto userDto = new UserDto(user);
        
        return ResponseEntity.status(HttpStatus.CREATED).body(userDto);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<UserDto> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody CreateUserDto updateUserDto) {
        
        logger.info("Atualizando usuário com ID: {}", id);
        
        User user = userService.updateUser(id, updateUserDto);
        UserDto userDto = new UserDto(user);
        
        return ResponseEntity.ok(userDto);
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        logger.info("Deletando usuário com ID: {}", id);
        
        userService.deleteUser(id);
        
        return ResponseEntity.noContent().build();
    }
}
```

### Services

```java
// ✅ Service com responsabilidades claras
@Service
@Transactional
public class UserService {
    
    private static final Logger logger = LoggerFactory.getLogger(UserService.class);
    
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Transactional(readOnly = true)
    public List<User> findAllUsers(int page, int size, String name) {
        logger.debug("Buscando usuários - página: {}, tamanho: {}, nome: {}", page, size, name);
        
        Pageable pageable = PageRequest.of(page, size);
        
        if (name != null && !name.trim().isEmpty()) {
            return userRepository.findByNameContainingIgnoreCase(name, pageable).getContent();
        }
        
        return userRepository.findAll(pageable).getContent();
    }
    
    @Transactional(readOnly = true)
    public User findUserById(Long id) {
        logger.debug("Buscando usuário com ID: {}", id);
        
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    @Transactional
    public User createUser(CreateUserDto createUserDto) {
        logger.debug("Criando usuário: {}", createUserDto.getName());
        
        // Verificar se email já existe
        if (userRepository.existsByEmail(createUserDto.getEmail())) {
            throw new DuplicateEmailException(createUserDto.getEmail());
        }
        
        User user = new User(createUserDto.getName(), createUserDto.getEmail());
        User savedUser = userRepository.save(user);
        
        logger.info("Usuário criado com sucesso - ID: {}", savedUser.getId());
        return savedUser;
    }
    
    @Transactional
    public User updateUser(Long id, CreateUserDto updateUserDto) {
        logger.debug("Atualizando usuário com ID: {}", id);
        
        User existingUser = findUserById(id);
        
        // Verificar se email mudou e se já existe
        if (!existingUser.getEmail().equals(updateUserDto.getEmail()) &&
            userRepository.existsByEmail(updateUserDto.getEmail())) {
            throw new DuplicateEmailException(updateUserDto.getEmail());
        }
        
        existingUser.setName(updateUserDto.getName());
        existingUser.setEmail(updateUserDto.getEmail());
        
        User updatedUser = userRepository.save(existingUser);
        
        logger.info("Usuário atualizado com sucesso - ID: {}", updatedUser.getId());
        return updatedUser;
    }
    
    @Transactional
    public void deleteUser(Long id) {
        logger.debug("Deletando usuário com ID: {}", id);
        
        User user = findUserById(id);
        userRepository.delete(user);
        
        logger.info("Usuário deletado com sucesso - ID: {}", id);
    }
}
```

### Repositories

```java
// ✅ Repository com métodos customizados
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    boolean existsByEmail(String email);
    
    Optional<User> findByEmail(String email);
    
    List<User> findByNameContainingIgnoreCase(String name, Pageable pageable);
    
    @Query("SELECT u FROM User u WHERE u.createdAt >= :since")
    List<User> findUsersCreatedSince(@Param("since") LocalDateTime since);
    
    @Modifying
    @Query("UPDATE User u SET u.name = :name WHERE u.id = :id")
    int updateUserName(@Param("id") Long id, @Param("name") String name);
}
```

## 🧪 Testes

### Testes Unitários

```java
// ✅ Teste unitário bem estruturado
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void deveCriarUsuarioComSucesso() {
        // Given
        CreateUserDto createUserDto = new CreateUserDto("João Silva", "joao@example.com");
        User expectedUser = new User("João Silva", "joao@example.com");
        expectedUser.setId(1L);
        
        when(userRepository.existsByEmail("joao@example.com")).thenReturn(false);
        when(userRepository.save(any(User.class))).thenReturn(expectedUser);
        
        // When
        User result = userService.createUser(createUserDto);
        
        // Then
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getName()).isEqualTo("João Silva");
        assertThat(result.getEmail()).isEqualTo("joao@example.com");
        
        verify(userRepository).existsByEmail("joao@example.com");
        verify(userRepository).save(any(User.class));
    }
    
    @Test
    void deveLancarExcecaoQuandoEmailJaExiste() {
        // Given
        CreateUserDto createUserDto = new CreateUserDto("João Silva", "joao@example.com");
        
        when(userRepository.existsByEmail("joao@example.com")).thenReturn(true);
        
        // When & Then
        assertThatThrownBy(() -> userService.createUser(createUserDto))
            .isInstanceOf(DuplicateEmailException.class)
            .hasMessage("Email joao@example.com já está em uso");
        
        verify(userRepository).existsByEmail("joao@example.com");
        verify(userRepository, never()).save(any(User.class));
    }
    
    @Test
    void deveBuscarUsuarioPorId() {
        // Given
        Long userId = 1L;
        User expectedUser = new User("João Silva", "joao@example.com");
        expectedUser.setId(userId);
        
        when(userRepository.findById(userId)).thenReturn(Optional.of(expectedUser));
        
        // When
        User result = userService.findUserById(userId);
        
        // Then
        assertThat(result).isEqualTo(expectedUser);
        verify(userRepository).findById(userId);
    }
    
    @Test
    void deveLancarExcecaoQuandoUsuarioNaoEncontrado() {
        // Given
        Long userId = 999L;
        
        when(userRepository.findById(userId)).thenReturn(Optional.empty());
        
        // When & Then
        assertThatThrownBy(() -> userService.findUserById(userId))
            .isInstanceOf(UserNotFoundException.class)
            .hasMessage("Usuário com ID 999 não encontrado");
        
        verify(userRepository).findById(userId);
    }
}
```

### Testes de Integração

```java
// ✅ Teste de integração com Spring Boot
@SpringBootTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Transactional
class UserControllerIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Autowired
    private UserRepository userRepository;
    
    @BeforeEach
    void setUp() {
        userRepository.deleteAll();
    }
    
    @Test
    void deveCriarUsuarioComSucesso() {
        // Given
        CreateUserDto createUserDto = new CreateUserDto("João Silva", "joao@example.com");
        
        // When
        ResponseEntity<UserDto> response = restTemplate.postForEntity(
            "/api/v1/users",
            createUserDto,
            UserDto.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody()).isNotNull();
        assertThat(response.getBody().getName()).isEqualTo("João Silva");
        assertThat(response.getBody().getEmail()).isEqualTo("joao@example.com");
        
        // Verificar se foi salvo no banco
        List<User> users = userRepository.findAll();
        assertThat(users).hasSize(1);
        assertThat(users.get(0).getName()).isEqualTo("João Silva");
    }
    
    @Test
    void deveRetornarErroQuandoEmailJaExiste() {
        // Given
        User existingUser = new User("Usuário Existente", "joao@example.com");
        userRepository.save(existingUser);
        
        CreateUserDto createUserDto = new CreateUserDto("João Silva", "joao@example.com");
        
        // When
        ResponseEntity<ErrorResponse> response = restTemplate.postForEntity(
            "/api/v1/users",
            createUserDto,
            ErrorResponse.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CONFLICT);
        assertThat(response.getBody()).isNotNull();
        assertThat(response.getBody().getCode()).isEqualTo("DUPLICATE_EMAIL");
    }
    
    @Test
    void deveBuscarUsuarioPorId() {
        // Given
        User user = new User("João Silva", "joao@example.com");
        User savedUser = userRepository.save(user);
        
        // When
        ResponseEntity<UserDto> response = restTemplate.getForEntity(
            "/api/v1/users/" + savedUser.getId(),
            UserDto.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody()).isNotNull();
        assertThat(response.getBody().getId()).isEqualTo(savedUser.getId());
        assertThat(response.getBody().getName()).isEqualTo("João Silva");
    }
}
```

## 🛡️ Segurança

### Configuração de Segurança

```java
// ✅ Configuração de segurança
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/v1/users/**").authenticated()
                .requestMatchers("/api/v1/auth/**").permitAll()
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt
                    .jwtAuthenticationConverter(jwtAuthenticationConverter())
                )
            );
        
        return http.build();
    }
    
    @Bean
    public JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtGrantedAuthoritiesConverter authoritiesConverter = new JwtGrantedAuthoritiesConverter();
        authoritiesConverter.setAuthorityPrefix("ROLE_");
        authoritiesConverter.setAuthoritiesClaimName("roles");
        
        JwtAuthenticationConverter authenticationConverter = new JwtAuthenticationConverter();
        authenticationConverter.setJwtGrantedAuthoritiesConverter(authoritiesConverter);
        
        return authenticationConverter;
    }
}
```

## 📊 Logging e Monitoramento

### Configuração de Logging

```xml
<!-- logback-spring.xml -->
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/application.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <logger name="com.company.project" level="DEBUG"/>
    <logger name="org.springframework.web" level="INFO"/>
    <logger name="org.hibernate.SQL" level="DEBUG"/>
    <logger name="org.hibernate.type.descriptor.sql.BasicBinder" level="TRACE"/>
    
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </root>
</configuration>
```

### Health Check

```java
// ✅ Health check customizado
@Component
public class DatabaseHealthIndicator implements HealthIndicator {
    
    private final UserRepository userRepository;
    
    public DatabaseHealthIndicator(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Override
    public Health health() {
        try {
            long userCount = userRepository.count();
            return Health.up()
                .withDetail("database", "Disponível")
                .withDetail("totalUsers", userCount)
                .build();
        } catch (Exception e) {
            return Health.down()
                .withDetail("database", "Indisponível")
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}
```

## 🚫 Anti-Padrões

### ❌ Evite

```java
// ❌ Classe muito grande
public class MegaService {
    // 500+ linhas de código
}

// ❌ Método muito longo
public void processEverything() {
    // 100+ linhas de código
}

// ❌ Tratamento genérico de exceções
try {
    // código
} catch (Exception e) {
    System.out.println("Erro: " + e.getMessage());
}

// ❌ Acoplamento forte
public class UserService {
    private DatabaseConnection connection; // Acoplamento direto
}
```

### ✅ Faça

```java
// ✅ Classes pequenas e focadas
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User createUser(CreateUserDto dto) {
        // Implementação focada
    }
}

// ✅ Métodos pequenos e testáveis
public User createUser(CreateUserDto dto) {
    validateUserData(dto);
    checkEmailUniqueness(dto.getEmail());
    return saveUser(dto);
}

// ✅ Tratamento específico de exceções
try {
    User user = userService.createUser(dto);
    return ResponseEntity.ok(user);
} catch (DuplicateEmailException e) {
    return ResponseEntity.status(HttpStatus.CONFLICT).build();
} catch (ValidationException e) {
    return ResponseEntity.badRequest().build();
}

// ✅ Inversão de dependência
public class UserService {
    private final UserRepository userRepository; // Interface, não implementação
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

## 📚 Recursos Adicionais

- [Documentação Java Oficial](https://docs.oracle.com/en/java/)
- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)
- [Maven Documentation](https://maven.apache.org/guides/)
- [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)
- [Mockito Documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html)

---

**Lembre-se**: Foque em código limpo, testável e bem estruturado. Use os princípios SOLID e mantenha classes e métodos pequenos e com responsabilidades claras. Sempre trate exceções adequadamente e use logging para rastreabilidade.
