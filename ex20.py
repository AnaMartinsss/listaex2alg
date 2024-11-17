#(Gerador de Números da Sequência de Fibonacci) Peça ao usuário um número n e gere uma lista com os n primeiros números da sequência de Fibonacci.
print(f"***GERADOR DE NÚMEROS SA SEQUêNCIA DE FIBONACCI***")
def gerar_fibonacci(n):
    fibonacci = []
    a,b = 0,1 
    for _ in range(n):
     fibonacci.append(a)
     a, b = b, a + b
     return fibonacci
 
n = int(input("Quantos números da sequência de Fibonacci você quer gerar? "))
resultado = gerar_fibonacci(n)
print(f"Os primeiros {n} números da sequência de Fibonacci são: {resultado}")