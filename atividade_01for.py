total_pessoas = int(input("Digite a quantidade de total de pessoas: "))

contador_masculino = 0

for i in range(total_pessoas):
    print(f"\nPessoa {i+1}: ")
    sexo = input("Informe o sexo (m/M para masculino): ")

if sexo == "m" or sexo == "M":
    contador_masculino += 1

print("\nTotal de pessoas do sexo masculino:", contador_masculino)



