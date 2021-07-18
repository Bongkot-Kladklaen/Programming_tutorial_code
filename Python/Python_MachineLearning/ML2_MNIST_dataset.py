import matplotlip.pyplot as plt
from sklearn import datasets

#! MNIST Dataset ชุดข้อมูลตัวเลขอาราบิค

digit_dataset = datasets.load_digits()

# print(digit_dataset.keys())
# print(digit_dataset['images'])
# print(digit_dataset.target_names)
# print(digit_dataset.images[0])
# print(digit_dataset.images[0].shape)
print(digit_dataset.target[2])

#! แสดงแบบรูปภาพ
plt.imshow(digit_dataset.images[2], cmap=plt.get_cmap('gray'))
plt.show()