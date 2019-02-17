import json

from pygal.maps.world import World
from pygal.style import RotateStyle

import importlib  
country_codes = importlib.import_module("16_5")


filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = country_codes.get_country_code(country_name)
        if code: 
            cc_gdp[code] = gdp
        else:
            print(country_name + " has no code.")

cc_gdp_1, cc_gdp_2 = {}, {}

for cc, gdp in cc_gdp.items():
    if gdp < 1000000000000:
        cc_gdp_1[cc] = gdp
    else:
        cc_gdp_2[cc] = gdp

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "GDP in 2016, by Country"
wm.add('0-1tr', cc_gdp_1)
wm.add('>1tr', cc_gdp_2)

wm.render_to_file('world_gdp.svg')