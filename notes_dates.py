#%%
# importing pandas module
import pandas as pd
import datetime as dt

# create pandas DataFrame with one column with five 
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
# COMPARE DATES

#%%
# choose row to focus on
irow = 1


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
## LOOK AT DIFFERENT CONVERSIONS

#%%
# convert all columns to just date
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
# convert all columns to datetime
# following makes all dates in row 0 equivalent (and they should be)
# following makes all dates in row 1 equivalent where they should be
dfc = df.copy()
for i in range(0,ncols):
    dfc.iloc[:,i] = pd.to_datetime(dfc.iloc[:,i])
dfc
#%%
print('for irow=', irow)
compare(dfc)

#%% [markdown]
## CONCLUSION
# The last example above using pd.to_datetime(dfc.iloc['date'], utc=True)
# seems to behave most consistently. 
#%%