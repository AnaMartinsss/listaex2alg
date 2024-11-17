# (Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida
print(f"***CALCULADORA BÁSICA COM ESTRUTURAS CONDICIONAIS: +, -, *, / ***")
def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else: 
        return "Operação inválida"
    
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operador = input("Escolha a operação: \n ADIÇÃO: + \n SUBTRAÇÃO: - \n MULTIPLICAÇÃO: *\n DIVISÃO: / ")
resultado = calculadora(num1, num2, operador)
 
print(f"Resultado: {resultado}")
