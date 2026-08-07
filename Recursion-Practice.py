maximum = -10000

def find_max(array, i =0):
    global maximum
    if i >= len(array):
        return maximum

    if array[i] > maximum:
        maximum = array[i]

    return find_max(array, i + 1)



arr = [2, 4, 1, 9, 20, 3, 21, 4]
print(find_max(arr))
