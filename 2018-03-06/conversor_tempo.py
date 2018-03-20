"""
  3 - Faça um 
"""

def converte(segundos):
	minutos = segundos//60
	horas = minutos%60
	segundos = segundos%60
	minutos = minutos%60
	horas = minutos//60
	print("horas:    ", str(horas))
	print("minutos:  ", str(minutos))
	print("segundos: ", str(segundos))


converte(3600)