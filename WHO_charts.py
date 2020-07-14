import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

df = pd.read_csv("/WHO_Data/WHO-COVID-19-global-data.csv")

df = df[['Date_reported', ' Country', ' New_cases', ' New_deaths']].copy()

df = df.rename(columns={
    ' Country': 'country',
    ' New_cases': 'new_cases',
    ' New_deaths': 'new_deaths',
    'Date_reported': 'date_reported'
})

df.country.unique()

# isolate desired country from above
df = df.loc[df['country'] == 'Spain']

country = df.iloc[0, 1]

df['date_reported'] = pd.to_datetime(df['date_reported']) # convert dates to date.time

df['new_cases'] = df['new_cases'].abs() # remove negative values

df['new_deaths'] = df['new_deaths'].abs() # remove negative values

df['new_cases_average'] = df['new_cases'].rolling(7).mean() # calculate 7 day average

df['new_deaths_average'] = df['new_deaths'].rolling(7).mean()

fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(20,15), facecolor='lightgray') # create subplots, set chart size
fig.suptitle(country, fontsize=30) # set title
plt.xlabel("Date", fontsize=15) # set x axis label

# new deaths subplot
ax0.bar(df['date_reported'], df['new_deaths'], color='blue') # plot bar chart
ax0.plot(df['date_reported'], df['new_deaths_average'], label='7 Day Average', linewidth=4.0, color='red') # plot line chart
ax0.tick_params(axis='y', colors='black') # change tick color
ax0.set_facecolor('lightgray')
ax0.set(ylabel="New Deaths")

# new cases subplot
ax1.bar(df['date_reported'], df['new_cases'], color='blue') 
ax1.plot(df['date_reported'], df['new_cases_average'], label='7 Day Average', linewidth=4.0, color='red') 
ax1.tick_params(axis='y', colors='black') 
ax1.tick_params(axis='x', colors='black')
ax1.set_facecolor('lightgray')
ax1.set(ylabel="New Cases")

# format dates axis
axs = plt.gca()
axs.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set intervals
axs.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m')) # set date format

plt.gcf().autofmt_xdate() # rotation

ax0.legend() # show legend
ax1.legend() 

plt.show() # show chart
