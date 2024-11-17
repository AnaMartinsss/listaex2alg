#(Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos, ordene-os de forma que os negativos fiquem
#antes dos positivos, mantendo a ordem original relativa entre eles.
print(f"***ORDENAÇÃO DE LISTA COM NÚMEROS NEGATIVOS E POSITIVOS***")
def ordenar_lista(numeros):
    negativos = []
    positivos = []
    
    for numero in numeros:
        if numero < 0:
            negativos.append(numero)
        else:
            positivos.append(numero)
    
    return negativos + positivos

entrada = input("Digite números separados por espaço: ")
numeros = []

for char in entrada.split():
    numeros.append(int(char))

print("Lista ordenada:", ordenar_lista(numeros))