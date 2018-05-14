# Paulo Sérgio do Nascimento	160013-3
#
# Programa Principal
#

from animal import Animal

class humano(Animal):
	idade = None
	def setIdade(self, idade):
		self.idade = idade
	def getIdade(self):
		return self.idade

class ave(Animal):
	porte = None
	def	setPorte(self, porte):
		self.porte = porte
	def getPorte(self):
		return self.porte

class inseto(Animal):
	patas = None
	def	setPatas(self, patas):
		self.patas = patas
	def getPatas(self):
		return self.patas

class peixe(Animal):
	tipo = None
	def setTipo(self, tipo):
		self.tipo = tipo
	def getTipo(self):
		return self.tipo


# Rotina principal do programa

humano  = humano("Terreste", "Mamífero", "Onívoro")
humano.setIdade("30")

galinha = ave("Terrestre", "Ave", "Herbivoro")
galinha.setPorte("médio")

formiga = inseto("Terrestre", "Inseto", "Onívoro")
formiga.setPatas("6")

tucunare = peixe("Aquático", "Peixe", "Carnívoro")
tucunare.setTipo("Água Doce")

print("HUMANO:  ",humano.getHabitat(), humano.getClassificacao(), humano.getAlimentacao(), humano.getIdade())
print("GALINHA: ", galinha.getHabitat(), galinha.getClassificacao(), galinha.getAlimentacao(), galinha.getPorte())
print("FORMIGA: ", formiga.getHabitat(), formiga.getClassificacao(), formiga.getAlimentacao(), formiga.getPatas())
print("TUCUNARE:", tucunare.getHabitat(), tucunare.getClassificacao(), tucunare.getAlimentacao(), tucunare.getTipo())