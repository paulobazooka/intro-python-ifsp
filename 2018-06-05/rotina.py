import mysql

def criaConexao():
	host = 'sql10.freemysqlhosting.net'
	banco = 'sql10241582'
	user = 'sql10241582'
	password = 'xqT4aW5U6Z'
	port = '3306'

	try:
		# db receber a conexão do banco específico
		db = pymysql.connect(host, user, password, banco)
		db.select_db(banco)
		return db
	except Exception as e:
		print('ERRO! Não foi possível se conectar ao Banco de Dados')
		exit(0)



def inicializaBanco():
	db = criaConexao()
	cursor = db.cursor()

	sql = 'DROP TABLE IF EXISTS Musicas'
	cursor.execute(sql)
	db.commit()

	sql = 'CREATE TABLE Musicas(id INT PRIMARY KEY AUTO_INCREMENT, titulo TEXT, tempo REAL, artista TEXT)'
	cursor.execute(sql)
	db.commit()

	sql = 'INSERT INTO Musicas(titulo, tempo, artista) VALUES("Regret", 4.32, "The Winery Dogs"), ("Something", 5.65, "The Beatles"), ("Hora do Mergulho", 3.56, "Engenheiros do Hawaii"), ("Andar na Pedra", 4.23, "Raimundos")'
	cursor.execute(sql)
	db.commit()
	db.close()



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
