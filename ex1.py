#(Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.

print(f"***CALCULADORA SIMPLES!***")

#num1 = int(input("Digite o primeiro número:"))
#num2 = int(input("Digite o segundo número:"))
#soma = num1 + num2
#print(f"O resultado da soma dos números {num1} e {num2} é {soma}")

def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    else: 
        return "Operação inválida"
    
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operador = input("Escolha a operação: \n ADIÇÃO: + \n SUBTRAÇÃO: - ")
resultado = calculadora(num1, num2, operador)
 
print(f"Resultado: {resultado}")