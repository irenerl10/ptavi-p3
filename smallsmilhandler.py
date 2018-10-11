#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys

class SmallSMILHandler(ContentHandler):
	def __init__(self):
		self.list = []
		self.elements = {
			'root-layout':['width', 'height', 'background-color'],
			'region':['id', 'top', 'bottom', 'left', 'right'],
			'img':['src', 'region', 'begin', 'dur'],
			'audio':['src', 'begin', 'dur'],
			'textstream':['src', 'region']}

	def startElement(self, name, attrs):
		if name in self.elements:
			dicc = {}
			dicc['element']=name
			for atributo in self.elements[name]:
				dicc[atributo] = attrs.get(atributo,"")
			self.list.append(dicc)

	def get_tags(self):
		return self.list

if __name__ == "__main__":
	parser = make_parser()
	cHandler = SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open(sys.argv[1])) #Aqui debe ir karaoke.smil pero tengo windows
	print(cHandler.get_tags())
