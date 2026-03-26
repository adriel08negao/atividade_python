turmas = int(input(" Digite a quantidade: "))
total_turmas = turmas
total_alunos = 0

while turmas > 0:
    alunos = int(input("Conte o número de alunos das turmas: "))

    if alunos >= 40:
        print("Turma grande, reconte!")
    else:
        total_alunos += alunos
        turmas -= 1

media = total_alunos / total_turmas

print(f"A média de alunos da turma é: {media}")






