import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')            
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)

    sit_highs = []
    sit_dates = []
    sit_lows = []
    for row in reader:
        try:
            sit_date = datetime.strptime(row[0], '%Y-%m-%d')            
            sit_high = int(row[1])
            sit_low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            sit_highs.append(sit_high)
            sit_lows.append(sit_low)
            sit_dates.append(sit_date)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.plot(sit_dates, sit_highs, c='yellow', alpha=0.5)
plt.plot(sit_dates, sit_lows, c='purple', alpha=0.5)
plt.fill_between(sit_dates, sit_highs, sit_lows, facecolor='green', alpha=0.5)

# Label the data.
plt.title("Daily high and low temperatures - 2014\n Death Valley, CA", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()