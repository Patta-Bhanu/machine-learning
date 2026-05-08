import numpy as np
arr=np.array([1,2,3,4],dtype='f',ndmin=1)
arr2=np.array([[1],[2],[3],[4]])
arr=arr.astype('i')
print(arr+arr2)
