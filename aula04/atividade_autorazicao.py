
idade = int(input("Qual é o seu idade: "))
autorizacao = input("você possui autorização? \n\
    Respoda com SIM ou NÃO. ").upper()

if (idade >= 18 or autorizacao == "SIM"):
    print(f"Seu acesso foi autorizado")

else:
    print(f"Seu acesso foi negado")


