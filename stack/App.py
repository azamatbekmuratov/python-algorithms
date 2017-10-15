from stack.Stack import Stack

stack = Stack()
stack.push(4)
stack.push('dog')
print(stack.peek())
stack.push(True)
print(stack.size())
print(stack.isEmpty())
