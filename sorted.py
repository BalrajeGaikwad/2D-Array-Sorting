arr = [[3, 1, 2], [9, 7, 8], [6, 5, 4]]

sorted_arr = []  # Create an empty list to store sorted rows

for row in arr:
    sorted_arr.append(sorted(row))  # Sort each row and append to new list

print(sorted_arr)
