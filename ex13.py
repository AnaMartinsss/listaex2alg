#(Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.
print(f"***MÉDIA COM NOTAS MAIORES QUE A MÉDIA***")
def media_notas_maiores(notas):
    media = sum(notas) / len(notas)
    maiores = list(filter(lambda x: x > media, notas))
    return media, maiores

notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
media, maiores = media_notas_maiores(notas)
print(f"Média: {media}")
print(f"Notas maiores que a média: {maiores}")
