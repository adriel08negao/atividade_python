
litros = float(input("Digite o número de litros: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

preco_alcool = 3.89
preco_gasolina = 5.50

if tipo == 'A':
    preco_total = litros * preco_alcool
    if litros <= 20:
        desconto = preco_total * 0.03
    else:
        desconto = preco_total * 0.05

elif tipo == 'G':
    preco_total = litros * preco_gasolina
    if litros <= 20:
        desconto = preco_total * 0.04
    else:
        desconto = preco_total * 0.06

else:
    print("Tipo de combustível inválido!")
    exit()

valor_final = preco_total - desconto

print(f"Valor a pagar: R$ {valor_final:.2f}")












