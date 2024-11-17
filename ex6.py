#(Cálculo de Média Aritmética) Peça três notas de um aluno e calcule a média aritmética  delas.
print(f"***CALCULO DE MÉDIA ARITMÉTICA!***")
notas = [float(input("Digite a primeira nota: ")), 
         float(input("Digite a segunda nota: ")), 
         float(input("Digite a terceira nota: "))]
media = sum(notas) / len(notas)
print(f"A média é: {media}") 