#%% [markdown]
## STUDY ON HOW TO DEFINE AND COMPARE DATES

#%% [markdown]
## create pandas DataFrame with various format date columns

#%%
# import pandas, datetime, and regex modules
import pandas as pd
import datetime as dt
import regex as re

#%%
# datetime values through a dictionary
df = pd.DataFrame({'YMDhms_str'       :               ['2021-01-15 00:00:00' , '1989-05-24 20:34:11'],
                   'YMD_str'          :               ['2021-01-15'          , '1989-05-24'         ],
                   'YMDhms_timestamp' :  [pd.Timestamp('2021-01-15 00:00:00'), pd.Timestamp('1989-05-24 20:34:11')],
                   'YMD_timestamp'    :  [pd.Timestamp('2021-01-15')         , pd.Timestamp('1989-05-24')],
                   'YMDhms_datetime'  :   [dt.datetime(2021, 1, 15, 0, 0, 0) , dt.datetime(1989, 5, 24, 20, 34, 11)],
                   'YMD_datetime'     :   [dt.datetime(2021, 1, 15)          , dt.datetime(1989, 5, 24)],
                   # dt.date takes max of 3 arguments
                   # 'YMDhms_date'    :       [dt.date(2021, 1, 15, 0, 0, 0) , dt.date(1989, 5, 24, 20, 34, 11)],
                   'YMD_date'         :       [dt.date(2021, 1, 15)          , dt.date(1989, 5, 24)]})

print("Original data")
print(df)

print()
print('df.dtypes')
print(df.dtypes)

print()
print('type of each column value')
ncols = df.shape[1]
for i in range(0,ncols):
    print(type(df.iloc[0,i]))

#%%
# print dataframe
df


#%% [markdown]
## COMPARE DATES

#%%
# choose row to focus on
irow = 1
print('irow=', irow)

#%%
# following shows that: pd.Timestamp and dt.datetime are equivalent
#                       dt.date is different even if Timestamp and datetime only use YYMMDD format
def compare(df):
    ncols = df.shape[1]
    for i in range(0,ncols):
        print()
        print('compare to', df.columns[i])
        for j in range(0,ncols):
            print(df.iloc[irow,i] == df.iloc[irow,j])
compare(df)

#%% [markdown]
## LOOK AT DIFFERENT CONVERSIONS FOR PANDAS COLUMNS

#%%
# convert all columns to just date using pd.to_datetime(df['date']).dt.date
# following shows that: string times now eqivalent to dt.date
#                       Timestamp and dt.datetime are still equiv but different from above
dfc = df.copy()
for i in range(0,ncols):
    dfc.iloc[:,i] = pd.to_datetime(dfc.iloc[:,i]).dt.date
dfc
#%%
print('for irow=', irow)
compare(dfc)


#%%
# convert all columns to datetime using pd.to_datetime(dfc['date'])
# following makes all dates in row 0 equivalent (and they should be)
# following makes all dates in row 1 equivalent where they should be
dfc = df.copy()
for i in range(0,ncols):
    dfc.iloc[:,i] = pd.to_datetime(dfc.iloc[:,i])
dfc
#%%
print('for irow=', irow)
compare(dfc)


#%%
## Convert pandas timestamp column to date string using df['date'].dt.strftime('%Y-%m-%d')
#%%
dfc=df.copy()
dfc['datestring'] = dfc.YMDhms_timestamp.dt.strftime('%Y-%m-%d')
dfc
#%%
print(type(dfc.datestring[0]))


#%% [markdown]
## CONVERT AND COMPARE SINGLE VALUE

#%%
YMDhms_str = '2021-01-15 11:09:08' 
YMD_str = '2021-01-15' 
#YMDhms_datetime = dt.datetime(YMDhms_str)
#YMD_datetime = dt.datetime(YMD_str)

def string2datetime(datetime_string):
    # Convert string to datetime object
    # If hour:minute:seconds are not provided, default is 00:00:00
    if (re.search(":", datetime_string)):
        format_string = '%Y-%m-%d %H:%M:%S'
    else:
        format_string = '%Y-%m-%d'
    datetime_object = dt.datetime.strptime(datetime_string, format_string)
    return datetime_object

def datetime2string(date_object, dateonly=True):
    # Convert the datetime object to a string in the specified format
    if dateonly:
        format_string = '%Y-%m-%d'
    else:
        format_string = '%Y-%m-%d %H:%M:%S'
    datetime_str = date_object.strftime(format_string)
    return datetime_str

print('convert string in datetime format to datetime')
mydate_obj = string2datetime(YMDhms_str)
print(mydate_obj)
print(type(mydate_obj))

print()
print('convert datetime to string')
mydate_str = datetime2string(mydate_obj)
print(mydate_str)
print(type(mydate_str))

print()
print('convert datetime to string with hrs:min:sec')
mydate_str = datetime2string(mydate_obj, dateonly=False)
print(mydate_str)
print(type(mydate_str))

print()
print('convert back to datetime')
mydate_obj = string2datetime(mydate_str)
print(mydate_obj)
print(type(mydate_obj))

print()
print('convert string in date only format to datetime')
mydate_obj = string2datetime(YMD_str)
print(mydate_obj)
print(type(mydate_obj))

print()
print('convert datetime to string')
mydate_str = datetime2string(mydate_obj)
print(mydate_str)
print(type(mydate_str))

#%% [markdown]
## CONCLUSION
# The last example above using pd.to_datetime(dfc.iloc['date'], utc=True)
# seems to behave most consistently. 

# Created two functions to convert single values to datetime or string.
#%%