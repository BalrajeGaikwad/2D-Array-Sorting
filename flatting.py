import numpy as np

arr1 = np.array([[3, 2], [1, 6], [5, 4]])
arr2 = np.array([[9, 7], [8, 5], [2, 1]])

flat1=arr1.flatten()
flat2=arr2.flatten()


merged=np.concatenate((flat1,flat2))
sorted=np.sort(merged)

print(merged)
print(sorted)

unique=np.sort(np.unique(sorted))
print("unique array is follows")
print(unique)
unique = np.append(unique, 0)
new_array=unique.reshape(-1,2)
print("new array")
print(new_array)



"""

# Add a padding element to make the total number of elements divisible by 2
unique = np.append(unique, 0)

new_array = unique.reshape(-1, 2)
print("Reshaped Array with Padding:")
print(new_array)"""
