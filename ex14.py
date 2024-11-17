# (Verificador de Palíndromos) Receba uma palavra e determine se ela é um palíndromo (ou seja, se lê igual de trás para frente)
print(f"***VERIFICADOR DE PALÍNDROMOS***")
def palindromo(palavra):
    palavra=''.join(palavra.lower().split())
    return palavra == palavra