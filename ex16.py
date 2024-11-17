# (Calculadora de Fatorial Recursiva) Crie uma função recursiva que calcula o fatorial de um número dado pelo usuário
print(f"***CALCULADORA DE FATORIAL RECURSIVA***")
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)

print(f"O fatorial de {numero} é {resultado}")