
idade = int(input("Digite sua idade: "))

if (idade >= 0 and idade <= 12):
    print(f"Sua idade é {idade}, Você é uma criança" )


elif (idade >= 13 and idade <= 17):
    print(f"Sua idade é {idade}, Você é um adolescente" )

elif (idade >= 18 and idade <= 25):
    print(f"Sua idade é {idade}, Você é um adulto jr" )

elif (idade >= 26 and idade <= 35):
    print(f"Sua idade é {idade}, Você é um adulto" )

elif (idade >= 36 and idade <= 60):
    print(f"Sua idade é {idade}, Você é um adulto sr" )

else:
    print(f"Você é um idoso")
    








