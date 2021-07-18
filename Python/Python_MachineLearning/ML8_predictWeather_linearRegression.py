"""
    ? ทดสอบจากข้อมูลอุณหภมูิจริง
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.formats import style 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")

# Training set and Test set
x = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# Training
model = LinearRegression()
model.fit(x_train,y_train)

# Test
y_predict = model.predict(x_test)

# compare true data & predict data
df = pd.DataFrame({'Actually':y_test.flatten(),'predicted':y_predict.flatten()})

print("MAE = ",metrics.mean_absolute_error(y_test,y_predict))
print("MSE = ",metrics.mean_squared_error(y_test,y_predict))
print("RMSE = ",np.sqrt(metrics.mean_squared_error(y_test,y_predict)))

print('Score = ',metrics.r2_score(y_test,y_predict))