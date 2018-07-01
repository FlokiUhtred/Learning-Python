kmrod = float(input("Quantos KM você rodou?.: "))
qtdias = int(input("Quantos dias você utilizou o carro?.: "))
carrodia = float(60.00)
km = float(0.15)
ckmrod = kmrod*km
cqtdias = qtdias*carrodia
total = ckmrod+cqtdias

print("\nVerificamos que você utilizou o carro por {} dias e rodou {}KM!".format(qtdias, kmrod))
print("\nUau! Você é um aventureiro, uh?!\n")
print("Então, como dito no contrato, o custo por dia do carro é R${}".format(carrodia))
print("E cada KM equivale  a R${}\n".format(km))
print("O total ser pago será.: R${:.2f}\nOBRIGADA!".format(total))
