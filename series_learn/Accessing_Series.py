'''
Created on 24-May-2022

@author: Rishi
'''
import pandas as pd 
s = pd.Series([100,200,300,400,500], index = ['a','b','c','d','e'])
print(s)

#retrieve the first element - accessing similar to String / numpy array / collection
print(s[0])
print("***** Index access ****")
#retrieve a single element
print (s[['a','b','c']])
print (s[['a','f','c']])
