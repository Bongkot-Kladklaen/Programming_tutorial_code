import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#? for loop
for x in arr:
    for y in x:
        for z in y:
            print(z)

#? nditer() buil-in function for NumPy
for x in np.nditer(arr):
    print(x)

#? Loop แบบเปลี่ยนแปลงค่าจะ array หลัก
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#? การลูปแบบแจกแจงจะเอาตำแหน่ง index มาแสดงด้วย ndenumerate()
for idx, x in np.ndenumerate(arr):
  print(idx, x)