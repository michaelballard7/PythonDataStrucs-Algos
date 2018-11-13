"""

A stack is a list of elements in which an element may be inserted or deleted only at one end

This mean elements are removed in reverse order than which they were inserted  

Last in First Out, First in Last out 

Remember the last element in a stack is the first element to be removed from the stack

Applications of stacks include: Parsing, Recursive Function, Calling Function, Expressive Evaluation, Expression Conversion, Towers of Hanoi

"""





class Stack:

    # this is the implementation of a stack data structure
    def __init__(self):
        self.stack = []

    # check to see is the stack is empty  
    def isEmpty(self):
        return self.stack == []

    # push additional data onto the stack
    def push(self, data):
        self.stack.append(data)

    # pop off the last value of the stack
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # check to see the last value on the stack without deleting it
    def peek(self):
        return self.stack[-1]

    # return the size of the stack itself
    def size(self):
        return len(self.stack)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("The stack has", stack.size(), "elements")
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print("Peek: ", stack.peek())
print("The new stack size is ", stack.size())