# Plotting a Simple Line Graph

* matplotlib.pyplot
* `linewidth` parameter for thickness of line
* `xlabel()` and `ylabel()`
* `tick_params()`
* `plt.plot(input_values, squares, linewidth=5)`
* `plt.scatter(2, 4, s=200)` s is the size of dots
    * `edgecolor` removes edges on the dots
    * `c` changes the color, name or RGB
    * **`cmap` to apply a colormap to your visualization**
* `plt.savefig('squares_plot.png', bbox_inches='tight')`
    * First argument is the name of the file
    * Second argument trims whitespace

# Random Walks

* `plt.axes().get_xaxis().set_visible(False)` to remove axis
* `plt.figure(dpi=128, figsize=(10,6))`
    * `figsize` takes a tuple, which tells matplotlib the dimeions of the plotting window in inches

# pygal and Dice

* `randint()` returns a number between the starting value and the ending value or either
* `count()` counts how many times a certain value appears

# CSVs

* `reader = csv.reader(filename)`
* `next` returns the next lien int eh file when passed to the reader object
* `enumerate` gets the index of each item as well as the value `(index, column_header)`

* `from datetime import datetime`, `strptime()` 
* `fig.autofmt_xdate()` draws the date labels diagonally to prevent them from overlapping.

* `alpha` argument controls a color's transparency (0 to 1, 0 is fully transparent)
* `fill_between(x, y1, y2)`, `facecolor` determines the color of the shaded region

* Ways to deal with with missing data, improperly formatted data, or incorrect data:
    * `try-except-else` block
    * `continue`to skip over some data
    * `remove()` or `del` to eliminate some data after it's been extracted