# (Soma de Diagonais de uma Matriz Quadrada) Receba uma matriz quadrada de inteiros e calcule a soma dos elementos das diagonais principal e secundária
print(f"***SOMA DE DIAGONAIS DE UMA MATRIZ QUADRADA***")
def soma_diagonais(matriz):
    n = len(matriz)
    soma_principal = 0
    soma_secundaria = 0
    
    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n - 1 - i]
    
    return soma_principal, soma_secundaria

n = int(input("Digite o tamanho da matriz quadrada: "))
matriz = []

for i in range(n):
    linha = []
    print(f"Digite os elementos da linha {i+1}:")
    for j in range(n):
        elemento = int(input(f"Elemento {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

soma_principal, soma_secundaria = soma_diagonais(matriz)

print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")