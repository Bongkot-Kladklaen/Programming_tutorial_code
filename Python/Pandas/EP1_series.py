import pandas as pd

a = [1, 7, 2]

calories = {
    "day1":420,
    "day2":380,
    "day3":390
    }

myvar = pd.Series(a, index=['x','y','z'])
myvar2 = pd.Series(calories)
myvar3 = pd.Series(calories, index=['day1','day2'])

# print(myvar['x'])
# print(myvar2)
print(myvar3)