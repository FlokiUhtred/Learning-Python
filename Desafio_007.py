nomealuno = str(input("Digite o nome do aluno.: "))
nota1 = float(input("Digite a nota da Av1.: "))
nota2 = float(input("Digite a nota da Av2.: "))
media = (nota1+nota2)/2

print("O aluno {} fez {} na AV1 e {} na AV2, portanto possui uma média de.: {:.2f}".format(nomealuno, nota1, nota2, media))
print(type(media))