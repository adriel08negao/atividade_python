
energia = int(input("Digite seu nível de energia: "))
Item_especial = input("Você possui algum item especial?" "\n\
    Responda com SIM ou NÃO").upper()

if ( energia < 0 and energia >100):
    print("Sua entrada é inválida (A energia deve ser de 0 a 100)")

elif ( energia < 30):
    print("Você não pode entrar no abrigo (Sua enrgia é abaixo de 30)")

elif (energia >= 30 and energia <= 70 and Item_especial == "SIM"):
    print("Você pode entra no abrigo")

elif (energia >= 30 and energia <= 70 and Item_especial == "NÃO"):
    print("Você não pode entra no abrigo")

elif (energia >70):
    print("Você pode entrar no abrigo")




