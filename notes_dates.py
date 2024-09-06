# importing pandas module
import pandas as pd
 
# create pandas DataFrame with one column with five 
# datetime values through a dictionary
df = pd.DataFrame({'DateTime': ['2021-01-15 20:02:11', 
                                '1989-05-24 20:34:11',
                                '2020-01-18 14:43:24',
                                '2021-01-15 20:02:10',
                                '1999-04-04 20:34:11']})
 
print("Original data")
print(df)

# convert datetime column to just date
df['Date'] = pd.to_datetime(df['DateTime']).dt.date
 
# display
print("Only date")
print(df)

print('datetime type =', type(df.DateTime[0]))
print('date.    type =', type(df.Date[0]))