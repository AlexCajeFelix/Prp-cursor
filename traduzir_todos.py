#!/usr/bin/env python3
"""
Script para traduzir todos os arquivos .md do repositório PRPs-agentic-eng para português brasileiro
"""
import os
import re
from pathlib import Path

# Mapeamento de traduções comuns
TRADUCOES = {
    # Títulos e seções comuns
    "# Create": "# Criar",
    "# Execute": "# Executar",
    "## Goal": "## Objetivo",
    "## Why": "## Por quê",
    "## What": "## O quê",
    "## Mission": "## Missão",
    "## Task": "## Tarefa",
    "## Process": "## Processo",
    "## Usage": "## Uso",
    "## Example": "## Exemplo",
    "## Output": "## Saída",
    "## Success": "## Sucesso",
    "## Anti-Patterns": "## Anti-Padrões",
    
    # Termos técnicos (manter alguns em inglês quando apropriado)
    "Feature": "Funcionalidade",
    "Execution": "Execução",
    "Implementation": "Implementação",
    "Validation": "Validação",
    "Quality Gates": "Portões de Qualidade",
    "Context": "Contexto",
    "Blueprint": "Blueprint",
    "Codebase": "Codebase",
    "Repository": "Repositório",
    
    # Frases comuns
    "Step-by-step": "Passo a passo",
    "Best practices": "Melhores práticas",
    "Quick reference": "Referência rápida",
    "Getting started": "Começando",
    "Prerequisites": "Pré-requisitos",
}

def traduzir_arquivo(caminho_origem, caminho_destino):
    """
    Traduz um arquivo markdown para português brasileiro
    """
    try:
        with open(caminho_origem, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Aplicar traduções básicas
        conteudo_traduzido = conteudo
        for ingles, portugues in TRADUCOES.items():
            conteudo_traduzido = conteudo_traduzido.replace(ingles, portugues)
        
        # Garantir que o diretório de destino existe
        os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
        
        with open(caminho_destino, 'w', encoding='utf-8') as f:
            f.write(conteudo_traduzido)
        
        print(f"✅ Traduzido: {caminho_origem} → {caminho_destino}")
        return True
    except Exception as e:
        print(f"❌ Erro ao traduzir {caminho_origem}: {e}")
        return False

def main():
    base_dir = Path("/home/alexfelix/Área de trabalho/PRP/PRPs-agentic-eng-pt-br")
    
    # Lista de diretórios para processar
    diretorios_para_traduzir = [
        ".claude/agents",
        ".claude/commands",
        "PRPs/templates",
        "PRPs/ai_docs",
        "claude_md_files",
    ]
    
    total = 0
    sucesso = 0
    
    for diretorio in diretorios_para_traduzir:
        dir_path = base_dir / diretorio
        if not dir_path.exists():
            print(f"⚠️ Diretório não encontrado: {dir_path}")
            continue
        
        # Encontrar todos os arquivos .md
        for arquivo_md in dir_path.rglob("*.md"):
            total += 1
            # O arquivo já está no local correto, vamos traduzir in-place
            if traduzir_arquivo(arquivo_md, arquivo_md):
                sucesso += 1
    
    print(f"\n📊 Resumo:")
    print(f"Total de arquivos: {total}")
    print(f"Traduzidos com sucesso: {sucesso}")
    print(f"Falhas: {total - sucesso}")

if __name__ == "__main__":
    main()

