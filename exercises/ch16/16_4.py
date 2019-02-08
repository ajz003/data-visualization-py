import csv
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'indicator_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    zip_code, per_capita = [], []

    for row in reader:
        try:
            code = int(row[3])
            capita = int(row[4])
        except ValueError:
            print(code, capita, 'missing data')
        else:
            zip_code.append(code)
            per_capita.append(capita)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.scatter(zip_code, per_capita, c='red')

title = "Per Capita Income ($) vs. Zip Code"
plt.title(title, fontsize=20)

plt.xlabel('Zip Code', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Per Capita Income ($)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()