import numpy as np
import matplotlib.pyplot as plt

#? แสดงเป็นเส้นตรง
# x = np.linspace(-5,5,100)
# # y = 2*x+1

# # plt.plot(x, y, '-r', label='y=2x+1')
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='upper left')
# plt.title("Graph y=2x+1")
# plt.grid()
# plt.show()

#? แสดงเเบบกระจาย
rng = np.random
x = rng.rand(50) * 10
y = 2*x+rng.randn(50)

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.title("Graph y=2x+1")
plt.grid()
plt.show()

