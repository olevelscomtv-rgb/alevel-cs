import random
Stack = []
for i in range(30):
    Stack.append(0)

TopOfStack = -1

def Push(num):
    global TopOfStack, Stack
    if TopOfStack > 29:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = num
        return True

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return -999
    else:
        num = Stack[TopOfStack]
        TopOfStack -= 1
        return num


for x in range(40):
    Pushed = Push(random.randint(0,1000))
    if Pushed == False:
        print("Stack full")
        break


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
