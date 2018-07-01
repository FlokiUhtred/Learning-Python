cart = float(input("Quanto dinheiro você possui R$.: "))
dolar = float(cart/3.27)
print("Com R${:.2f}, você pode conseguir ${:.2f}".format(cart, dolar))