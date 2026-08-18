def sumDigits(n, total =0):

    if n <= 0:
        return total
    
    total += n % 10
    return sumDigits(n//10, total)
