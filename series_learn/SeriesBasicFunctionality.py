'''
Created on 24-May-2022

@author: Rishi
'''
import pandas as pd
import numpy as np

#Create a series with 25 random numbers
s = pd.Series(np.random.randn(10))
print (s)
print ("The axes are:")
print (s.axes)
print ("Is the Object empty?")
print (s.empty)
print ("The dimensions of the object:")
print (s.ndim)
print ("The size of the object:")
print (s.size)
print ("The actual data series is:")
print (s.values)
print ("The first two rows of the data series:")
print (s.head())
print ("The last two rows of the data series:")
print (s.tail())

