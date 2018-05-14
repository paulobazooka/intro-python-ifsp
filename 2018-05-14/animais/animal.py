#	Paulo Sérgio do Nascimento	160013-3
#   14/05/2018
#	Classe Principal
#


# Classe principal
class Animal(object):
	# Construtor ----------------------
	def __init__(self, habitat, classificacao, alimentacao):
		self.habitat = habitat
		self.classificacao = classificacao
		self.alimentacao = alimentacao

	# Getters ------------------------
	def getHabitat(self):
		return self.habitat

	def getClassificacao(self):
		return self.classificacao

	def getAlimentacao(self):
		return self.alimentacao

	# Setters -------------------------
	def setHabitat(self, habitat):
		self.habitat = habitat

	def setClassificacao(self, classificacao):
		self.classificacao = classificacao

	def setAlimentacao(self, alimentacao):
		self.alimentacao = alimentacao