# %%
import pandas as pd
import numpy as np

## data types
mytuple = ('a', 'b', 'c')  # immutable
mylist  = ['a', 'b', 'c']  # mutable
mydict = {'a':(1,2), 'b':(2,3), 'c':(3,4), 'd':('five', 'six'), 'e':[7,8]} 
mydf = pd.DataFrame(mydict)
mymatrix = np.array(mydf)

## data types can also be complex
complex_tuple = (1, 'b', ('c', 'd'), ['e', 'f'])
complex_list =[1, 'b', ('c', 'd'), ['e', 'f']]
complex_mydict = {'a':1, 'b':2, 'c':(3,4), 'd':('five', 'six'), 'e':[7,8]} 

## views
mydict_list = list(mydict.items())
mydict['c']


# %%

## adding to list
mylist2 = ['d', 'e']
mylist.append(mylist2)
mylist.append('f')
mylist.append(mylist2)
print(mylist)

## the above is messy, so flatten with
from itertools import chain
list(chain.from_iterable(mylist))

# %%
## use enumerate to get a counter as work through list or tuple
for i, thing in enumerate(mylist):
    print('i = ', i, ' , thing = ', thing)

# %%
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
