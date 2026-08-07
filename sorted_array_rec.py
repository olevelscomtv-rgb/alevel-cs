arr = [3,10,99,10]

def loop_sort_check(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else: 
            return False
    return True

print(loop_sort_check(arr))
