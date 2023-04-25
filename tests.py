import pandas as pd

# Put the data into a Pandas Dataframe.
df = pd.read_csv('river.csv')

# Compute the average temperature across all 4 days.
avg_temp = df['temp'].mean()
print(f"Average temperature: {avg_temp:.2f}")

""" 
Add a new column 'tempincrease' with the increase or 
decrease of the water temperature since the day before.
"""
df['tempincrease'] = df['temp'].diff()
df.loc[0, 'tempincrease'] = 0
print("Temperature increasement since the day before")
print(df['tempincrease'])

# Compute the average of the 'tempincrease' column.
avg_tempincrease = df['tempincrease'].mean()
print(f"Average of the 'tempincrease' column: {avg_tempincrease:.2f}")

# Add a new column 'avglevel' with the average of the low and high water levels for each day.
df['avglevel'] = (df['low'] + df['high'])/2
print("Average level for each day:")
print(df['avglevel'])

# Write the DataFrame to a new CSV file name 'new.csv'.
df.to_csv("new.csv", index = False)