#	Paulo Sérgio do Nascimento	160013-3
#	15/05/2018
#	Teste de conexão com banco de dados MySQL


# import da biblioteca para conexão com o banco
import pymysql

# db receber a conexão do banco específico
db = pymysql.connect(host="localhost", user="root", passwd="1q2w3e", db="agenda")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

# print("Database VERSION:", data)

sql = "SELECT * FROM contatos"
cursor.execute(sql)

for linha in cursor:
	print(linha)

inserir = """INSERT INTO contatos(nome,telefone,email) VALUES ('Gumercinda Araujo Malazarte', '987654321', 'gumercinda@outlook.com')"""
cursor.execute(inserir)
db.commit()

for linha in cursor:
	print(linha)

db.close()