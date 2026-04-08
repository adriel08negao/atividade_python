
password = input("Crie uma senha: ")

if password.isdigit():
    print("Senha pouco segura (apenas números)")

elif len(password) <6:
    print("Senha fraca")

elif len(password) >= 6 and len(password) <= 8:
    print("Senha média")

else:
    print("Senha forte")




