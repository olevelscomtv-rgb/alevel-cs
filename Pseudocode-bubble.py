def bubble_sort(the_array):

    n = len(the_array)

    for x in range(n):

        for y in range(0, n - x - 1):
            
            if the_array[y] > the_array[y + 1]:
                temp = the_array[y]
                the_array[y] = the_array[y + 1]
                the_array[y + 1] = temp
