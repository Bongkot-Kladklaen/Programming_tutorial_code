from sklearn import datasets

#! Iris Dataset ชุดข้อมูลดอกกล้วยไม้
iris_dataset = datasets.load_iris()

# print(iris_dataset.keys())
# print(iris_dataset['frame'])
# print(iris_dataset['DESCR'])
# print(iris_dataset['filename'])
print(iris_dataset['data'][0:10])
print(iris_dataset['target'])
print(iris_dataset['target_names'])
print(iris_dataset['feature_names'])