import numpy as np
import pandas as pd

df1 = pd.read_csv("./Bookings.csv")
df2 = pd.read_csv("./Bookings.csv")
#print(df2.info())
#print(df2.describe())
#print(df2.describe(include='str'))
#print(df2.describe(exclude='str'))
print(df1['Review'].value_counts())
df1.loc[df1['Review'] == 'Superb 9.0', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Superb ', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Exceptional 10', 'Review'] = "Exceptional"
df1.loc[df1['Review'] == 'Exceptional ', 'Review'] = "Exceptional"
print(df1['Review'].value_counts())