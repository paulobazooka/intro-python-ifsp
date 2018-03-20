"""
 2. Reescreva o programa do cálculo de salário com pagamento de horas extras com uma função chamada 
    calculaSalario que recebe dois parâmetros → horas e taxa.
(a) Enter Hours: 45
(b) Enter Rate: 10
(c) Pay: 475.0
"""

import math

def calculaSalario(horas, valor):
	
	if(horas>40):
		extra=(valor*1.5)*(horas-40)
		salario=(valor*40)
		salario=(salario+extra)       
	else:
		salario=(valor*horas)

	return salario



try:
   	horas = int(input("Digite a quantidade de horas trabalhadas: "))
   	valor = float(input("Digite o valor da hora trabalhada: "))

   	salario = calculaSalario(horas, valor)
   	print(salario)
except:
   	print("Erro!! Somente valores númericos!")   
