#(Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula:

print(f"***CONVERSOR DE TEMPERATURA!***")

#celsius= float(input("Digite uma temperatura em graus Celcius:"))
#conversor = celsius * 1.8 + 32 
#print(f"A temperatura em Fahrenheit é, {conversor}°F")

def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"{celsius}°C é igual a {fahrenheit}°F.")