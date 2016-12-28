# -*- coding: utf-8 -*-
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.models import Range1d
import json
import numpy as np
from china import China
from chinamap import ChinaMap
#from bokeh.sampledata.sample_geojson import geojson

china = China()
provinces = china.provinceArray
chinamap = ChinaMap()
xs, ys = chinamap.provinces()

x, y = chinamap.hebei()

p = figure(toolbar_location="below",
           toolbar_sticky=False,tools = "pan,wheel_zoom,box_zoom,reset,save")
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.y_range = Range1d(10, 65)
p.x_range = Range1d(70, 140)
#p.patches(x, y, alpha=0.5, line_width=2,line_color = "white")
p.patches(xs, ys,legend="中国", alpha=0.5, line_width=2,line_color = "white")
output_file("geojson.html")
show(p)