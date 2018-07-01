print("+"*50) 
graus = float(input("\nDigite a temperatura em ºC.: "))
transfah = float(((graus/5)*9)+32)
transkel = graus+273
print("A sua temperatura {:.1f}ºC equivale a {:.1f}ºF\n e corresponde a {:.0f}K".format(graus, transfah, transkel))