# -*- coding: utf-8 -*-
import json
import numpy as np
from china import China

class ChinaMap:
	provinceArray = China().provinceArray

	def __init__(self):
		f = open("chinamap.json", 'r')
		geojson = f.read()
		self.geoinfo = json.loads(geojson)

	def provinces(self):
		xs = []
		ys = []
		for i in xrange(1,len(self.provinceArray)):
			if self.provinceArray[i-1] == "河北":
				x, y = self.hebei()
				xs.extend(x)
				ys.extend(y)
			else:
				x, y = self.province(self.provinceArray[i-1])
				xs.append(x)
				ys.append(y)
		return xs,ys

	def province(self, name):
		x = []
		y = []
		if name in self.provinceArray:
			index = self.provinceArray.index(name)
			coordinates = self.geoinfo["features"][index]["geometry"]["coordinates"][0]
			for i in xrange(1,len(coordinates)):
				#print(coordinates[i-1])
				x.append(coordinates[i-1][0])
				y.append(coordinates[i-1][1])

		return x, y

	def hebei(self):
		xs = []
		ys = []
		index = self.provinceArray.index("河北")
		for j in xrange(0,2):
			x = []
			y = []
			coordinates = self.geoinfo["features"][index]["geometry"]["coordinates"][j][0]
			for i in xrange(1,len(coordinates)):
				#print(coordinates[i-1])
				x.append(coordinates[i-1][0])
				y.append(coordinates[i-1][1])
			xs.append(x)
			ys.append(y)
		
		return xs, ys


