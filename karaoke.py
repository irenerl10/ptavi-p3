#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib.request

class KaraokeLocal:

	def __init__(self, fichero):
			parser = make_parser()
			cHandler = SmallSMILHandler()
			parser.setContentHandler(cHandler)
			parser.parse(open(fichero)) 
			self.lista = cHandler.get_tags()		

	def listaordenada(self):
		for etiquetas in self.lista:
			atr = []
			for atributo in etiquetas:
				if atributo != 'element' and etiquetas[atributo] != '':
					atr.append(atributo + '="' + etiquetas[atributo] + '"')
			print(etiquetas['element'] + '\t' + '\t'.join(atr))


	def to_json(self, fichero, fichero_json=""):
		if fichero_json == "":
			fichero_json = fichero.replace('.smil', '.json')
		with open(fichero_json, 'w') as file:
			json.dump(self.lista, file, indent=3)

	def do_local(self):
		for etiquetas in self.lista:
			for atributo in etiquetas:
				if atributo == 'src':
					url = etiquetas[atributo]
					if url.startswith('http://'):
						fichero = url.split('/')[-1]
						urllib.request.urlretrieve(url, fichero)
						etiquetas[atributo] = fichero

if __name__ == "__main__":
	try:
		fichero = KaraokeLocal(sys.argv[1])
	except:
		print('Usage: python3 karaoke.py file.smil')
	fichero.__str__()
	fichero.to_json(sys.argv[1])
	fichero.do_local()
	fichero.to_json(sys.argv[1], 'local.json')
	fichero.listaordenada()


		





