# Instituto Federal de São Paulo campus Campinas
# Paulo Sérgio do Nascimento	160013-3
# Introdução ao Python
#
#
#

import json

# Abrir o arquivo
try:
	arquivo = open('db.json')	
except Exception as e:
	print('Não foi possível abrir o arquivo')
	exit(0)

# Tratamento do arquivo retirando as partes (colchetes) que não fazem sentido
# para leitura Json 
dados = arquivo.read()
colIni = dados.find('[')
colFim = dados.find(']')
dadosJson = dados[colIni-1: colFim+1]
usuarios = json.loads(dadosJson)


# Laço para leitura de candidatos dentro do usuarios
for candidato in usuarios:
	if(candidato['candidato'] is not None):
		if(candidato['candidato'] == 2):
			print('id: ',        candidato['id'])
			print('nome: ',      candidato['nome'])
			print('email: ',     candidato['email'])
			print('profissao: ', candidato['profissao'])
			print('candidato: ', candidato['candidato'])
			print('\n')

# Imprimir quantidade de usuários dentro do arquivo
print('\nNúmeros de usuários: ', len(dados))