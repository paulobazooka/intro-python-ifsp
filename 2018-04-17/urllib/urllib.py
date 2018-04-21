#   UTF-8
#   Introdução ao Python
#   Paulo Sérgio do Nascimento   160013-3
#   17/04/2018
#   Urllib

import urllib.request

fhand = urllib.request.urlopen('http://andrebordignon.esy.es/texto.txt')

for line in fhand:
	print(line.decode().strip())