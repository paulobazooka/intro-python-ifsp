"""
   Desenvolver um programa que mostre quantos números existem na lista e
   informe quanto elementos existem dentro da lista
"""
menor = None
cont = 0

for num in [12, 34, 23, 11, 16, 78, 89, 34, 32, 45, 13, 78, 98, 345, 43, 37]:
	cont = cont+1
	if(menor is None or num < menor):
		menor = num
    
print("O menor número é: " + str(menor))
print("A quantidade de elementos na lista é: " + str(cont))

#Programa principal



