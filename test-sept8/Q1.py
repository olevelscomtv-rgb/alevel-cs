DataStored = [] * 20
NumberItems = 0

def Initialize():
    global DataStored, NumberItems 
    Quantity = int(input("Enter the number of items to store (max 20): "))
    if Quantity > 20 or Quantity < 1:
        print("Invalid quantity. Please enter a number between 1 and 20.")
        return
    for i in range(1, Quantity + 1):
        item = input(f"Enter item {i}: ")
        DataStored.append(item)
        NumberItems += 1

def BubbleSort():
    global DataStored, NumberItems
    for i in range(NumberItems - 1):
        for j in range(0, NumberItems - i - 1):
            if DataStored[j] > DataStored[j + 1]:
                DataStored[j], DataStored[j + 1] = (
                    DataStored[j + 1],
                    DataStored[j],
                )

def BinarySearch(DataToFind):
    global DataStored, NumberItems
    left = 0
    right = NumberItems - 1
    while left <= right:
        mid = (left + right) // 2
        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] < DataToFind:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def Main():
    Initialize()

    DataToFind = input("Enter the item to search for: ")
    index = BinarySearch(DataToFind)
    if index != -1: 
        print(f"Item '{DataToFind}': Index {index}")
    else:
        print(f"Item '{DataToFind}' not found.")
    print("")

    print("Items stored:", DataStored)
    BubbleSort()
    print("Items after sorting:", DataStored)
    print("Total number of items:", NumberItems)

Main()