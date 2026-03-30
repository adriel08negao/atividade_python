
quantidade = int(input("Digite a quantidade de pessoas: "))

entraram = 0
barrados = 0
sem_convite = 0


for i in range(quantidade):
    print(f"\nPessoa {i+1}:")
    
    idade = int(input("Digite a idade: "))
    convite = int(input("Possui convite? (1 = sim, 0 = não): "))
    
    
    if idade < 16:
        barrados += 1
    elif 16 <= idade <= 17:
        if convite == 1:
            entraram += 1
        else:
            barrados += 1
    else:  
        entraram += 1
        if convite == 0:
            sem_convite += 1

print("\nResultado:")
print(f"Pessoas que entraram: {entraram}")
print(f"Pessoas barradas: {barrados}")
print(f"Pessoas que entraram sem convite: {sem_convite}")