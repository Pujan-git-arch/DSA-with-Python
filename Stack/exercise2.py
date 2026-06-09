# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


# Using LIst and String methods to solve the problem of checking for balanced parentheses is a common approach. Below is a Python function that implements this logic using a stack data structure:

# from collections import deque
# class Stack:
#     def __init__(self):
#         self.stack = deque()
        
#     def push(self, item):
#         self.stack.append(item) # Appends an item to the right end of the deque, which represents the top of the stack. 
        
#     def pop(self):  
#         if not self.is_empty():
#             return self.stack.pop() # Removes and returns the item from the right end of the deque, which represents the top of the stack. 
#         raise IndexError("Stack is empty")              
    
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1] # Returns the item at the right end of the deque without removing it, which represents the top of the stack. 
#         raise IndexError("Stack is empty")
    
#     def is_empty(self):
#         return len(self.stack) == 0 # Checks if the stack is empty by checking if the length of the deque is zero.
    
# def is_balanced(s):
#     stack = Stack()
#     opening = "({["
#     closing = ")}]" 
#     for char in s:
#         if char in opening:
#             stack.push(char) # If the character is an opening parenthesis, push it onto the stack.
#         elif char in closing:
#             if stack.is_empty():
#                 return False # If the stack is empty when we encounter a closing parenthesis, it means there is no corresponding opening parenthesis, so we return False.
#             top = stack.pop() # Pop the top element from the stack to check if it matches the current closing parenthesis.
#             if opening.index(top) != closing.index(char):
#                 return False # If the indices of the opening and closing parentheses do not match, it means they are not balanced, so we return False.
#     return stack.is_empty() # If the stack is empty at the end, it means all parentheses are balanced, so we return True.   

# # Example usage:
# input_string = input("Enter a string to check for balanced parentheses: ")
# if is_balanced(input_string):
#     print("The parentheses in the string are balanced.")
# else:
#     print("The parentheses in the string are not balanced.")


from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        return None

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_match(opening, closing):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return pairs[opening] == closing


def is_balanced(s):
    stack = Stack()

    for ch in s:
        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":
            if stack.is_empty():
                return False

            if not is_match(stack.pop(), ch):
                return False

    return stack.is_empty()


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))