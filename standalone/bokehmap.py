# -*- coding: utf-8 -*-
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import Range1d, HoverTool, CustomJS
from bokeh.layouts import widgetbox,column,row, gridplot, layout
from bokeh.models.widgets import Dropdown, TextInput, Button, RadioButtonGroup, Select, Slider, DataTable, DateFormatter, TableColumn
import json
import numpy as np
from china import China
from chinamap import ChinaMap
from datetime import date
from random import randint

legends = []
colors = []
for x in xrange(0,35):
    legends.append("灰色")
    colors.append("lightgrey")

china = China()
provinceArray = china.provinceArray
provinceArray2Hebei = china.provinceArray2Hebei
chinamap = ChinaMap()
xs, ys = chinamap.allProvinces()

source = ColumnDataSource(
        data = dict(
            x = xs,
            y = ys,
            provinces = china.provinceArray2Hebei,
            legends = legends,
            colors = colors
        )
    )

hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@provinces</span>
            </div>
        </div>
        """
    )

p = figure(toolbar_location="below",
           toolbar_sticky=False,tools = [hover, "pan","wheel_zoom","box_zoom","reset","save"])
p.toolbar.logo = None
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.y_range = Range1d(10, 65)
p.x_range = Range1d(70, 140)
p.patches('x', 'y',legend='legends',color = "colors", source=source, alpha=0.5, line_width=2,line_color = "white")

text_input = TextInput(value="default", title="标题:")
slider = Slider(start=0, end=10, value=1, step=.1, title="Slider")
button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)
select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
button_1 = Button(label="Button 1")

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data
        var province = cb_obj.label
        var index = data['provinces'].indexOf(province)
        var results = cb_obj.value.split("|")
        var newlegend = results[0]
        var newColor = results[1]
        colors = data['colors']
        colors[index] = newColor
        legends = data['legends']
        legends[index] = newlegend
        if (province == '河北') {
            colors[index+1] = newColor
            legends[index+1] = newlegend
        }
        source.trigger('change')
    """)
dropdowns1 = []
dropdowns2 = []
dropdowns3 = []
menu = [("红色", "红色|crimson"), ("橙色", "橙色|coral"),("黄色", "黄色|yellow"), ("绿色", "绿色|darkgreen"), ("青色", "青色|darkcyan"),  ("蓝色", "蓝色|cornflowerblue"), ("紫色", "紫色|indigo"), ("灰色", "灰色|lightgrey")]
for i in xrange(0,12):
    dropdown = Dropdown(label=provinceArray[i], menu=menu, callback = callback)
    dropdowns1.append(dropdown)
for i in xrange(12,24):
    dropdown = Dropdown(label=provinceArray[i], menu=menu, callback = callback)
    dropdowns2.append(dropdown)
for i in xrange(24,34):
    dropdown = Dropdown(label=provinceArray[i], menu=menu, callback = callback)
    dropdowns3.append(dropdown)

'''
data = dict(
        provinces=provinceArray,
        legends=legends
    )
tablesource = ColumnDataSource(data)

columns = [
        TableColumn(field="provinces", title="Province"),
        TableColumn(field="legends", title="Legend"),
    ]
data_table = DataTable(source=tablesource, columns=columns, width=400, height=400)
'''


output_file("chinamap.html")
l = layout([
    [p,widgetbox(dropdowns1, width=100),widgetbox(dropdowns2, width=100),widgetbox(dropdowns3, width=100)]])
show(l)

