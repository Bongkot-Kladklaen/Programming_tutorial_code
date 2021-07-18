import numpy as np 
from scipy.spatial import Delaunay, ConvexHull
import matplotlib.pyplot as plt 

arr_delaunay = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices = Delaunay(arr_delaunay).simplices
plt.triplot(arr_delaunay[:, 0], arr_delaunay[:, 1], simplices)
plt.scatter(arr_delaunay[:, 0], arr_delaunay[:, 1], color='r')
plt.show()