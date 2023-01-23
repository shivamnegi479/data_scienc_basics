import numpy as np
from scipy.sparse import csc_matrix

arr=np.array([[0,1,0,1,0,1],[0,2,2,0,1,0]])
# csc_matrix(arr).eliminate_zeros()
# dup=csc_matrix(arr)
# dup.sum_duplicates()
# print(dup)
# print(len(arr[1])+len(arr[0]))
x=0
for i in np.nditer(arr):
    x=x+1
print(x)