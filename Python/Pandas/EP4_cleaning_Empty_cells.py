import pandas as pd

df = pd.read_csv('dirtydata.csv')

# new_df = df.dropna()
# df.dropna(inplace=True)
# df.fillna(130, inplace = True)
# df['Calories'].fillna(130, inplace=True)

'''
x = df['Calories'].mean()
df['Calories'].fillna(x, inplace=True)
'''

'''
x = df['Calories'].median()
df['Calories'].fillna(x, inplace=True)
'''

x = df['Calories'].mode()[0]
df['Calories'].fillna(x, inplace=True)

# print(new_df.to_string())
print(df.to_string())