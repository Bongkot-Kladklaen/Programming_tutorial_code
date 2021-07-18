import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# การจำลองข้อมูล
rng = np.random
x = rng.rand(50) * 10
y = 2*x+rng.randn(50)

# Linear regression model
model = LinearRegression()

x_new = x.reshape(-1,1)

# Training data model
model.fit(x_new,y)

# Test model
xfit = np.linspace(-1,11)
xfit_new = xfit.reshape(-1,1)

yfit = model.predict(xfit_new)

# analysis model
plt.scatter(x,y)
plt.plot(xfit,yfit)
plt.show()