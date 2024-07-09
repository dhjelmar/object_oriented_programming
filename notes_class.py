#!$HOME/.conda/envs/py39/bin/python

#%%
# C-S-p 'Python: Select Interpreter'
import pandas as pd
import numpy as np

########################################################################
# %%
## Error handling
y = 0
try:
    ## attempt coding that may throw an error
    div = 10 / y
    print('Good number entered')
except:
    ## coding to handle the error
    print('Error: Divide by zero')

    ## Alternatley, can use, for example, "except ValueError:"
    ## Python Standard Library errors can be TypeError, ValueError, NameError, 
    ## ZeroDivisionError, and several others


###########################################################
# %%
## more complicated example with raise and exception name

## use of raise to exit the method and return control back to the caller
## which then needs to catch the exception in its except clause and so on
## until the error is caught. If not caught, the program quits and an error
## is displayed.

# use a class for exceptions
class error(Exception):
    '''raise this error'''
    pass
    #def __init__(self, message):
    #    super.__init__(message)


###########################################################
#%%
# SIMPLE CLASS EXAMPLE
class myclass():
    '''
    class object: takes arguments x and y
                  has functions for x+y and x/y
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumit(self):
        answer = self.x + self.y
        return answer
    
    def divideit(self):
        try:
            # answer = self.x / self.y
            xx = self.x
            answer = xx / self.y
        except ZeroDivisionError as e:
            print('e = ', e)
            #return ValueError('Error: divide by zero error')
            #return error('Error: divide by zero error')
            raise error('Error: divide by zero error') from None   # none sends back less error messaging
            # answer = 0
        return answer

##########################################################
#%%
# Simple use of myclass
ob1 =  myclass(1,2)
print('x      = ', ob1.x)
print('y      = ', ob1.y)
print('sum    = ', ob1.sumit())
print('divide = ', ob1.divideit())

#%%
# Test for exception error
ob2 = myclass(3,0)
ob2.sumit()

ob2.divideit()
#%%
