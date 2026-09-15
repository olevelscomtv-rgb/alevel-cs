import random
Stack = []
for i in range(30):
    Stack.append(0)

TopOfStack = -1

def Push(num):
    global TopOfStack
    if TopOfStack == 29:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = num
        return True

def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return -999
    else:
        num = Stack[TopOfStack]
        TopOfStack -= 1
        return num

def Main():
    number = random.randint(1, 1000)
    for x in range(40):
        if Push(number) == False:
            return ("Stack full")
        else:
            Push(number)
        return
    
    FindValues()

def FindValues():
    global TopOfStack
    Max = -1
    Min = 10000
    for i in range(TopOfStack + 1):
        if Pop()[i] > Max:
            Max = Pop()[i]
        if Pop()[i] < Min:
            Min = Pop()[i]
    return Max, Min

print(Main())