
idade = []
altura = []
alunos = 0

for i in range(30):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura em metros: "))

    idade.append(idade)
    altura.append(altura)

media = sum(altura) / 30

for i in range(30):
    
    if idade[i]>13 and altura[i]<media:
       alunos+=1
print(f"A quantidade de alunos {alunos}")

     


