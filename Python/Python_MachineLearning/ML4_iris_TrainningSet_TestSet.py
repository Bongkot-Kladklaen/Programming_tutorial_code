from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

"""
    Dataset
        - Trainning set model 75%
        - Test set            25%
"""

x_train, x_test = train_test_split(iris_dataset['data'],random_state=0)
y_train, y_test = train_test_split(iris_dataset['target'],random_state=0)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)