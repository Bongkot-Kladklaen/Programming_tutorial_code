import pandas as pd

data = {
    'calories': [230, 280, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data, index=['day1','day2','day3'])
# print(df)
# print(df.loc[0])
# print(df.loc[[0, 1]])

# print(df2)
print(df2.loc['day2'])
print(df2.loc[['day1','day2']])