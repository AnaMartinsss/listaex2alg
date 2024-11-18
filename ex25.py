 #(Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas os números pares.
print(f"***FILTRO DE NÚMEROS PARES***")
def filtrar_num_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))

for _ in range(quantidade):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

pares = filtrar_num_pares(numeros)

print(f"Números pares:{pares}") 