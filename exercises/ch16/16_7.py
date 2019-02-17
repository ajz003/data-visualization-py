import csv
import importlib  
country_codes = importlib.import_module("16_5")

import json

from pygal.maps.world import World
from pygal.style import RotateStyle

country_RD_0, country_RD_1, country_RD_2, country_RD_3 = {}, {}, {}, {}
hasData = 0
noData = 0
with open('rnd.csv') as f:
    data = csv.reader(f)
    title = next(data)
    update_dates = next(data)
    header_row = next(data)   

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    for row in data:
        country_name = row[0]

        try:
            RD = float(row[54])
        except ValueError:
            print(country_name + " has no data for this year.")
            noData += 1
        else:
            cc = country_codes.get_country_code(country_name)
            if cc == None:
                print(country_name + ": NO MATCHING COUNTRY CODE")
            if RD <= 1:
                country_RD_0[cc] = RD
            if RD > 1 and RD <= 2:
                country_RD_1[cc] = RD
            if RD > 2 and RD <= 3:
                country_RD_2[cc] = RD
            else:
                country_RD_3[cc] = RD

            hasData += 1

print(hasData)
print(noData)

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "% of GDP spent in R&D in 2010, by Country"
wm.add('0-1%', country_RD_0)
wm.add('1-2%', country_RD_1)
wm.add('2-3%', country_RD_2)
wm.add('>3%', country_RD_3)

wm.render_to_file('rnd_gdp.svg')



