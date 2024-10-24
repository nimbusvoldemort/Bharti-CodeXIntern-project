# import pandas library
import pandas as pd

# read csv file and create a dataframe of new york 2016 temperature data
file_path = 'temp_new_york_2016.csv'
temp_df = pd.read_csv(file_path,index_col="date")

# print the first five rows of the dataframe
print(temp_df.head())

# print the summary statistics of the dataframe
print(temp_df.describe())

