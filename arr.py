import numpy as np

arr=np.array([[3,2,1],[6,5,4],[9,8,7]])

sorted_array=np.sort(arr , axis=None).reshape(arr.shape)
print(sorted_array)