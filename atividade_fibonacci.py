numero_limite = int(input("Digite um número para gerar a sequência de Fibonacci até ele: "))

fibonacci = [0, 1]

while True:
    proximo = fibonacci[-1] + fibonacci[-2]
    if proximo > numero_limite:
        break
    fibonacci.append(proximo)

print("Sequência de Fibonacci até", numero_limite, "é:")
print(fibonacci)