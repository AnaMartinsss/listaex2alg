#  (Verificação de Anagrama) Receba duas palavras e determine se elas são anagramas (ou seja, possuem as mesmas letras em qualquer ordem)
print(f"***VERIFICAÇÃO DE ANAGRAMA***")
def verificar_anagramas(palavra1, palavra2):
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if len(palavra1) != len(palavra2):
        return False
    
    return sorted(palavra1) == sorted(palavra2)

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if verificar_anagramas(palavra1, palavra2):
    print(f"{palavra1} e {palavra2} são anagramas!")
else:
    print(f"{palavra1} e {palavra2} NÃO são anagramas!")