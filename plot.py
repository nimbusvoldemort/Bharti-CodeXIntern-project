
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Load data
data = pd.read_csv('temp_new_york_2016.csv',index_col='date')  # Replace with your actual file path
daily_temp_df=data['average temperature']

# # Group data into weeks (7 days per week)
weekly_temp_data = [np.mean(daily_temp_df[i:i+7]) for i in range(0, 364, 7)]

# Reshape weekly temperature data to plot as a heatmap (assuming 52 weeks)

# Let's reshape the data into a 4x13 grid (to represent 52 weeks
weekly_temp_matrix = np.array(weekly_temp_data).reshape(4, 13)

plt.figure(figsize=(10, 6))
sns.heatmap(weekly_temp_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Adding titles and labels
plt.title('Weekly Average Temperature Heatmap')
plt.xlabel('Week')
plt.ylabel('Month-like Groupings')

# Show the plot
plt.show()



# Create a list of week numbers
weeks = list(range(1, 53))  # 52 weeks in a year

# Plotting the bar plot
plt.figure(figsize=(10, 6))
plt.bar(weeks, weekly_temp_data, color='skyblue')

# Adding titles and labels
plt.title('Weekly Average Temperature Bar Plot')
plt.xlabel('Week Number')
plt.ylabel('Average Temperature (°C)')

# Display the plot
plt.show()


min_temp_df = data['minimum temperature']  # Replace with actual min temperature data
max_temp_df = data['maximum temperature']  # Max temps slightly higher than min

# Combine daily min, max, and avg temperature data into a 2D array
daily_temp_data = np.vstack([min_temp_df, max_temp_df, daily_temp_df])

# Group data into weeks (7 days per week)
weekly_temp_data_bar = [daily_temp_data[:, i:i+7] for i in range(0, 364, 7)]
weekly_temp_data_bar.append(daily_temp_data[:, 364:])  # Handle the last few days separately

# Flatten the weekly data so that each week can be a separate box in the box plot
weekly_min_max_avg_data = [np.concatenate(week) for week in weekly_temp_data_bar]

# Plotting the weekly box plot
plt.figure(figsize=(20, 6))
plt.boxplot(weekly_min_max_avg_data, patch_artist=True, boxprops=dict(facecolor='lightblue'))

# Adding titles and labels
plt.title('Weekly Box Plot of Min, Max, and Avg Daily Temperatures')
plt.xlabel('Week Number')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 53), range(1, 53))  # Labeling x-axis for each week (1-52)

# Display the plot
plt.show()


# Plotting the line plot
plt.figure(figsize=(10, 6))
plt.plot(weeks, weekly_temp_data, marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Weekly Average Temperature Line Plot')
plt.xlabel('Week Number')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)

# Display the plot
plt.show()