#	Introdução ao Python
#   09/04/2018
#   Verificar os salários dos servidores da prefeitura


try:
	arquivo = open("remuneracao.csv")
except Exception as e:
	print("Não foi possível abrir o arquivo")
	exit(0)


remuneracoes = dict()
ordenada = dict()

for linha in arquivo:
	if("matricula" not in linha):
		linha_sem_virgula = linha.replace('"', " ").split()
		linha_sem_virgula2 = linha_sem_virgula.remove(",")
		remuneracoes[linha_sem_virgula2[0]] = linha_sem_virgula2[8]
maior = ""

arquivo.close()

for matricula in remuneracoes:
	for matricula2 in remuneracoes:
		if(matricula != matricula2):
			if (remuneracoes[matricula] >= remuneracoes[matricula2]):
				maior = matricula			
			else:
				maior = matricula2

	ordenada[maior] = remuneracoes[maior]

for chave in remuneracoes:
	print(chave," ", remuneracoes[chave])