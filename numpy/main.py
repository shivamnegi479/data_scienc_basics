import numpy as np

# firsr_array=np.array([1,2,3,4,56])
# print(firsr_array)

# zero_array=np.zeros(shape=(2,4),dtype='int64')
# print(zero_array)

# one_array=np.ones(shape=(3,3),dtype=int)
# print(one_array)

# empty_array=np.empty(shape=(2,3),dtype=int)
# print(empty_array)


arrange_array=np.arange(12)
# print(arrange_array)

# zz=arrange_array.reshape(3,4)
# print(zz)

# linespace_arrat=np.linspace(1,5,5)
# print(linespace_arrat)

# arr=np.array([[1,2,3,4,5],[2,35,67,989,86]])
# x=arr.view()
# arr[0,0]=242
# print(x)

# for x in np.nditer(arr):
#     print(x)

# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,9])
# arr1=np.arange(120123129)
# arr3=np.concatenate((arr1,arr2))
# arr3=np.stack((arr2,arr1))
# arr3=np.hstack((arr2,arr1))
# arr3=np.vstack((arr2,arr1))
# print(arr3)

# x=np.where(arr1==2433)
# print(x)

x=np.arange(8).reshape(2,2,2)
print(x)