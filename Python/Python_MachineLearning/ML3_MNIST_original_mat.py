from scipy.io import loadmat
import matplotlib.pyplot as plt

mnist_raw = loadmat('mnist-original.mat')

mnist = {
    'data':mnist_raw['data'].T,
    'target':mnist_raw['label'][0]
}
x, y = mnist['data'], mnist['target']

number = x[15000]
number_image = number.reshape(28,28)

print(y[15000])
plt.imshow(number_image, cmap=plt.cm.binary, interpolation='nearest')
plt.show()

print(x.shape)