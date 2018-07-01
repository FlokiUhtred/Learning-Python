preco = float(input("Informe o preço do produto.: "))
descontofix = (5/100)
novopreco = preco-(preco*descontofix)
print("O novo valor a ser pago é.: R${:.2f}".format(novopreco))