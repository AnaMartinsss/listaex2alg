#(Remoção de Elementos Duplicados de uma Lista Aninhada) Receba uma lista de listas (uma lista aninhada) com valores duplicados e crie uma nova lista de listas onde cada
#sublista contenha apenas valores únicos
print(f"***REMOÇÃO DE ELEMENTOS DUPLICADOS***")
def remover_duplicados(lista_aninhada):
    return [list(set(sublista)) for sublista in lista_aninhada]

lista_aninhada = [[1, 2, 2, 3], [4, 4, 5, 5], [6, 7, 6, 8]]
resultado = remover_duplicados(lista_aninhada)
print(resultado) 

