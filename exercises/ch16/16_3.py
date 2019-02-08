import csv
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt

target_year = "2014"

filename = 'rdu-weather-history.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rainfall = [], []

    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            rain = float(row[3])
        except ValueError:
            print(date, rainfall, 'missing data')
        else:
            if target_year in str(date.year):
                dates.append(date)
                rainfall.append(rain)


dates.sort()




fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfall, c='red', alpha=0.5)

title = "Daily Rainfall in Raleigh-Durham International Airport, " +  target_year
plt.title(title, fontsize=20)



plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)


plt.yticks(np.arange(min(rainfall), max(rainfall)+1, 0.5)) # (np.arange was used rather than Python's range function just in case min(x) and max(x) are floats instead of ints.)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()