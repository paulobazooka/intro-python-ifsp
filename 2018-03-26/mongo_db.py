#   Paulo Sérgio do Nascimento	160013-3
#	Verificar quantas vzs o MongoDB inicializou de acordo com o arquivo de log 
#   26-03-2018

try:
	arquivo = open('mongod.log')
except Exception as e:
	print("Não foi possível abrir o arquivo")
	exit(0)


cont = 0

for linha in arquivo:
	if("MongoDB starting : pid=" in linha): 
		cont = cont + 1
		print("hora:" + linha[11:19] + " data:" + linha[8:10] + "/" + linha[5:7] + "/" + linha[:4])

print("Quantidade de partidas do banco de dados: " + str(cont))
