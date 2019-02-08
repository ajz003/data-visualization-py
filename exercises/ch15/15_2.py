import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
cubes = [value**3 for value in input_values]

plt.scatter(input_values, cubes, s=40, 
    c=cubes, cmap=plt.cm.Blues, edgecolor='none')

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()