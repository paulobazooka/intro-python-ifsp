

import matplotlib.pyplot as plt  # importar biblioteca pra plotar gráficos
import numpy as np               # importar a biblioteca numby para manipular com numeros


arquivos = []

try:
	arquivos.append(open("novembro.csv"))
	arquivos.append(open("janeiro.csv"))
	arquivos.append(open("fevereiro.csv"))
	arquivos.append(open("marco.csv"))

except Exception as e:
	print("erro ao abrir arquivo...")
	exit(0)

salarios = []
meses = ['novembro', 'janeiro', 'fevereiro', 'março']

for arquivo in arquivos:
	maiorSalario = ["", "", "",       0]
	menorSalario = ["", "", "", 2000000]
	cargo = ""

	for linha in arquivo:
		if('Matricula' not in linha and 'true' not in linha):	
			linha_sem_virgula = linha.split(';')
			cargo     = linha_sem_virgula[4][8:]
			matricula = linha_sem_virgula[0]
			lotacao   = linha_sem_virgula[3].rstrip()
			campo     = linha_sem_virgula[16].split('$')
			salario   = campo[1].replace(".","")
			salario   = float(salario.replace(",", "."))
     
			if(salario > maiorSalario[3]):
				maiorSalario[3] = salario
				maiorSalario[1] = cargo
				maiorSalario[0] = matricula
				maiorSalario[2] = lotacao
			if(salario < menorSalario[3] and salario > 0 and "INDENIZACOES JUDICIAIS" not in cargo and "ESTAGIARIO" not in cargo):
				menorSalario[3] = salario
				menorSalario[1] = cargo
				menorSalario[0] = matricula
				menorSalario[2] = lotacao

	salarios.append(maiorSalario[3])

	print("Maior Salário: ", maiorSalario)
	print("Menor Salário: ", menorSalario)	

data1 = salarios
x = 10*np.array(range(len(data1)))

plt.plot( x, data1, 'go') # green bolinha
plt.plot( x, data1, 'k:', color='orange') # linha pontilha orange

plt.axis()
plt.title("MAIORES SALÁRIOS")

plt.grid(True)
plt.xlabel("MESES")
plt.ylabel("SALÁRIO")
plt.show()