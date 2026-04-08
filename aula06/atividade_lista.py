
idade = []
altura = []
alunos = 0

for i in range(3):
    numero = int(input("Digite sua idade: "))
    tamanho = float(input("Digite sua altura em metros: "))

    idade.append(numero)
    altura.append(tamanho)

media = sum(altura) / 3

for i in range(3):
    
    if idade[i]>13 and altura[i]<media:
       alunos+=1
print(f"A quantidade de alunos {alunos}, a media {media:.2f}")

     


