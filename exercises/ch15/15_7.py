"""2d8"""

import pygal
from die import Die

# Create two D6 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(100000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

the_range = [str(x) for x in range(2, max_result+1)]
print(the_range)


hist.title = "Results of rolling two D8s 1000 times."
hist.x_labels = the_range
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')