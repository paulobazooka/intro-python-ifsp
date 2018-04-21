#   Introdução ao Python
#   Paulo Sérgio do Nascimento   160013-3
#   16/04/2018
#


try:
	# Abrir arquivo a ser analizado
	arquivo = open("suicidio-estado.csv")
except Exception as e:
	print("Não foi possível abrir o arquivo...")
	exit(0)

# Abrir o arquivo para escrita ou criar arquivo caso não exista
arquivo_est = open("arquivo-estado.log", "w")

for linha in arquivo:
	if("Unidade" not in linha and "Total" not in linha):
		linha = linha.split(',')
		homicidios = float(linha[1])
		habitantes = float(linha[2])

		# Arredondar casas decimais
		taxa = round((homicidios / habitantes) * 100, 4)
		
		# Concatenar a string que será gravada no arquivo
		estado = linha[0] + " " + str(taxa) + "%\n"
		
		# gravar a linha no arquivo
		arquivo_est.write(estado)

# fechar arquivo após a escrita
arquivo_est.close()        
		