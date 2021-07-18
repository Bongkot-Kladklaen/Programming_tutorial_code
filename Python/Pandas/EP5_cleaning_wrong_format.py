import pandas as pd

df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())