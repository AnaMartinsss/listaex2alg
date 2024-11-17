#(Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.

print(f"***VERIFICADOR DE NÚMERO, PAR OU ÍMPAR!***")

#num = int(input("Digite um número inteiro:"))
#if num %2 == 0:
#   print(f"Seu número é par!")
#else:
#   print(f"Seu número é ímpar!")
     
def par_ou_impar(numero):
    return "par" if numero % 2 == 0 else "ímpar"

numero = int(input("Digite um número: "))
print(f"O número {numero} é {par_ou_impar(numero)}.")   