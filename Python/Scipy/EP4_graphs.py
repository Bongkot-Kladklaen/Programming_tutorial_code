import numpy as np 
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr)
print(connected_components(newarr))
print(dijkstra(newarr, return_predecessors=True, indices=0))
print(floyd_warshall(newarr, return_predecessors=True))

bellman = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
arrbellman = csr_matrix(bellman)
print(bellman_ford(arrbellman, return_predecessors=True, indices=0))

depthFirstOrder = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
arrdefthfirstorder = csr_matrix(depthFirstOrder)
print(depth_first_order(arrdefthfirstorder, 1))

arrBreadthFirstOrder = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
arrbreadthfirstorder = csr_matrix(arrBreadthFirstOrder)
print(breadth_first_order(arrbreadthfirstorder, 1))