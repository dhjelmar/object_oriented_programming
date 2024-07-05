#!$HOME/.conda/envs/py39/bin/python

#%%
# C-S-p 'Python: Select Interpreter'
import pandas as pd
import numpy as np

#%%
## data types
mytuple = ('a', 'b', 'c')  # immutable
mylist  = ['a', 'b', 'c']  # mutable
# dictionary expects key:(value) entries where value can be multidimensional
mydict = {'a':(1,2), 'b':(2,3), 'c':(3,4), 'd':('five', 'six'), 'e':[7,8]} 
# can transform dictionary into dataframe if same number of entries for each key
mydf = pd.DataFrame(mydict)
mymatrix = np.array(mydf)

#%%
## data types can also be complex
complex_tuple = (1, 'b', ('c', 'd'), ['e', 'f'])
complex_list =[1, 'b', ('c', 'd'), ['e', 'f']]
# a dictionary is a list with a key for each list item
complex_mydict = {'a':1, 'b':2, 'c':(3,4), 'd':('five', 'six'), 'e':[7,8]} 
complex_mydict = {'a':1, 'b':(3,4), 'c': [1,2,3], 'd':mymatrix, 'e':mydf, 'f':complex_list}

#%%
## views
mydict = complex_mydict
print('mydict.keys()')
print(mydict.keys())

print()
print('list(mydict.items())')
print(list(mydict.items()))

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
mylist2 = ['d', 'e']
mylist.append(mylist2)
mylist.append('f')
mylist.append(mylist2)
print(mylist)


#%%
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
########################################################################
## Error handling
age = input('Enter age as integer')
try:
    ## attempt coding that may throw an error
    age = int(age)
    print('Good number entered')
except:
    ## coding to handle the error
    print('Invalid number')

    ## Alternatley, can use, for example, "except ValueError:"
    ## Python Standard Library errors can be TypeError, ValueError, NameError, 
    ## ZeroDivisionError, and several others

# %%
## more complicated example with raise and exception name

## use of raise to exit the method and return control back to the caller
## which then needs to catch the exception in its except clause and so on
## until the error is caught. If not caught, the program quits and an error
## is displayed.

class myexception(Exception):
    pass

age = input('Enter age as integer')
try:
    age = int(age)
    print('Good number entered')
except ValueError:  # ValueError is a standard Python exception; others include TypeError, NameError, ZeroDivisionError...
    raise myexception('Invalid number')
    ## or do not define custom exception and use
    ## raise Exception('Invalid number')

# %%
