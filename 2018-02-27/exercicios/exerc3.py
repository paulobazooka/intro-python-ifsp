"""
 3. Escreva um programa para coletar uma nota entre 0.0 e 1.0. 
    Se a nota estiver fora do intervalo exiba uma mensagem de erro. 
    Se a nota estiver entre 0 e 1 imprima o conceito obtido baseado na seguinte tabela 
""" 
nota = input("Digite a nota: ")
nota = float(nota)

if (nota <=1) and (nota >=0):
	
	if (nota< 0.6):
		print("Conceito E")
	elif (nota < 0.7):
		print("Conceito D")
	elif (nota < 0.8):
	    print("Conceito C")
	elif (nota < 0.9):
		print("Conceito B")
	else:
		print("Conceito A")

else:
	print("Nota fora do intervalo")
