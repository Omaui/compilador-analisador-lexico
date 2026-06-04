//listas para controle de palavras, operadores e comandos

quebra = [";", ":", ".", "!", "?", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "/", "\\", "|", "`", "~", "<", ">", " "]
comandos = ["inteiro", "caractere", "se", "senao", "fimse", "para", "fimpara", "enquanto", "fimenquanto"]

with open("programa.por", "r", encoding="utf-8") as arquivo:
    texto_do_arquivo = arquivo.read()

i = 0
acumulador = ""

while i < len(texto_do_arquivo):
    caractere_atual = texto_do_arquivo[i]
    
    acumulador += caractere_atual
    
    i += 1

print(acumulador)
