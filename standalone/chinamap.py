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

	def allProvinces(self):
		xs = []
		ys = []
		for i in xrange(len(self.provinceArray)):
			if self.provinceArray[i] == "河北":
				x, y = self.hebei()
				xs.extend(x)
				ys.extend(y)
			else:
				x, y = self.province(self.provinceArray[i])
				xs.append(x)
				ys.append(y)
		return xs,ys

	def selectedProvinces(self,selectedArray):
		xs = []
		ys = []
		for i in xrange(len(selectedArray)):
			if selectedArray[i] == "河北":
				x, y = self.hebei()
				xs.extend(x)
				ys.extend(y)
			else:
				x, y = self.province(selectedArray[i])
				xs.append(x)
				ys.append(y)
		return xs,ys

	def province(self, name):
		x = []
		y = []
		if name in self.provinceArray:
			index = self.provinceArray.index(name)
			coordinates = self.geoinfo["features"][index]["geometry"]["coordinates"][0]
			for i in xrange(len(coordinates)):
				x.append(coordinates[i][0])
				y.append(coordinates[i][1])

		return x, y

	def hebei(self):
		xs = []
		ys = []
		index = self.provinceArray.index("河北")
		for j in xrange(2):
			x = []
			y = []
			coordinates = self.geoinfo["features"][index]["geometry"]["coordinates"][j][0]
			for i in xrange(len(coordinates)):
				x.append(coordinates[i][0])
				y.append(coordinates[i][1])
			xs.append(x)
			ys.append(y)
		
		return xs, ys


