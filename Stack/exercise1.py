# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def push(self, item):
        self.stack.append(item) # Appends an item to the right end of the deque, which represents the top of the stack. 
        
    def pop(self):  
        if not self.is_empty():
            return self.stack.pop() # Removes and returns the item from the right end of the deque, which represents the top of the stack. 
        raise IndexError("Stack is empty")              
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1] # Returns the item at the right end of the deque without removing it, which represents the top of the stack. 
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0 # Checks if the stack is empty by checking if the length of the deque is zero.
    
def reverse_string(s):
    stack = Stack() # Create an instance of the Stack class to use for reversing the string.
    
    for char in s: # Iterate through each character in the input string.
        stack.push(char) # Push each character onto the stack.
    
    reversed_str = '' # Initialize an empty string to hold the reversed characters.
    
    while not stack.is_empty(): # Continue popping characters from the stack until it is empty.
        reversed_str += stack.pop() # Pop a character from the stack and append it to the reversed string.
    
    return reversed_str # Return the fully reversed string.

# Example usage:
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: "91-DIVOC ereuqnoc lliw eW"

