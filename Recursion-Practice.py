def find_max(array, i):
    maximum = -10000
    if i >= len(array):
        return maximum
    
    find_max(array, i + 1)
    print(maximum)

    if array[i] > maximum:
        maximum = array[i]


array = [2, 4, 1, 9, 0]
print(find_max(array, 0))
