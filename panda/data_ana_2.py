import numpy as np
import pandas as pd
d = {'Name':pd.Series(['manthan','sahil','tirth','samarth','dhruv','rahul','nikhil','ethan','stocin',
                       'snax','hitler','elevan']),
     'Age':pd.Series([26,27,28,29,30,31,32,33,34,35,36,37]),
     'Score':pd.Series([89,87,67,55,47,72,76,79,47,57,56,76])}

df = pd.DataFrame(d)
print(df)

columns = list(df.columns)
print(columns)

df.shape
print(df.shape)

print(df.describe())

print(df.describe(include=['object']))
print(df.describe(include='all'))