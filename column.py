import numpy as np

arr = np.array([[3, 2, 1], [9, 7, 8], [6, 5, 4]])
sorted_cols = np.sort(arr, axis=0)

print(sorted_cols)
