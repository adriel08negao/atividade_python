
nota01 = float(input("Digite sua nota: "))
nota02 = float(input("Digite sua nota: "))
nota03 = float(input("Digite sua nota: "))
nota04 = float(input("Digite sua nota: "))
NotaFinal = (nota01+nota02+nota03+nota04)/4

frequencia = float(input("Informe sua frquêmcia: "))

if (NotaFinal >= 7 or frequencia >= 75):
    print(f"sua nota é: {NotaFinal} e sua frequencia de {frequencia} % , aprovado!")
    
else:  
    print(f"sua nota é: {NotaFinal} e sua frequencia de {frequencia} % , reprovado!")

