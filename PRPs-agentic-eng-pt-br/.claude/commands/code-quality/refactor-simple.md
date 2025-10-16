Verificação rápida de refatoração para código Python focando em:
- Limites de fatia vertical
- Complexidade de função
- Segurança de tipo com Pydantic v2
- Responsabilidade única

Procurar por:
1. Funções >20 linhas que precisam decomposição
2. Arquivos longos que precisam decomposição
3. Modelos Pydantic ausentes para I/O
4. Importações entre funcionalidades violando fatias verticais
5. Classes com múltiplas responsabilidades
6. Type hints ausentes

Arquitetura desejada:
- Limites de fatia vertical
- Responsabilidade única
- Segurança de tipo com Pydantic v2 

Para cada problema encontrado, fornecer:
- Localização
- Por que é um problema
- Correção específica com exemplo de código
- Local específico onde a correção deve ser implementada
- Prioridade (alta/média/baixa)

Focar em itens acionáveis que podem ser corrigidos em <1 hora cada.

Salve um refactor_plan.md na pasta PRPs/ai_docs, garanta que você não sobrescreva arquivos existentes
