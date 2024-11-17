# (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços)
print(f"***CONTADOR DE CARACTERES DE UMA FRASE***")
def contador_caracteres(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contador_caracteres(frase)
print("Contagem de caracteres:")
for caractere, quantidade in resultado.items():
    print(f"'{caractere}': {quantidade}")