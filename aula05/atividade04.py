numero = int(input("Digite um número: "))
contador = 0

while numero > 0:
    contador = contador + 1
    numero = numero // 10 
    print(numero)


