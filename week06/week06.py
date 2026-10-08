import seaborn as sns
import pandas as pd
import numpy as np

df = pd.DataFrame([['A', 1],['A', 1],['A', 1],['B', 10],['B', 10]], columns=['group', 'value'])

df1 = pd.DataFrame({'group':['A','A','A','B','B'], 'value':[1,1,1,10,10]})

print(df)
print(df.groupby([0,0,1,1,1])['value'].sum())
s = pd.Series([True, False, True, False, True])
print(df.groupby(s)['value'].sum())