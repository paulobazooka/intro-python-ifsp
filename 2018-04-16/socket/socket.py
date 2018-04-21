#   UTF-8
#   Introdução ao Python
#   Paulo Sérgio do Nascimento   160013-3
#   16/04/2018
#   Socket
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect("andrebordignon.esy.es", 80)
cmd = "GET http://andrebordignon.esy.es/texto.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512) #vamos ler de 512 em 512 caracteres.
	if (len(data) < 1):
		break
	print(data.decode())

mysock.close()