# Debugar Problema

Debugue e diagnostique sistematicamente o problema relatado.

## Descrição do Problema

$ARGUMENTS

## Processo de Debug

1. **Reproduzir o Problema**
   - Obter passos exatos para reproduzir
   - Verificar se você consegue ver o mesmo problema
   - Anotar quaisquer mensagens de erro ou logs
   - Documentar o comportamento esperado vs atual

2. **Coletar Informações**

   ```bash
   # Verificar mudanças recentes
   git log --oneline -10

   # Procurar por padrões de erro em logs
   # Procurar por mensagens de erro relacionadas
   ```

3. **Isolar o Problema**
   - **Busca Binária**: Comentar seções de código para restringir
   - **Git Bisect**: Encontrar quando o bug foi introduzido
   - **Logging**: Adicionar declarações de log estratégicas
   - **Debugger**: Definir breakpoints se aplicável

4. **Estratégias Comuns de Debug**

   ### Para Erros de Runtime
   - Ler o stack trace completo
   - Identificar a linha exata causando o erro
   - Verificar valores de variáveis naquele ponto
   - Verificar suposições sobre tipos de dados

   ### Para Erros de Lógica
   - Adicionar declarações print/log para rastrear execução
   - Verificar se cada passo produz resultados esperados
   - Verificar condições de contorno
   - Testar com exemplo mínimo reproduzível

   ### Para Problemas de Performance
   - Adicionar medições de tempo
   - Verificar por queries N+1
   - Procurar por algoritmos ineficientes
   - Fazer profile se necessário

   ### Para Problemas de Integração
   - Verificar se serviço externo está acessível
   - Verificar autenticação/credenciais
   - Validar formatos de request/response
   - Testar com curl/Postman primeiro

5. **Análise de Causa Raiz**
   - Por que isso aconteceu?
   - Por que não foi detectado antes?
   - Existem problemas similares em outro lugar?
   - Como podemos prevenir essa classe de bugs?

6. **Implementar Correção**
   - Corrigir a causa raiz, não apenas sintomas
   - Adicionar programação defensiva se necessário
   - Considerar casos extremos
   - Manter correção mínima e focada, seguir KISS

7. **Verificar Resolução**
   - Confirmar que problema original está corrigido
   - Verificar por regressão
   - Testar funcionalidade relacionada
   - Adicionar teste para prevenir recorrência

8. **Documentar Descobertas**

   ```markdown
   ## Resumo de Debug

   ### Problema

   [O que estava quebrado]

   ### Causa Raiz

   [Por que estava quebrado]

   ### Correção

   [O que foi mudado]

   ### Prevenção

   [Como evitar problemas similares]
   ```

## Checklist de Debug

- [ ] Problema reproduzido localmente
- [ ] Causa raiz identificada
- [ ] Correção implementada
- [ ] Testes adicionados/atualizados
- [ ] Nenhuma regressão introduzida
- [ ] Documentação atualizada se necessário

Lembre-se: O objetivo não é apenas corrigir o bug, mas entender por que aconteceu e prevenir problemas similares no futuro.
