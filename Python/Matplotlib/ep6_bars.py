import matplotlib.pyplot as plt
import numpy as np

'''
    #? การพล็อตกราฟแท่ง
    #? แสดงกราฟแนวนอนด้วย plt.bart()
    #? ปรับขนาดด้วย parameter width=0.1
'''

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
