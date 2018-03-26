

caminho = input("Digite o caminho do arquivo: ")

try:
	arq = open(caminho)	
except Exception as e:
	print("Não foi possível abrir o arquivo...\n")


for linha in arq:
	linha2 = linha.strip()
	if(linha2.startswith('nome')):
		print(linha2)