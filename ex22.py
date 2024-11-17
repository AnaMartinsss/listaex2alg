#(Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de vogais e consoantes. Ignore espaços e caracteres especiais
print(f"***CONTAGEM DE VOGAIS E CONSOANTES***")
frase = input("Digite uma frase: ").lower()
vogais = ("aeiou")
consoantes = ("bcdfghjklmnpqrstvwxyz")
contador_vogais = 0
contador_consoantes = 0

for letra in frase:
    if letra in vogais:
        contador_vogais += 1
    elif letra in consoantes:
        contador_consoantes += 1

print(f"Número de vogais: {contador_vogais}")
print(f"Número de consoantes: {contador_consoantes}")