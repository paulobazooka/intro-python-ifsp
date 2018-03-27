# Exercicio com leitura de arquivo csv do portal de transparencia de Campinas
# Análise do maior e menor salário
# 27-03-2018


try:
	arquivo = open("remuneracoes.csv")
except Exception as e:
	print("erro ao abrir arquivo...")
	exit(0)

maiorSalario = ["", 0]
menorSalario = ["", 2000000]
cargo = ""

for linha in arquivo:
	if('Matricula' not in linha and 'true' not in linha):	
		linha_sem_virgula = linha.split(';')
		campo = linha_sem_virgula[16].split('$')
		cargo = linha_sem_virgula[4][8:]
		salario = campo[1].replace(".","")
		salario = float(salario.replace(",", "."))
         
		if(salario > maiorSalario[1]):
			maiorSalario[1] = salario
			maiorSalario[0] = linha_sem_virgula[4][8:]
		if(salario < menorSalario[1] and salario > 0 and cargo != "INDENIZACOES JUDICIAIS"):
			menorSalario[1] = salario
			menorSalario[0] = linha_sem_virgula[4][8:]

print("Menor Salário da Prefeitura: " + str(menorSalario))
print("Maior Salário da Prefeitura: " + str(maiorSalario))

arquivoLog = open("fevereiro.log", "w")
arquivoLog.write("Menor Salário da Prefeitura: " + str(menorSalario) + "\n")
arquivoLog.write("Maior Salário da Prefeitura: " + str(maiorSalario) + "\n")

arquivoLog.close()