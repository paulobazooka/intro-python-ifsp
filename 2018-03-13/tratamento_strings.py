# econding "utf-8"

#  Desenvolva uma função que receba uma string e um caracter e conte
#                        quantas vezes o caractere aparece na string


def contarOcorrencia(palavra, letra):
	cont = 0
	for c in palavra:
		if(c == letra):
			cont = cont + 1

	print("A letra " + str(letra) + " apareceu " + str(cont) + " vezes.")


def contarLetras(palavra):
	cont = 0
	for c in palavra:
		cont = cont + 1
	print("A palavra contém " + str(cont) + " letras")


palavra = input("Palavra: ")
letra   = input("Letra: ")

contarOcorrencia(palavra, letra)
contarLetras(palavra)


