def binary_search():

    num_elements = int(input("Enter number of elements: "))
    if num_elements <= 1:
        print("Search can not be performed.")
        return
    
    elements = input("Enter elements: ")
    arr = list(elements)

    element_find = int(input("Enter element to search: "))

    low = 0
    high = num_elements - 1
    comparisons = 0
    element_index = -1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == element_find:
            element_index = mid
            break
        elif arr[mid] < element_find:
            low = mid + 1
        else:
            high = mid - 1

    if element_index != -1:
        print("Element found!")
        print(f"Position: {element_index + 1}")
        print(f"Index: {element_index}")
        print(f"Comparisions: {comparisons}")
    else:
        print("Element not found")
        print(f"Comparisions: {comparisons}")

if __name__ == "__main__":
    binary_search()