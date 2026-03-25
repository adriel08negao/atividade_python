estado_civil = input("digite seu estado civl: ").lower()

if ( estado_civil == "c"):
    print(f"Casado")

elif ( estado_civil == "s"):
    print(f"Solteiro")

elif ( estado_civil == "d"):
    print(f"Divorciado")

elif ( estado_civil == "v"):
    print(f"Viúvo")

else:
    print(f"Outros")