


operação = input("Digite a operação desejada\n"
" (+, -, /, *, %, **): ")
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))


if ( operação == "+"):
    print(f"{numero1} + {numero2} = {numero1-numero2}")

elif ( operação == "-"):
    print(f"{numero1} - {numero2} = {numero1+numero2}")

elif ( operação == "/"):
    print(f"{numero1} / {numero2} = {numero1/numero2}")

elif ( operação == "*"):
    print(f"{numero1} x {numero2} = {numero1*numero2}")

elif ( operação == "%"):
    print(f"{numero1} % {numero2} = {numero1%numero2}")

elif ( operação == "**"):
    print(f"{numero1} ** {numero2} = {numero1**numero2}")

else:
    print("operação inválida")






