import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://andrebordignon.esy.es/video.flv')
fhand = open('video.flv', 'wb')
size = 0
while True:
	info = img.read(100000)
	if len(info) < 1: break
	size = size + len(info)
	fhand.write(info)
	
print(size, 'caracteres copiados.')
fhand.close()