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

########$$

#timestamp is the standard pandas format that should be consistent with datetime.

# Does read from excel come in as string or some date format?

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df


# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

>>> pd.to_datetime(['2018-10-26 12:00 -0530', '2018-10-26 12:00 -0500'],
...                utc=True)
DatetimeIndex(['2018-10-26 17:30:00+00:00', '2018-10-26 17:00:00+00:00'],
              dtype='datetime64[ns, UTC]', freq=None)

>>> pd.to_datetime(['2018-10-26 12:00', datetime(2020, 1, 1, 18)], utc=True)
DatetimeIndex(['2018-10-26 12:00:00+00:00', '2020-01-01 18:00:00+00:00'],
              dtype='datetime64[ns, UTC]', freq=None)