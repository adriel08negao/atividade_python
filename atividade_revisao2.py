
operação = input("Digite qual operação quer utilizar\n"
" (+, -, /, *): ")

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

if ( operação == "+"):
    print(f"{number1} + {number2} = {number1+number2}")

elif ( operação == "-"):
    print(f"{number1} - {number2} = {number1-number2}")

elif ( operação == "/"):
    print(f"{number1} / {number2} = {number1/number2}")

elif ( operação == "*"):
    print(f"{number1} * {number2} = {number1*number2}")

else:
    print("Operação inválida")






