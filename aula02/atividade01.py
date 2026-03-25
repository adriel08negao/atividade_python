
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
nota4 = float(input("Digite sua nota: "))

nota_final=(nota1+nota2+nota3+nota4)/4

if ( nota_final >= 7):
    print(f"Sua média final é: {nota_final} Aprovado!!")

elif ( nota_final >= 5):
    print(f"Sua média final é: {nota_final} Recupeação")

else: 
    print(f"Sua média final é: {nota_final} Reprovado.")