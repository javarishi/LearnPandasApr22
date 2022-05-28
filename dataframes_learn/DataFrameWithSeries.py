'''
Created on 26-May-2022

@author: Rishi
'''
import pandas as pd

d = {
    'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

# Column Selection
print (df ['one'])
print (df ['two'])

df['three']=pd.Series([10,20,30],index=['a','b','c'])
print ("Adding a new column by passing as Series:")
print (df)
df['sum'] = df ['one'] + df ['two'] + df['three']
print (df)


print ("Deleting the first column using DEL function:")
del df['one']
print(df)

print ("Deleting another column using POP function:")
df.pop('two')
print (df)
