#(Contagem de Números em uma Lista) Dada uma lista de números, exiba quantos números ela contém
print(f"***CONTAGEM DE NÚMEROS EM UMA LISTA!***")
frase = input("Digite uma frase: ")
contador = 0
dentro_de_palavra = False

for caractere in frase:
    if caractere.isalnum():
        if not dentro_de_palavra:
            contador += 1
            dentro_de_palavra = True
    else:
        dentro_de_palavra = False

print(f"A frase contém {contador} palavras.")