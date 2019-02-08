import matplotlib.pyplot as plt

# # First 5 

# input_values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]

# plt.scatter(input_values, cubes, s=100)

# # Set chart title and label axes.
# plt.title("Cube Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# plt.tick_params(axis='both', labelsize=14)

# plt.show()

# First 5000

input_values = list(range(1, 5001))
cubes = [value**3 for value in input_values]

plt.scatter(input_values, cubes, s=40, edgecolor='none')

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()