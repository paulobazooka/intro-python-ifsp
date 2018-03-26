#	Persistência de Dados
#   Abrir arquivo com python
#   Paulo Sérgio do Nascimento	160013-3
#

caminho = input("Digite o caminho completo até o arquivo a ser aberto: ")

try:
	arquivo = open(caminho)

	try:
		cont = 0
	
		for linha in arquivo:
			cont = cont + 1

		print("O arquivo contém " + str(cont) + " linhas\n")
	except:
		print("Não foi possível contar as linhas do arquivo\n")
		
	

except Exception as e:
	print("Arquivo não encontrado...\n")


	