# encoding: utf-8
"""
	Faça um programa para a coleta de dados em um 
"""

# Programa Principal

cont = 0 #contador, número de pessoas cadastradas
pesos = 0
alturas = 0
idades = 0
continuar = True
maior_altura = 0
menor_altura = 3
maior_peso = 0
menor_peso = 1000
maior_idade = 0
menor_idade = 200

# Coleta de dados
while continuar:
	peso 	= float(input("Digite o peso da pessoa: "))
	altura  = float(input("Digite a altura da pessoa: "))
	idade	= int(input("Digite a idade da pessoa: "))
	continuar = input("Deseja continuar [s/n]? ")
	cont = cont + 1
	
	idades  = idades  + idade
	pesos   = pesos   + peso
	alturas = alturas + altura

	if(altura > maior_altura):
		maior_altura = altura
	if(altura < menor_altura):
		menor_altura = altura

	if(peso > maior_peso):
		maior_peso = peso
	if(peso < menor_peso):
		menor_peso = peso

	if(idade > maior_idade):
		maior_idade = idade
	if(idade < menor_idade):
		menor_idade = idade

	if(continuar == 'n'):

		alturas = alturas / cont
		pesos   = pesos / cont
		idades  = idades / cont

		print ("Quantidade de Pessoas: " + str(cont))
		print ("Média de idade: " + str(idades))
		print ("Média de peso: " + str(pesos))
		print ("Média de altura: " + str(alturas))

		print ("Menor altura: " + str(menor_altura))
		print ("Maior altura: " + str(maior_altura))
		
		print("Menor idade: " + str(menor_idade))
		print("Maior idade: " + str(maior_idade))
		
		print("Menor peso:  " + str(menor_peso))
		print("Maior peso: " + str(maior_peso))

		break


	