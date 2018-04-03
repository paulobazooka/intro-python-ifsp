# encoding: utf-8
# Paulo Sérgio do Nascimento	160013-3
# 03-04-2018 
# Introdução ao Python 
# Instituto Federal de São Paulo campus Campinas
# Listas II



def removerPrimeiroUltimoElemento(lista):
	lista.pop()
	lista.pop(0)
	print(lista)

def contruirLista(lista, lista2):
	lista3 = []
	for elemento in lista2:
		if (elemento not in lista):
			lista3.append(elemento)
	print(lista3)		


lista = [0, 1, 2, 3, "outro", 8, "queijo", 9, "touro", 6, "martelo", 5]
lista2 = lista[:]

removerPrimeiroUltimoElemento(lista)
contruirLista(lista, lista2)

