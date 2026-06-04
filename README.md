# Compilador Portugol

Este é um projeto de um compilador simples para a linguagem Portugol, desenvolvido em Python. O objetivo é ler um arquivo de código-fonte `.por`, identificar seus componentes e traduzi-lo.

## 🛠️ Estrutura do Projeto

O desenvolvimento do compilador está dividido em 3 etapas principais:

1. **Analisador Léxico (Concluído ✅):** Lê o arquivo caractere por caractere, separa as palavras e gera uma lista de tokens classificados (Comandos, Identificadores e Símbolos).
2. **Analisador Sintático (Pendente ⏳):** Irá receber os tokens e validar se a ordem das instruções e a gramática estão corretas.
3. **Gerador de Código (Pendente ⏳):** Irá traduzir os tokens validados para código Python executável.

## 🚀 Como Executar o Analisador Léxico

### Pre-requisitos
* Python 3.x instalado.

### Passo a Passo

1. Crie um arquivo chamado `codigo.por` na mesma pasta do script principal.
2. Escreva o seu código em Portugol dentro dele. Exemplo:
   ```text
   inteiro: idade;