import matplotlib.pyplot as plt 
import numpy as np 

'''
    #? ปรับการแสดงผลของเส้นด้วย parameter linestyle='dotted' หรือ ls='dotted'
    #? ปรับสีเส้นด้วย parameter color='r' หรือ c='r'
    #? ปรับขนาดเส้นด้วย parameter linewidth='20' หรือ lw='20'
    #? Multiline plot(x1,y1,x2,y2, x(n), y(n))
'''

y = np.array([3, 8, 1, 10])

# plt.plot(y, linestyle = 'dotted')
# plt.plot(y, color = 'r')
# plt.plot(y, lw = '10')


#? Multiline
x1 = np.array([0, 2, 4, 6])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 2, 4, 6])
y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)
plt.plot(x1,y1,x2,y2)

plt.show()
