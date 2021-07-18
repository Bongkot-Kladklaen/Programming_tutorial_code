import numpy as np

#? ค้นหาข้อมุลในอาร์เรย์ where() จะคืนค่าเป็นตำแหน่งที่ข้อมูลอยู่เป็น index
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#? ค้นหาแบบจัดเรียง จะค้นหาว่าตัวเลขควรอยุ่ในตำแหน่งไหน
arr = np.array([5,6, 8, 9,10])
x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)