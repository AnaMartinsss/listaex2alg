#(Contador de Caracteres em uma Palavra) Solicite uma palavra do usuário e exiba quantos caracteres ela possui.
print(f"***CONTADOR DE CARACTERES!***")

#palavra = input("Digite uma palavra:")
#contagem_caracteres= len(palavra)
#print(f"A palavra tem {contagem_caracteres} caracteres!")

def contar_caracteres(palavra):
    return len([letra for letra in palavra if letra != ' '])

palavra = input("Digite uma palavra: ")
print(f"A palavra tem {contar_caracteres(palavra)} caracteres.") 