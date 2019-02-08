"""Die-rolling in matplotlib and Random Walk in pygal"""

import pygal
import matplotlib.pyplot as plt

from die import Die
from random_walk import RandomWalk

# Die-rolling in matplotlib

die_1 = Die(6)
die_2 = Die(6)

results = [die_1.roll() + die_2.roll() for roll_num in range(10000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

the_range = [str(x) for x in range(2, max_result+1)]
print(the_range)

plt.hist(results, ec='black')

plt.title("Results of rolling two D6s 10000 times.")
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# Random Walk in pygal

rw = RandomWalk()

rw.fill_walk()

pairs = list(zip(rw.x_values, rw.y_values))
print(pairs)

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Random Walk'
xy_chart.add('Values', pairs)

xy_chart.render_to_file('random_walk_pygal.svg')