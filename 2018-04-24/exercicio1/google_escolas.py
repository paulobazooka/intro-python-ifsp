# utf-8
# Instituto Federal de São Paulo campus Campinas
# Paulo Sérgio do Nascimento	160013-3
# Introdução ao Python
# 
#  https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=


import urllib.request, urllib.parse, urllib.error
import json


# Strings de conexão com a Google
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
googleKey = 'AIzaSyBzBYyN79Mn7gL2m3OruLFewOJ7qNhAzvY'

# carregar o arquivo escolas.csv para descobrir os endereços
try:
    arquivo = open('escolas.csv')
except Exception as e:
    print('ERRRO! Não foi possível abrir o arquivo.')
    exit(0)

# Abrir arquivo para salvar os dados
gravar = open('enderecos.txt', 'w')
gravar.write('============== Endereços das Escolas de Campinas =================\n\n')

# tratamento dos dados do arquivo
for linha in arquivo:
    if('local' not in linha):   
        leitura = linha.split(',')
        address = leitura[1] + " " + leitura[2]

        url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=' + googleKey
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Falha na Busca ====')
            print(data)
            break

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        location = 'latitude: ' + str(lat) + ' ' + 'longitude: ' + str(lng) + '\n'
        location += 'endereço: ' + js['results'][0]['formatted_address'] + '\n\n'
        gravar.write(location)

gravar.close()
arquivo.close()