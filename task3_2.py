import pandas as pd

# load your dataset into a pandas dataframe
df = pd.read_csv('activity_botscore.csv')

# count the number of null rows before removing them
null_rows_before = df.isnull().sum().sum()

# remove null rows from the dataframe
df.dropna(inplace=True)
#count the number of null rows after removing
null_rows_after = df.isnull().sum().sum()
#printing
print(f'Number of null rows before: {null_rows_before}')
print(f'Number of null rows after: {null_rows_after}')

