# 2 ^ 10 = 1024

# iterative method 

# def iter_base(base,power):
#     return base ** power

# print(iter_base(2,10))


# 2 ^ 10   2 * 2 * 2 * 2 ---------------

def rec_base(base,power,total = 1):
    
    total = total * base 
    print(power)
    if power <= 1: # 2048 1024 * 2
        return total 

    return (rec_base(base,power - 1, total))

print(rec_base(2,10))