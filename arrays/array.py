my_array = [1, 2, 3, 4, 5]

print(my_array[0])  # 1
print(my_array[1])  # 2

#lowest value in an array

'''Go through the values in the array one by one.
Check if the current value is the lowest so far, and if it is, store it.
After looking at all the values, the stored value will be the lowest of all values in the array.'''

array = [1, 2, 3, 4, 5, 0]

min_value = array[0]

for i in array:
    if i < min_value:
        min_value = i

print(f"lowest value is: {min_value}")