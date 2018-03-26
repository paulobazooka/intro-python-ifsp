# 	Paulo Sérgio do Nascimento
#	20 03 2018
#   
#	Verifique quantas vzs a palavra analfabeto aparece dentro do arquivo fornecido pelo professor
#   Conte também quantas letras e quantas palavras existem nesse arquivo

try:
	#arquivo = input("Digite o caminho do arquivo a ser lido: ")
	arquivo = open('analfa.txt')
except Exception as e:
	print("O arquivo não pode ser aberto...\n")
	exit(0)


contletras = 0
_contletras = 0
_contletras_ = 0
contanalfabeto = 0
palavra = ''
caracter = ''

for linha in arquivo:
	for caracter in linha:
		_contletras = _contletras + 1
		if(caracter == ' '):
			if(palavra == "analfabeto" or palavra == "Analfabeto"):
			   contanalfabeto = contanalfabeto + 1
			palavra = ''	   
		else:
			palavra = palavra + caracter
			contletras = contletras + 1
			if(caracter != ',' and caracter != '.'):
				_contletras_ = _contletras_ + 1

print("Quantidade da palavra ANALFABETO:   " + str(contanalfabeto))
print("Quantidade de letras COM espaços:   " + str(_contletras))
print("Quantidade de letras SEM espaços:   " + str(contletras))
print("Quantidade de letras SEM pontuação: " + str(_contletras_))
