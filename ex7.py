# (Inversor de String) Receba uma palavra e exiba-a invertida (exemplo: "Python->"nohtyP")
print(f"***INVERSOR DE STRING***")
def inverter_string(texto):
    return ''.join(reversed(texto))

texto = input("Digite uma palavra: ")
print(f"A palavra invertida é: {inverter_string(texto)}")