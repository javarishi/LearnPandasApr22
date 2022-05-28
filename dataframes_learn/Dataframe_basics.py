'''
Created on 26-May-2022

@author: Rishi
'''
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data, columns=['Name', 'Marks'], dtype=float)
#print (df)
# ValueError: All arrays must be of the same length
data = {
    'Name':['Tom', 'Jack', 'Steve', 'Robert'],
    'Age':[28,34,29, 10]
    }
df = pd.DataFrame(data)
#print (df)

data = [
        {'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}
        ]
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'd'])
print (df)

