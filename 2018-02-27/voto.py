# encoding: utf-8
# Programa verificar voto 
# Paulo Sérgio do Nascimento 160013-3   27/02/2018

nome = input("Digite seu nome: ")
try:
	idade = int(input("Digite sua idade: "))
except:
	idade = int(input("Digite sua idade: "))

idade = int(idade)

if(idade < 16): 
	print(nome + ", você não pode votar ainda!")

elif(idade < 18):
	print(nome + ", seu voto é facultativo!")

elif(idade < 65):
	print(nome + ", seu voto é obrigatório!")

else: print(nome + ", seu voto é facultativo!")

print()