print("Insira o usuário e senha: ")
for i in range(3):
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print(f"ERRO! Você ainda tem {3-1-i} tentativas ")
    
    else:
        print("Login aceito!")
        break
else:
    print("Limite de tentativas!")