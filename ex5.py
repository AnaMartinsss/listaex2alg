#(Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10)

print(f"***GERADOR DE TABUADA!***")

#numero = int(input("Digite um número: "))
#for i in range(1, 11):
#   print(f"{numero} x {i} = {numero * i}")
    
def tabuada(n):
    contador = 1
    while contador <= 10:
        print(f"{n} x {contador} = {n * contador}")
        contador += 1

numero = int(input("Digite um número para gerar a tabuada: "))
tabuada(numero)