import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("ก่อนเปลี่ยนแปลง : ",arr)

#? การปรับเปลี่ยนรูปร่างของอาร์เรย์
newarr = arr.reshape(4,3)           #! แปลงอาร์เรย์ 1 มิติ เป็นหลายมิติ
print("หลังเปลี่ยนแปล : ",newarr)

newarr = arr.reshape(2,3,2)          #! แปลงอาร์เรย์ 1 มิติ เป็นหลายมิติ
print("หลังเปลี่ยนแปล : ",newarr)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr2.reshape(-1)          #! แปลงอาร์เรย์์หลายมิติ เป็น 1 มิติ
print("ก่อนเปลี่ยนแปลง : ",arr2)
print('แปลงจากหลายมิติให้เป็น 1 มิติ : ',newarr)

