#	Introdução ao Python
#   09/04/2018
#   Programa para contar o numero de ocorrências de uma palavra dentro do texto

import string

try:
	arquivo = open("cancioneiro-FernandoPessoa.txt") 
except Exception as e:
	exit(0)

dicionario = dict()

for linha in arquivo:
	linha = linha.translate(linha.maketrans("","",string.punctuation))
	paragrafo = linha.lower().split()
	for palavra in paragrafo:
		if (palavra in dicionario):
			dicionario[palavra] = dicionario[palavra] + 1
		else:
			dicionario[palavra] = 1

for palavra in dicionario:
	print(palavra, "-> ", dicionario[palavra])