#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys

class KaraokeLocal:

	def __init__(self, fichero):
		try:
			parser = make_parser()
			cHandler = SmallSMILHandler()
			parser.setContentHandler(cHandler)
			parser.parse(open(fichero)) 
			self.lista = cHandler.get_tags()
			print(self.lista)
		except:
			print('Usage: python3 karaoke.py file.smil')

	def listaordenada(self):
		for etiquetas in self.lista:
			atr = []
			print('\n')
			for atributo in etiquetas:
				if atributo != 'element' and etiquetas[atributo] != '':
					print('x')
					atr.append(atributo + '=' + etiquetas[atributo] + '')
			print(atr)
					
		
		

if __name__ == "__main__":
	 fichero = KaraokeLocal(sys.argv[1])





