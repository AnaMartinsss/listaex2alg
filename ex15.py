#(Jogo de Adivinhação) Implemente um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o
#usuário deve adivinhar. Após cada tentativa, diga se o número é maior ou menor que o número secreto, e conte o número de tentativas até acertar.
import random
print(f"***JOGO DE ADIVINHAÇÃO***")
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
        tentativas += 1
        if tentativa < numero_secreto:
            print("Mais alto!")
        elif tentativa > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

jogo_adivinhacao()