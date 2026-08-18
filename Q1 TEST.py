def binary_search(arr, val):
    l = 0
    r = len(arr)-1

    while r >= l:
        mid = (r+l)//2

        if arr[mid] == val:
            return mid
    
        elif arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1

    return -1


arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x = binary_search(arr1, 4)
print(x)