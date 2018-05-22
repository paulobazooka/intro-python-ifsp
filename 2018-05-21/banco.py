#	Paulo Sérgio do Nascimento	160013-3
#	21/05/2018
#	Trabalhando com Banco de Dados remoto


# import da biblioteca para conexão com o banco
import pymysql

# db receber a conexão do banco específico
db = pymysql.connect(host="sql145.main-hosting.eu", user="u125951895_add", passwd="ifspCampinas@", db="u125951895_agd")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

# Executa a query na tabela SSCustomer
sql = "SELECT * FROM SSCustomer "
cursor.execute(sql)

# Lista de Clientes
clientes = []
# Lista de Paises
paises = []

# Laço de repetição
for linha in cursor:
	clientes.append(linha[1]) # adiciona o nome do cliente ao vetor dos clientes
	if linha[7] not in paises:  # verifica se o nome do país não está nno vetor países
		paises.append(linha[7]) # senão existir no vetor, salva


print("************ Lista de Clientes *************")
for cliente in clientes:
	print(cliente)

print("\n************* Lista de Países **************")
for pais in paises:
	print(pais)

# Fecha conexão com o banco de dados
db.close()