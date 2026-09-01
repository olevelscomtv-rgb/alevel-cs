def IterativeCalculate(Number):
    Total = 0
    ToFind = Number
    while Number > 0:
        if ToFind % Number == 0:
            Total += Number

        Number -= 1
    return Total

x = IterativeCalculate(10)
print(x)

def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    if ToFind % Number == 0:
        return Number + RecursiveValue(Number - 1, ToFind)
    else:
        return RecursiveValue(Number - 1, ToFind)
y = RecursiveValue(50, 50)
print(y)