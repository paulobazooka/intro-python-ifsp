# Jogo Desenvolvimento na Classe
# Paulo Sérgio do Nascimento 160013-3


from random import randint


# Classe personagem
class Personagem:
	pontos = 0
	def __init__(self, patas, idade):
		self.idade = idade
		self.patas = patas

	def getIdade(self):
		return self.idade

	def addPonto(self):
		self.pontos = self.pontos + 1

	def getPontos(self):
		return self.pontos



# Programa Principal
bruxa = Personagem(3,45)
monstro = Personagem(4,33)


i = 0
while(i < 1000):
	# Random
	numBruxa = randint(0,9)
	numMonstro = randint(0,9)


	# Comparação
	if(numBruxa > numMonstro):
		bruxa.addPonto()
	else:
		if(numBruxa < numMonstro):
			monstro.addPonto()
	i = i + 1

print("Pontos da Bruxa:",bruxa.getPontos())
print("Pontos do Monstro:",monstro.getPontos())