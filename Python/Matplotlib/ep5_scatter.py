import matplotlib.pyplot as plt
import numpy as np

'''
    #? Scatter plot การพร็อตแบบกระจาย
    #? ColorMap สีที่มีมาให้ใน matplotlib เรียกใช้ด้วย parameter cmap='viridis'
    #? เพิ่มแทบสีของ colormap ไปในพล็อตได้ด้วย plt.colorbar()
    #? เพิ่มขนาดจุดสำหรับของ scatter ด้วย parameter s = 10
    #? ปรับความโปร่งแสงของจุดด้วย parameter alpha = 0.5
'''
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

#? การเปรียบเทียบพล็อต
#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x, y, s=50, alpha=0.5)

plt.colorbar()
plt.show()
