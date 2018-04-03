# Exercicio com leitura de arquivo csv do portal de transparencia de Campinas
# Análise do maior e menor salário
# 27-03-2018


try:
	arquivo = open("remuneracao_marco.csv")
except Exception as e:
	print("erro ao abrir arquivo...")
	exit(0)

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

arquivo.close()
print("Menor Salário da Prefeitura: " + str(menorSalario))
print("Maior Salário da Prefeitura: " + str(maiorSalario))

"""
arquivoLog = open("fevereiro.log", "w")
arquivoLog.write("Menor Salário da Prefeitura: " + str(menorSalario) + "\n")
arquivoLog.write("Maior Salário da Prefeitura: " + str(maiorSalario) + "\n")

arquivoLog.close()  """