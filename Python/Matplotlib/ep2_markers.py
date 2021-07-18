import matplotlib.pyplot as plt 
import numpy as np 

'''
    #? ปรับเปลี่ยนจุดในการแสดงผลด้วย parameter marker='o' มีให้เลือกหลายรูปแบบ
    #? shortcut parameter  marker|line|color -> 'o:r' format strings
    #? เพิ่มขนาดจุดด้วย parameter markersize = '20' หรือ ms = '20'
    #? ปรับสีขอบของจุดด้วย parameter markeredgecolor = 'r' หรือ mec = 'r'
    #? ปรับสีของจุดด้วย parameter markerfacecolor = 'r' หรือ mfc = 'r'
'''

y = np.array([3,8,1,10])

# plt.plot(y, marker='o')
# plt.plot(y, 'o:r')
# plt.plot(y, marker = 'o', ms = 20)
# plt.plot(y, marker = 'o', ms = 20, mec='r')
plt.plot(y, marker = 'o', ms = 20, mfc='r')
plt.show()