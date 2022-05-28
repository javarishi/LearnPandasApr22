'''
Created on 24-May-2022

@author: Rishi
'''
import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[101, 102, 103, 104])
print(data)
print("*************")
print(s)
print("*************")
index_list = np.arange(100, (data.size + 1)*100, 100)
s = pd.Series(data, index=index_list)
print(s)
print("*************")

data = {'a' : 0.0, 'b' : 1.0, 'c' : 2.0}
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)

print("*************")
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)


