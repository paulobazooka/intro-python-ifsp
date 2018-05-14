# Instituto Federal de São Paulo campus Campinas
# Paulo Sérgio do Nascimento	160013-3
# Introdução ao Python
# 
#  https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=


import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
googleKey = ''
while True:
    address = input('Digite o endereço: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) # + '&key=' + googleKey

#    print('Carregando...', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
  #  print('Dados ', len(data), 'caracteres')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Falha na Busca ====')
        print(data)
        continue

 #   print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)