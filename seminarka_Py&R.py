# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt
import folium
import pyproj

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DATA LOADINT AND PREPARATION

# Path to file
path = "files/HlmestoPraha2019.csv"

# Read csv
df = pd.read_csv(path, sep=';', engine='python', header=None)

# Name columns
df.columns = ['p1', 'p36', 'p37', 'p2a', 'weekday(p2a)', 'p2b', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13a',
              'p13b', 'p13c', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p27', 'p28',
              'p34', 'p35', 'p39', 'p44', 'p45a', 'p47', 'p48a', 'p49', 'p50a', 'p50b', 'p51', 'p52', 'p53', 'p55a',
              'p57', 'p58', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'p5a']
# Subset dataframe to handpicked columns
df_subset = df[
    ['p2a', 'p37', 'p6', 'p9', 'p10', 'p11', 'p12', 'p13a', 'p13b', 'p13c', 'p15', 'p16', 'p18', 'p34', 'p35', 'p36',
     'p44', 'd', 'e']]

df_subset['p2a'] = pd.to_datetime(df_subset['p2a'], format='%d.%m.%Y')  # Convert column to date-time format
df_subset['p2a'] = df_subset['p2a'] + pd.to_timedelta(df_subset['p37'], unit='h')  # Add hour into datetime
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - ACCIDENTS PER MONTH

accidents_month = df_subset.groupby(df_subset['p2a'].dt.month).count().p2a  # Count number of accidents by month
accidents_month.index = [calendar.month_name[x] for x in range(1, 13)]  # Replace the month integers by month names.

plt.style.use('ggplot')  # Create ggplot style barplot

accidents_month.plot(kind='bar', figsize=(12, 7), color='green', alpha=0.5)  # plot accidents per month

# title and x,y labels
plt.title('Accidents in Prague in 2019', fontsize=23)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of accidents', fontsize=15)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - ACCIDENTS PER DAY OF THE WEEK

accidents_day = df_subset.groupby(df_subset['p2a'].dt.dayofweek).count().p2a  # Number of accident per day of the week
accidents_day.index = [calendar.day_name[x] for x in range(0, 7)]  # Replace the day integers by day names.

accidents_day.plot(kind='bar', figsize=(12, 7), color='blue', alpha=0.5)  # plot accidents per day

# title and x,y labels
plt.title('Accidents in Prague in 2019', fontsize=23)
plt.xlabel('Day of the week', fontsize=15)
plt.ylabel('Number of accidents', fontsize=15)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - ACCIDENTS BY NUMBER OF VEHICLES INVOLVED

vehicles_involved = df_subset.p34.value_counts()  # The number of accidents according to the number of vehicles involved

# Add 0 to number of accidents that we do not have
vehicles_involved[8] = 0
vehicles_involved[10] = 0
vehicles_involved[11] = 0
vehicles_involved[12] = 0
vehicles_involved[13] = 0
vehicles_involved[14] = 0

vehicles_involved.sort_index(inplace=True)
vehicles_involved.plot(kind='bar', figsize=(12, 7), color='darkgreen', alpha=0.5)  # Plot number of car accidents

# Title and x,y labels
plt.title('Accidents in Prague in 2019', fontsize=23)
plt.xlabel('Vehicles involved', fontsize=15)
plt.ylabel('Number of accidents', fontsize=15);

# Add label to each bar of the plot
for index in vehicles_involved.index:
    plt.text(x=index, y=vehicles_involved.loc[index], s=str(vehicles_involved.loc[index]), horizontalalignment='center')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - ACCIDENTS BY TYPE OF INJURY

injuries = df[['p13a', 'p13b', 'p13c']].sum()  # Count number of imjuries

injuries.plot(kind='pie', figsize=(7, 7), colors=['black', 'red', 'green'], labels=None, autopct='%1.1f%%', fontsize=15,
              pctdistance=1.2)  # Pie plot with the percentages

# Legend and title
plt.legend(labels=['Deaths', 'Serious Injuries', 'Mild Injuries'])
plt.title('Injuries in Prague in 2019', fontsize=23)
plt.ylabel('')
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - RATE OF INJURY BY DAY OF THE WEEK

accidents_serious = df_subset[df_subset['p13b'] != 0].groupby(
    df_subset['p2a'].dt.dayofweek).sum().p13b  # Number of serious injuries per day of the week
rate_serious = accidents_serious / accidents_serious.sum()

accidents_mild = df_subset[df_subset['p13c'] != 0].groupby(
    df_subset['p2a'].dt.dayofweek).sum().p13c  # Number of mild injuries per day of the week
rate_mild = accidents_mild / accidents_mild.sum()

accidents_deaths = df_subset[df_subset['p13a'] != 0].groupby(
    df_subset['p2a'].dt.dayofweek).sum().p13a  # Number of mild injuries per day of the week
rate_deaths = accidents_deaths / accidents_deaths.sum()

# Combine series to data frame
rates = pd.DataFrame({'Serious injures': rate_serious, 'Mild injuries': rate_mild, 'Deaths': rate_deaths})
rates.plot(kind='bar', figsize=(12, 7), color=['red', 'green', 'black'], alpha=0.5)

# Title and labels
plt.title('Rate of injuries type by day of the week', fontsize=23)
plt.xlabel('Day of the week', fontsize=15)
plt.ylabel('Percentage', fontsize=15)
plt.xticks(np.arange(7), [calendar.day_name[x] for x in range(0, 7)]);

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PLOT - MAIN CAUSE OF ACCIDENTS

# Divide accidents into categories
p12a = sum(1 for i in df_subset['p12'] if i == 100)
p12b = sum(1 for i in df_subset['p12'] if i >= 201 and i <= 219)
p12c = sum(1 for i in df_subset['p12'] if i >= 301 and i <= 311)
p12d = sum(1 for i in df_subset['p12'] if i >= 401 and i <= 414)
p12e = sum(1 for i in df_subset['p12'] if i >= 501 and i <= 416)
p12f = sum(1 for i in df_subset['p12'] if i >= 601 and i <= 615)

# Create one data frame, drop empty column, transpose and name
causes = pd.DataFrame(
    {'driver_innocent': [p12a], 'high_speed': [p12b], 'wrong_overtaking': [p12c], 'right_of_way': [p12d],
     'wrong_driving': [p12e], 'technical_problems': [p12f]})
causes = causes.drop(columns=['wrong_driving'], axis=1)
causes = causes.transpose()
causes.columns = ['number of accidents']

# Create pie plot
causes.plot(kind='pie', subplots=True, figsize=(10, 10), labels=None, autopct='%1.1f%%', fontsize=15, pctdistance=1.2)

# Title and labels
plt.legend(
    labels=['Nezaviněná řidičem', 'Nepřiměřená rychlost jízdy', 'Nesprávné předjíždění', 'Nedání přednosti v jízdě',
            'Technická závada vozidla'], loc="lower right")
plt.title('Hlavní příčiny dopravních nehod v Praze v roce 2019', fontsize=23)
plt.ylabel('')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAP OF PRAGUE SHOWING ALL THE ACCIDENTS

# Convert coordinates to correct format
proj = pyproj.Transformer.from_crs(5514, 4326, always_xy=True)

x1, y1 = (df_subset['d'], df_subset['e'])
x2, y2 = proj.transform(x1, y1)

df_subset['lat'] = y2
df_subset['lon'] = x2

# Create basic map
map = folium.Map(location=[50.0784, 14.4728], zoom_start=12)

# Add markers on the map
for lat, lng in zip(df_subset.lat, df_subset.lon):
    folium.features.CircleMarker(
        [lat, lng],
        radius=3,
        color='red',
        fill=True,
        fill_color='darkred',
        fill_opacity=0.6
    ).add_to(map)

# Need to save it and open in web browser or use display it in notebook
map.save("index.html")
