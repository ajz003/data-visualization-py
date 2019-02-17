from pygal.maps.world import World

wm = World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 36710000, 'us': 325700000, 'mx': 129200000})

wm.render_to_file('na_populations.svg')