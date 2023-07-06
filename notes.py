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
list(chain.from_iterable(my_list))

# %%
## use enumerate to get a counter as work through list or tuple
for i, thing in enumerate(mylist):
    print('i = ', i, ' , thing = ', thing)

# %%
