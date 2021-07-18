import matplotlib.pyplot as plt
import numpy as np

'''
    #? แสดงกราฟหลายกราฟพร้อมกัน subplots(row,col,plot)
    #? ใส่หัวเรื่องให้ plot แต่ละ plot ด้วย title()
    #? ใส่หัวเรื่องให้กับหน้าแสดง plot ด้วย suptitle()
'''

#*plot 1:

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x, y)
plt.title('first')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x, y)
plt.title('second')

plt.suptitle('My plot')
plt.show()