from DataStructures.stack.Stack import Stack


def divide_by2(decNumber):
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber //2

    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())

    return binString


print(divide_by2(42))

