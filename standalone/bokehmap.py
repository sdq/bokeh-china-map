# -*- coding: utf-8 -*-
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import Range1d, HoverTool
import json
import numpy as np
from china import China
from chinamap import ChinaMap
#from bokeh.sampledata.sample_geojson import geojson

china = China()
provinces = china.provinceArray
chinamap = ChinaMap()
xs, ys = chinamap.allProvinces()

source = ColumnDataSource(
		data = dict(
			x = xs,
			y = ys,
			province = china.provinceArray2Hebei
		)
	)

hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@province</span>
            </div>
        </div>
        """
    )

p = figure(toolbar_location="below",
           toolbar_sticky=False,tools = "pan,wheel_zoom,box_zoom,reset,save")
p.add_tools(hover)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.y_range = Range1d(10, 65)
p.x_range = Range1d(70, 140)

p.patches('x', 'y',legend="中国", alpha=0.5, line_width=2,line_color = "white",hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white',source = source)
p.toolbar.logo = None
output_file("geojson.html")
show(p)