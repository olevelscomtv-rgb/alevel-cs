arr = [3,10,99,10]

def loop_sort_check(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else: 
            return False
    return True

print(loop_sort_check(arr))

#RECURSIVE FUNCTION

def sort_check(array, count=0):
    if count >= len(array)-1:
        return True
    
    
    if array[count] > array[count + 1]:
        return False

    return sort_check(array, count + 1)

arr1 = [3, 10, 90, 10, 4, 50]
print(sort_check(arr1))