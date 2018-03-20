"""
1. Escreva um programa que calcule o salário de um funcionário. 
   Todas as horas excedentes a 40 horas o valor é acrescido de 50%. 
   Colete do usuário o valor da hora e quantas horas o funcionário trabalhou.
"""

horas = input("Digite a quantidade de horas trabalhadas: ")
valor = input("Digite o valor da hora trabalha")
salario = 0

horas = int(horas)
valor = float(valor)


if (horas > 40):
  extra=(valor*1.5)*(horas-40)
  salario=(40*valor)
  salario = salario + extra 

else:
	salario = (horas * valor)

		
print('O valor do salário a ser recebido é: ' + str(salario))