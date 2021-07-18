import pandas as pd

df = pd.read_csv('dirtydata.csv')

# df.loc[7, 'Duration'] = 45

# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.loc[x, 'Duration'] = 120

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace=True)

print(df.to_string())