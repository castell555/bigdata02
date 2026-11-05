import pandas as pd

df = pd.read_csv('product_inspection.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())
print(df.tail())