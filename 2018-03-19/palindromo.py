#     Programa que verifica se uma palavra é palindromo ou não
#
#     Paulo Sérgio do Nascimento	160013-3   
#     19 03 2018
#

print("Verificador de Palíndromo")

palavra = input("Digite a palavra: ")
palavra_sem_espacos = palavra.replace(" ","")
palavra_minus = palavra_sem_espacos.lower()
tamanho = len(palavra_minus) - 1

palavra2 = ""

while (tamanho >= 0):
	palavra2 = palavra2 + palavra_minus[tamanho]
	tamanho = tamanho - 1

if(palavra2 == palavra):
	print("a palavra " + palavra  + " é Palíndromo")
else:
	print("a palavra" +  palavra + "não é Palíndromo")