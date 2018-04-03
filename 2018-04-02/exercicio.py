# encoding: utf-8
# Paulo Sérgio do Nascimento	160013-3
# 02-04-2018 
# Introdução ao Python 
# Instituto Federal de São Paulo campus Campinas


try:
	arquivo = open("intertexto.txt")
except Exception as e:
	print("ERRO! Não foi possível abrir o arquivo.")

lista_palavras=[]
lista_palavras_ordenadas=[]
caracter = ""
palavra  = ""
contpalavras = 0
	
for linha in arquivo:
	
	linha_sem_espacos = linha.replace("\n",' ')
	linha_sem_espacos2 = linha_sem_espacos.replace(".", '')
	linha_sem_espacos3 = linha_sem_espacos2.replace(",", '')
	
	for caracter in linha_sem_espacos3:
		if(caracter != ' '):
			palavra = palavra + caracter
		else:
			palavra2 = palavra.lower()
			if(palavra2 not in lista_palavras):				
				lista_palavras.append(palavra2)
				contpalavras = contpalavras + 1
			palavra = ''

lista_palavras.remove('')
lista_palavras.sort()

print(lista_palavras)
print(contpalavras)