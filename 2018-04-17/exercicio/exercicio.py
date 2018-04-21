#   UTF-8
#   Introdução ao Python
#   Paulo Sérgio do Nascimento   160013-3
#   17/04/2018
#   Exercício 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def buscarLinkSites(url, sites):
	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	# Retrieve all of the anchor tags
	tags = soup('a')

	for tag in tags:
		print(tag.get('www', None))


sites = []

buscarLinkSites('https://www.cmp.ifsp.edu.br/', sites)
