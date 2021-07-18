import numpy as np

#? การแยกอาร์เอย์ออกแบบส่วน ๆ array_split()
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.hsplit(arr, 3)
print(newarr)