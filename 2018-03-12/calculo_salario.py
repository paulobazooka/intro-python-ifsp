"""
Reescreva o programa do calculo de salário com pagamento de horas extras
com um função chamada calculaSalario que recebe dois parametros horas e taxas
"""

def calculaSalario(numHoras, valorHora):
	if(numHoras > 40):
		salario = 40*valorHora + (numHoras-40)*valorHora
	else:
		salario = numHoras*valorHora	

	return salario
	


#Programa Principal

valorHora = float (input("Digite o valor hora do salário: "))
numHoras = int(input("Digite o número de horas trabalhadas: "))

salario = calculaSalario(numHoras, valorHora)

print(str(salario))