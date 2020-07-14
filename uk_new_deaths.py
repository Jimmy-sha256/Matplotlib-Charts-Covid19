import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

df = pd.read_csv("/UK_Data/uk_new_death_data.csv") # extract data from csv

df = df.rename(columns={'newDeathsByPublishDate': 'new_deaths'}) # rename column

df['date'] = pd.to_datetime(df['date']) # convert date to pandas date.time

df = df.groupby(df['date'].dt.date).sum() # aggregate columns with same date and calculate the sum

del df['cumDeathsByPublishDate'] # delete cumulative data column

df.reset_index(level=0, inplace=True) # reset index

df['date'] = pd.to_datetime(df['date']) # convert date to pandas date.time

df['new_deaths'] = pd.to_numeric(df['new_deaths']) # convert data to pandas numeric

df['new_deaths_average'] = df['new_deaths'].rolling(7).mean() # calculate 7 day average

plt.figure(figsize=(20,15), facecolor='lightgray') # set chart size / border color
plt.bar(df['date'], df['new_deaths']) # plot bar chart
plt.plot(df['date'], df['new_deaths_average'], label='7 Day Average', linewidth=4.0, color='red') # plot average

# format x axis
ax = plt.gca()
ax.set_facecolor('lightgray') # set background color
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set date interval
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m')) # format date

plt.suptitle('UK New Deaths', fontsize=30) # set title
plt.tight_layout() # move title inside chart
plt.xlabel("Date", fontsize=15) # set x axis label
plt.ylabel("New Deaths", fontsize=15) # set y axis label


plt.gcf().autofmt_xdate() # Rotation
plt.legend() # set legend
plt.show() # show chart
