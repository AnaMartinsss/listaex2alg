#(Remoção de Elementos Duplicados) Receba uma lista de inteiros e retorne uma nova lista sem elementos duplicados, mantendo a ordem original
print(f"***REMOÇÃO DE ELEMENTOS DUPLICADOS***")
def remover_duplicados(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    return nova_lista

numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))

for _ in range(quantidade):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

resultado = remover_duplicados(numeros)
print("Lista sem duplicados:", resultado)

