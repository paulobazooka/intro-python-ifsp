"""
	Imprimir de trás pra frente sem imprimi espaços em branco
"""

frase = input("Digite uma frase: ")

tamanho = (len(frase))-1


while tamanho >=0:
	letra = frase[tamanho]

	if letra != ' ':
		print(letra)
    
	tamanho = tamanho -1