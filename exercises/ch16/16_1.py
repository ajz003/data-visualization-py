import csv
from datetime import datetime

from matplotlib import pyplot as plt

target_year = input("Please input the year of the data you'd like to see: ")

filename = 'rdu-weather-history.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = float(row[2])
            low = float(row[1])
        except ValueError:
            print(date, high , low, 'missing data')
        else:
            if target_year in str(date.year):
                dates.append(date)
                highs.append(high)
                lows.append(low)


dates.sort()


fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily high and low temperatures in " + target_year + ", Raleigh-Durham International Airport"
plt.title(title, fontsize=20)

plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()