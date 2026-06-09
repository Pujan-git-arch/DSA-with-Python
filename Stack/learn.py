from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty")
    
    def display(self):
        print("Stack elements:", list(self.stack))  # Output: Stack elements: [1, 2, 3] # list is used to convert the deque to a list for better visualization.

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("the top element is",s.peek())  # Output: 3

print("the size of the stack is",s.size(),"and the elements are",s.stack)  # Output: 3
print( "the element to be poped is",s.pop())   # Output: 3
print("the last element is",s.peek())  # Output: 2
print("the size of the stack is",s.size())  # Output: 2
print(" The elements of the stack are",s.stack)  # Output: deque([1, 2])

