#!/bin/bash
# Script para gerar código a partir de um PRP usando o Cursor

set -e  # Para o script se houver erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Função para mostrar uso
show_usage() {
    echo "Uso: $0 <arquivo-prp> <diretorio-saida> [opcoes]"
    echo ""
    echo "Argumentos:"
    echo "  arquivo-prp    Caminho para o arquivo PRP"
    echo "  diretorio-saida Diretório onde o código será gerado"
    echo ""
    echo "Opções:"
    echo "  --validate     Validar PRP antes de gerar código"
    echo "  --test         Executar testes após geração"
    echo "  --install      Instalar dependências após geração"
    echo "  --help         Mostrar esta ajuda"
    echo ""
    echo "Exemplos:"
    echo "  $0 examples/my-project.md ./output"
    echo "  $0 examples/api-service.md ./api --validate --test"
    echo "  $0 examples/web-app.md ./web-app --validate --install --test"
}

# Verificar se os argumentos foram fornecidos
if [ $# -lt 2 ]; then
    print_error "Argumentos insuficientes"
    show_usage
    exit 1
fi

# Parse argumentos
PRP_FILE="$1"
OUTPUT_DIR="$2"
VALIDATE=false
TEST=false
INSTALL=false

shift 2  # Remove os dois primeiros argumentos

while [[ $# -gt 0 ]]; do
    case $1 in
        --validate)
            VALIDATE=true
            shift
            ;;
        --test)
            TEST=true
            shift
            ;;
        --install)
            INSTALL=true
            shift
            ;;
        --help)
            show_usage
            exit 0
            ;;
        *)
            print_error "Opção desconhecida: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Verificar se o arquivo PRP existe
if [ ! -f "$PRP_FILE" ]; then
    print_error "Arquivo PRP não encontrado: $PRP_FILE"
    exit 1
fi

# Verificar se o diretório de saída é válido
if [ ! -d "$OUTPUT_DIR" ]; then
    print_info "Criando diretório de saída: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

print_info "Iniciando geração de código..."
print_info "PRP: $PRP_FILE"
print_info "Saída: $OUTPUT_DIR"

# Validação do PRP (se solicitada)
if [ "$VALIDATE" = true ]; then
    print_info "Validando PRP..."
    
    if command -v python3 &> /dev/null; then
        if python3 scripts/validate_prp.py "$PRP_FILE"; then
            print_success "PRP válido!"
        else
            print_error "PRP inválido! Corrija os problemas antes de continuar."
            exit 1
        fi
    else
        print_warning "Python3 não encontrado. Pulando validação do PRP."
    fi
fi

# Criar arquivo temporário com o PRP para o Cursor
TEMP_FILE="/tmp/prp_$(date +%s).md"
cp "$PRP_FILE" "$TEMP_FILE"

print_info "Usando Cursor para gerar código..."

# Comando para gerar código usando o Cursor
# Nota: Este comando assume que o Cursor está configurado com os agentes apropriados
CURSOR_COMMAND="cursor generate-code --prp '$TEMP_FILE' --output '$OUTPUT_DIR' --agent prp-generator"

# Tentar executar o comando do Cursor
if command -v cursor &> /dev/null; then
    print_info "Executando: $CURSOR_COMMAND"
    
    if eval "$CURSOR_COMMAND"; then
        print_success "Código gerado com sucesso!"
    else
        print_error "Erro ao gerar código com Cursor"
        rm -f "$TEMP_FILE"
        exit 1
    fi
else
    print_warning "Cursor CLI não encontrado. Tentando método alternativo..."
    
    # Método alternativo: abrir o arquivo no Cursor e instruir o usuário
    print_info "Abra o arquivo PRP no Cursor e use o agente 'PRP Code Generator'"
    print_info "Arquivo temporário criado: $TEMP_FILE"
    print_info "Diretório de saída: $OUTPUT_DIR"
    
    # Aguardar input do usuário
    read -p "Pressione Enter quando o código for gerado..."
fi

# Limpar arquivo temporário
rm -f "$TEMP_FILE"

# Instalar dependências (se solicitado)
if [ "$INSTALL" = true ]; then
    print_info "Instalando dependências..."
    
    cd "$OUTPUT_DIR"
    
    # Verificar tipo de projeto e instalar dependências apropriadas
    if [ -f "package.json" ]; then
        print_info "Projeto Node.js detectado. Executando npm install..."
        if npm install; then
            print_success "Dependências Node.js instaladas!"
        else
            print_warning "Erro ao instalar dependências Node.js"
        fi
    elif [ -f "requirements.txt" ]; then
        print_info "Projeto Python detectado. Executando pip install..."
        if pip install -r requirements.txt; then
            print_success "Dependências Python instaladas!"
        else
            print_warning "Erro ao instalar dependências Python"
        fi
    elif [ -f "composer.json" ]; then
        print_info "Projeto PHP detectado. Executando composer install..."
        if composer install; then
            print_success "Dependências PHP instaladas!"
        else
            print_warning "Erro ao instalar dependências PHP"
        fi
    else
        print_warning "Tipo de projeto não detectado. Pulando instalação de dependências."
    fi
    
    cd - > /dev/null
fi

# Executar testes (se solicitado)
if [ "$TEST" = true ]; then
    print_info "Executando testes..."
    
    cd "$OUTPUT_DIR"
    
    # Verificar tipo de projeto e executar testes apropriados
    if [ -f "package.json" ]; then
        if npm test; then
            print_success "Testes Node.js executados com sucesso!"
        else
            print_warning "Alguns testes Node.js falharam"
        fi
    elif [ -f "requirements.txt" ]; then
        if python3 -m pytest; then
            print_success "Testes Python executados com sucesso!"
        else
            print_warning "Alguns testes Python falharam"
        fi
    elif [ -f "composer.json" ]; then
        if composer test; then
            print_success "Testes PHP executados com sucesso!"
        else
            print_warning "Alguns testes PHP falharam"
        fi
    else
        print_warning "Comandos de teste não encontrados para este tipo de projeto."
    fi
    
    cd - > /dev/null
fi

print_success "Processo concluído!"
print_info "Código gerado em: $OUTPUT_DIR"

# Mostrar resumo do que foi gerado
if [ -d "$OUTPUT_DIR" ]; then
    print_info "Arquivos gerados:"
    find "$OUTPUT_DIR" -type f -name "*.ts" -o -name "*.js" -o -name "*.tsx" -o -name "*.jsx" -o -name "*.py" -o -name "*.php" | head -10 | while read file; do
        echo "  📄 $file"
    done
    
    total_files=$(find "$OUTPUT_DIR" -type f | wc -l)
    if [ "$total_files" -gt 10 ]; then
        print_info "... e mais $((total_files - 10)) arquivos"
    fi
fi
