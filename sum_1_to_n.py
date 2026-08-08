# sum all numbers from 1 to n 

#  iterative approach 

def sum_iteration(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total


# 1,2,3,4,5 -> 15 

# recursion approach 

def sum_rec(n, total = 0):
    if n < 1:
        return total
    total += n

    return sum_rec(n-1, total)                                # call stack 

print(sum_rec(10))



