#!/usr/bin/env python3
"""
Script para validar estrutura de PRPs
Valida se um arquivo PRP segue a estrutura correta definida no projeto
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple


class PRPValidator:
    def __init__(self, config_path: str = "config/templates.json"):
        """Inicializa o validador com configurações"""
        self.config_path = config_path
        self.config = self._load_config()
        self.required_sections = self.config.get("validation", {}).get("requiredSections", [])
        self.optional_sections = self.config.get("validation", {}).get("optionalSections", [])
    
    def _load_config(self) -> Dict:
        """Carrega configurações do arquivo JSON"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Arquivo de configuração não encontrado: {self.config_path}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Erro ao ler configuração: {e}")
            sys.exit(1)
    
    def validate_file(self, file_path: str) -> Tuple[bool, List[str]]:
        """
        Valida um arquivo PRP
        Retorna (é_válido, lista_de_problemas)
        """
        if not os.path.exists(file_path):
            return False, [f"Arquivo não encontrado: {file_path}"]
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            return False, [f"Erro de encoding no arquivo: {file_path}"]
        
        problems = []
        
        # Validações básicas
        problems.extend(self._validate_header(content, file_path))
        problems.extend(self._validate_sections(content, file_path))
        problems.extend(self._validate_structure(content, file_path))
        problems.extend(self._validate_content_quality(content, file_path))
        
        is_valid = len(problems) == 0
        return is_valid, problems
    
    def _validate_header(self, content: str, file_path: str) -> List[str]:
        """Valida o cabeçalho do PRP"""
        problems = []
        
        # Verifica se tem título principal
        if not re.search(r'^#\s+.+', content, re.MULTILINE):
            problems.append(f"{file_path}: Falta título principal (começando com #)")
        
        # Verifica metadados básicos
        metadata_patterns = [
            r'\*\*Tipo:\*\*',
            r'\*\*Complexidade:\*\*',
            r'\*\*Tempo Estimado:\*\*',
            r'\*\*Versão:\*\*'
        ]
        
        for pattern in metadata_patterns:
            if not re.search(pattern, content):
                problems.append(f"{file_path}: Falta metadado: {pattern}")
        
        return problems
    
    def _validate_sections(self, content: str, file_path: str) -> List[str]:
        """Valida seções obrigatórias"""
        problems = []
        
        # Converte seções para padrões regex
        required_patterns = [
            r'## 🎯 Contexto do Projeto',
            r'## ⚙️ Requisitos Funcionais',
            r'## 🔧 Requisitos Técnicos',
            r'## 📦 Entregáveis Esperados'
        ]
        
        for pattern in required_patterns:
            if not re.search(pattern, content):
                problems.append(f"{file_path}: Seção obrigatória faltando: {pattern}")
        
        return problems
    
    def _validate_structure(self, content: str, file_path: str) -> List[str]:
        """Valida estrutura geral do documento"""
        problems = []
        
        # Verifica se tem pelo menos alguns requisitos funcionais (mais flexível)
        functional_reqs = re.findall(r'### \*\*\[.*?\]\*\*|### \*\*.*?\*\*|\d+\. \*\*.*?\*\*', content)
        if len(functional_reqs) < 1:
            problems.append(f"{file_path}: Deve ter pelo menos 1 requisito funcional detalhado")
        
        # Verifica se tem critérios de aceitação
        acceptance_criteria = re.findall(r'- \[ \]', content)
        if len(acceptance_criteria) < 3:
            problems.append(f"{file_path}: Deve ter pelo menos 3 critérios de aceitação")
        
        # Verifica se tem estrutura de arquivos
        if not re.search(r'## 📁 Estrutura de Arquivos', content):
            problems.append(f"{file_path}: Deve incluir seção de estrutura de arquivos")
        
        return problems
    
    def _validate_content_quality(self, content: str, file_path: str) -> List[str]:
        """Valida qualidade do conteúdo"""
        problems = []
        
        # Verifica se não está muito vago (mais flexível para exemplos)
        vague_patterns = [
            r'\[Descreva.*?\]',  # Placeholders de instrução não preenchidos
            r'\[Exemplo.*?\]',   # Placeholders de exemplo não preenchidos
            r'\[Adicione.*?\]'   # Placeholders de adição não preenchidos
        ]
        
        vague_count = 0
        for pattern in vague_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            vague_count += len(matches)
        
        # Mais tolerante: só reclama se tiver muitos placeholders de instrução
        if vague_count > 10:
            problems.append(f"{file_path}: Muitos placeholders de instrução não preenchidos ({vague_count} encontrados)")
        
        # Verifica se tem exemplos de código
        if not re.search(r'```[\s\S]*?```', content):
            problems.append(f"{file_path}: Deveria incluir exemplos de código")
        
        return problems
    
    def validate_directory(self, directory_path: str) -> Dict[str, Tuple[bool, List[str]]]:
        """Valida todos os arquivos PRP em um diretório"""
        results = {}
        directory = Path(directory_path)
        
        # Procura por arquivos .md
        for file_path in directory.rglob("*.md"):
            if file_path.name != "README.md":  # Ignora READMEs
                is_valid, problems = self.validate_file(str(file_path))
                results[str(file_path)] = (is_valid, problems)
        
        return results


def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print("Uso: python validate_prp.py <arquivo-prp> [diretorio]")
        print("Exemplos:")
        print("  python validate_prp.py examples/my-project.md")
        print("  python validate_prp.py examples/")
        sys.exit(1)
    
    target = sys.argv[1]
    validator = PRPValidator()
    
    if os.path.isfile(target):
        # Validação de arquivo único
        is_valid, problems = validator.validate_file(target)
        
        if is_valid:
            print(f"✅ {target}: PRP válido!")
        else:
            print(f"❌ {target}: PRP inválido!")
            for problem in problems:
                print(f"  • {problem}")
            sys.exit(1)
    
    elif os.path.isdir(target):
        # Validação de diretório
        results = validator.validate_directory(target)
        
        valid_count = 0
        total_count = len(results)
        
        for file_path, (is_valid, problems) in results.items():
            if is_valid:
                print(f"✅ {file_path}")
                valid_count += 1
            else:
                print(f"❌ {file_path}")
                for problem in problems:
                    print(f"  • {problem}")
        
        print(f"\n📊 Resumo: {valid_count}/{total_count} PRPs válidos")
        
        if valid_count < total_count:
            sys.exit(1)
    
    else:
        print(f"❌ Caminho não encontrado: {target}")
        sys.exit(1)


if __name__ == "__main__":
    main()
