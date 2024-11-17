#(Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse intervalo
print(f"***NÚMEROS PRIMOS EM UM INTERVALO***")
def num_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
primos = [num for num in range(inicio, fim + 1) if num_primo(num)]
print("Números primos:{primos}")
