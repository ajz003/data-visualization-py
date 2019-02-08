"""Sum of 4d6 minus the lowest value of the 4d6s"""

import pygal
from die import Die

# Create four D6 dice.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
die_4 = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000000):
    result = [die_1.roll(), die_2.roll(), die_3.roll(), die_4.roll()]
    result.remove(min(result))
    results.append(sum(result))

# Analyze the results.
max_result = 18
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

# Check to see if the x labels will be correct
the_range = [str(x) for x in range(3, max_result+1)]
print(the_range)


hist.title = "Results of rolling four D6s and removing the lowest value 1000000 times."
hist.x_labels = the_range
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6 + D6 - Lowest', frequencies)
hist.render_to_file('die_visual_4d6_remove_lowest.svg')