array = [51, 69, 24, 11, 1, 69, 51]

#length of the array
n = len(array)

for i in range(n-1):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            print(array)