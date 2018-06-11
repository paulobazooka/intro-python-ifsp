#	Introdução ao Python
#	Paulo Sérgio do Nascimento	160013-3
#	22/05/2018
#   manipular banco de dados


# import da biblioteca para conexão com o banco
import pymysql
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def commitar(sql):
	db = criaConexao()
	cursor = db.cursor()
	cursor.execute(sql)
	db.commit()
	db.close()



def criaConexao():
	host = 'localhost'
	user = 'root'
	password = '1q2w3e'
	banco = 'playlist'

	try:
		# db receber a conexão do banco específico
		db = pymysql.connect(host, user, password, banco)
		db.select_db(banco)
		return db
	except Exception as e:
		print('ERRO! Não foi possível se conectar ao Banco de Dados')
		exit(0)




def inicializaBanco():

	sql = 'DROP TABLE IF EXISTS Musicas'
	commitar(sql)
	
	sql = 'CREATE TABLE Musicas(id INT PRIMARY KEY AUTO_INCREMENT, titulo TEXT, tempo REAL, artista TEXT)'
	commitar(sql)

	sql = 'INSERT INTO Musicas(titulo, tempo, artista) VALUES("Regret", 4.32, "The Winery Dogs"), ("Something", 5.65, "The Beatles"), ("Hora do Mergulho", 3.56, "Engenheiros do Hawaii"), ("Andar na Pedra", 4.23, "Raimundos")'
	commitar(sql)




def consultarMusicas():
	cls()
	sql = 'SELECT * FROM Musicas'
	db = criaConexao()
	cursor = db.cursor()
	cursor.execute(sql)
	for linha in cursor:
		print(linha)
	db.close()




def incluirMusica():
	cls()
	musica  = input("Digite o nome da musica: ")
	tempo   = input("Digite o tempo de duração da musica: ")
	artista = input("Digite o nome do artista/banda: ")
	sql = "INSERT INTO Musicas(titulo, tempo, artista) VALUES('" + musica + "', " + tempo + ", '" + artista + "')"
	commitar(sql)
	print("Musica incluida com sucesso!")




def excluirMusica():
	idMusica = input("Digite o id da musica: ")
	sql = "DELETE FROM Musicas where id = " + str(idMusica)
	commitar(sql)
	print("Musica exluida com sucesso!")




def alterarMusica():
	cls()
	consultarMusicas()
	idMusica = input("Digite o id da musica: ")
	musica  = input("Digite o nome da musica: ")
	tempo   = input("Digite o tempo de duração da musica: ")
	artista = input("Digite o nome do artista/banda: ")

	sql = "UPDATE Musicas set titulo = '" + musica + "', tempo = " + tempo + ", artista = '" + artista + "' where id = " + str(idMusica)
	commitar(sql)
	print("Musica alterada com sucesso!")





while True:
	print("\n********* 0.SAIR       1.CONSULTAR       2.INCLUIR      3.EXCUIR     4.ALTERAR ***********")
	opcao = int(input("Digite a opção desejada: "))
	if(opcao == 0): 
		break
	if(opcao == 1): 
		consultarMusicas()
	if(opcao == 2):
		incluirMusica()
	if(opcao == 3):
		excluirMusica()
	if (opcao == 4):
		alterarMusica()



