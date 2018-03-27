# Exemplo de criação de arquivo em python
# 27-03-2018
#
#

try:
	arquivo = open("teste.txt", 'a')
except Exception as e:
	print("erro ao abrir arquivo...")
	exit(0)

linha = 'Primeira linha para gravar no arquivo'
arquivo.write(linha + "\n")
linha = "Segunda linha para gravar no arquivo"
arquivo.write(linha + '\n')
arquivo.close()
