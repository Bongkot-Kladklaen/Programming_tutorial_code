import numpy as np 
from scipy.sparse import csr_matrix 

arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))
print(csr_matrix(arr).data)
print(csr_matrix(arr).count_nonzero())

arr2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr2)
# mat.eliminate_zeros()
mat.sum_duplicates()
print(mat)