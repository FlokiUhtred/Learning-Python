largura = float(input("Digite a Largura da parede em metros.: "))
altura = float(input("Digite a Altura da parede em metros.: "))
area = float(largura*altura)
tintapinta = 2 #m²
qtnecess = float(area/tintapinta)
print("Identificamos que você possui.: {}m² para ser pintado".format(area))
print("Para essa medida será necessário.: {} litros de tinta".format(qtnecess))