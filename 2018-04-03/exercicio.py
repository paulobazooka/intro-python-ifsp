# encoding: utf-8
# Paulo Sérgio do Nascimento	160013-3
# 03-04-2018 
# Introdução ao Python 
# Instituto Federal de São Paulo campus Campinas
# Listas II


total = []

while (True):
	inp = input("Digite um numero: ")
	if (inp == 'feito'): break
	total.append(float(inp))

media = sum(total)/len(total)
print("Média: " + str(media))
