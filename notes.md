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