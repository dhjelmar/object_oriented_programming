#!$HOME/.conda/envs/py39/bin/python

#%%
# VSCode: C-S-p 'Python: Select Interpreter'
import pandas as pd
import numpy as np

########################################################################## 
#%%
# DATA TYPES

## simple data types
# immutable = xxxxxxxxxxxxxx
# mutable   = xxxxxxxxxxxxxx
mytuple = ('a', 'b', 'c')  # immutable
mylist  = ['a', 'b', 'c']  # mutable
# dictionary expects key:(value) entries where value can be multidimensional
mydict = {'a':(1,2), 'b':(2,3), 'c':(3,4), 'd':('five', 'six'), 'e':[7,8]} 
# can transform dictionary into dataframe if same number of entries for each key
mydf = pd.DataFrame(mydict)
mymatrix = np.array(mydf)


########################################################################## 
#%%
# DATAFRAMES

#%%
# print dataframe
print(mydf)

#%%
# extract dataframe value
print("mydf.loc[1, 'd'] =", mydf.loc[1, 'd'])

#%%
# extract dataframe column
print("mydf['c'] =")
print(mydf['c'])
print()
print("mydf['c'].tolist() =", mydf['c'].tolist())
print()
print("list(mydf['c']) =", list(mydf['c']), " but slower and different type")

#%%
# extract dataframe row
print("mydf.loc[1,] =")
print(mydf.loc[1,])
print()
print("mydf.loc[mydf.b==3,] =")
print(mydf.loc[mydf.b==3,])
print()
print("mydf.loc[1,].tolist() =", mydf.loc[1,].tolist())

#%%
# move some columns to front of dataframe without specifying all columns in dataframe
def first(df, first):
    '''
    df    = dataframe
    first = list of columns to move to front of df
    '''
    new_column_order = first + [col for col in df.columns if col not in first]
    df = df[new_column_order]
    return df

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': [10, 11, 12],
    'E': [13, 14, 15]
})
df = first(df, ['E', 'C'])
df

#%%
# delete columns
df = mydf.drop(columns=['c','d'])
df


########################################################################## 
#%%
# MATRICES (NUMPY)

#%%
# print dataframe
print(mymatrix)

#%%
# extract dataframe value
print("mymatrix[1, 3] =", mymatrix[1, 3])

#%%
##############################
# dlh - not working yet
##############################
# extract matrix column
print("mymatrix[2] =")
print(mymatrix[2])
#print()
#print("mymatrix[2].tolist() =", mymatrix[2].tolist())
#print()
#print("list(mymatrix[2]) =", list(mymatrix[2]), " but slower and different type")

#%%
##############################
# dlh - not working yet
##############################
print("mymatrix.loc[1,] =")
print(mymatrix.loc[1,])
print()
print("mymatrix.loc[mymatrix.b==3,] =")
print(mymatrix.loc[mymatrix.b==3,])
print()
print("mymatrix.loc[1,].tolist() =", mymatrix.loc[1,].tolist())



###############################################################
##%%
## data types can also be complex
complex_tuple = (1, 'b', ('c', 'd'), ['e', 'f'])
complex_list =[1, 'b', ('c', 'd'), ['e', 'f']]
# a dictionary is a list with a key for each list item
complex_mydict = {'a':1, 'b':(3,4), 'c': [1,2,3], 'd':mymatrix, 'e':mydf, 'f':complex_list}

#%%
## dictionary views
mydict = complex_mydict
print('mydict.keys()')
print(mydict.keys())

print()
print('list(mydict.items())')
print(list(mydict.items()))

#%%
print()
print("mydict['a'] is a value   = ", mydict['a'])

print()
print("mydict['b'] is a tuple   = ", mydict['b'])
print("mydict['b'][1]           = ", mydict['b'][1])

print()
print("mydict['c'] is a list    = ", mydict['c'])
print("mydict['c'][1]           = ", mydict['c'][1])

print()
print("mydict['d'] is a matrix")
print(mydict['d'])
print("mydict['d'][1,3]         = ", mydict['d'][1,3])

print()
print("mydict['e'] is a dataframe")
print(mydict['e'])
print("mydict['e'].loc[1,'d'] = ", mydict['e'].loc[1,'d'])
print("mydf.loc[1,'d']        = ", mydf.loc[1,'d'])

print()
print("mydict['f'] is another list")
print(mydict['f'])

# %%

## adding to list
mylist  = ['a', 'b', 'c']
mylist2 = ['d', 'e']
mylist = mylist + mylist2
print(mylist)

## add to list
mylist.append(['f', 'g'])
mylist.append('h')
mylist.append('i')
#mylist.append(mylist2)
#mylist.append('f')
#mylist.append(mylist2)
print(mylist)

## can flatten the list
from itertools import chain
list(chain.from_iterable(mylist))

# %%
## use enumerate to get a counter as work through list or tuple
for i, thing in enumerate(mylist):
    print('i = ', i, ' , thing = ', thing)


#%%
# enumerate dictionary runs through each key
for i, key in enumerate(mydict):
    print('i = ', i, ' , key = ', key, ', value = mydict[key] = ', mydict[key])

# %%
