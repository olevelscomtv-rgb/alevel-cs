# # Count the number of digits in a number using recursion
# # counting digits using loops

# number = 13080876
# count = 0
# while number > 0:
#     count += 1 
#     new = number % 10
#     number = number // 10 
#     print(new)


# print(f"The number of digits are {count}")


# counting using recursion method

def counting(number, count=0):

    if number <= 0 :
        return count
    #new = number % 10
    #Sir this line ^ has no effect on the code

    return counting(number//10,  count + 1)

print(counting(803199))

# My ITERVATIVE METHOD
num = 1234567890
count1 = 0
while num > 0:
  num = num // 10
  count1 += 1
print(count1)