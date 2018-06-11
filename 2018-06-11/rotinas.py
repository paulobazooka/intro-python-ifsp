import MySQLdb


def criaConexao():
	host = 'sql10.freemysqlhosting.net'
	banco = 'sql10241582'
	user = 'sql10241582'
	password = 'xqT4aW5U6Z'
	port = '3306'

	try:
		# db receber a conexão do banco específico
		remote =  MySQLdb.connect(host, port, user, password, banco)
		dbhandler = remote.cursor()
		dbhandler.execute("SELECT * from teste")
		result = dbhandler.fetchall()
		for item in result:
			print (item)

	except Exception as e:
		print (e)

	finally:
		remote.close()
