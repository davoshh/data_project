import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_1 = 'data/death_valley_2018_simple.csv'
filename_2 = 'data/sitka_weather_2018_simple.csv'

with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get data for Death Valley.
    dates_dv = []
    highs_dv = []
    lows_dv = []

    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates_dv.append(date)
            highs_dv.append(high)
            lows_dv.append(low)

# Get data for Sitka.
with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_st = []
    highs_st = []
    lows_st = []

    for row in reader:
        try:
            date = int(row[2])
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates_st.append(date)
            highs_st.append(high)
            lows_st.append(low)

# Plot the data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_dv, highs_dv, c='red', alpha=0.5)
ax.plot(dates_dv, lows_dv, c='blue', alpha=0.5)
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)

ax.plot(dates_dv, highs_st, c='red', alpha=0.5)
ax.plot(dates_dv, lows_st, c='blue', alpha=0.5)
ax.fill_between(dates_dv, highs_st, lows_st, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley and Sitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
