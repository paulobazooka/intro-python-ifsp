import MySQLdb as db


def criaConexao():
	HOST = "sql10.freemysqlhosting.net"
	PORT = 3306
	USER = "sql10241582"
	PASSWORD = "xqT4aW5U6Z"
	BANCO = "sql10241582"
	

	try:
		# db receber a conexão do banco específico
		print("Conectando...")
		remote =  db.Connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=BANCO)
		print("Obtendo cursor...")
		dbhandler = remote.cursor()
		print("Realizando a consulta...")
		dbhandler.execute("SELECT * from teste")
		result = dbhandler.fetchall()
		for item in result:
			print (item)
	except Exception as e:
		print (e)
		exit(0)
	finally:
		remote.close()

		