# Binary Tree Part 2 Exercise
# Modify delete method in class BinarySearchTreeNode class to use min element from left subtree. You will remove lines marked with ---> and use max value from left subtree

#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.right

#           --->  min_val = self.right.find_min()
#           --->  self.data = min_val
#           --->  self.right = self.right.delete(min_val)

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal() # if the current node has a left child, then recursively call the post_order_traversal method on the left child and add the result to the list of elements #Example: if the current node has a left child with data 5, then call the post_order_traversal method on that child and add the result to the list of elements  
        if self.right:
            elements += self.right.post_order_traversal() # if the current node has a right child, then recursively call the post_order_traversal method on the right child and add the result to the list of elements #Example: if the current node has a right child with data 15, then call the post_order_traversal method on that child and add the result to the list of elements
        elements.append(self.data) # add the data of the current node to the list of elements #Example: if the current node has data 10, then add 10 to the list of elements
        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
        
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
        
    def delete_node(self, value):   
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete_node(max_value)
        return self
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("In order traversal gives sorted order of elements in the tree")
    print(numbers_tree.in_order_traversal())
    print("Pre order traversal gives the order in which the nodes are visited")
    print(numbers_tree.pre_order_traversal())
    print("Post order traversal gives the order in which the nodes are visited")
    print(numbers_tree.post_order_traversal())
    print("Search for 20 in the tree")
    print(numbers_tree.search(20))
    print("Search for 21 in the tree")
    print(numbers_tree.search(21))
    print("Minimum value in the tree")
    print(numbers_tree.find_min())
    print("Maximum value in the tree")
    print(numbers_tree.find_max())
    print("Delete 20 from the tree")
    numbers_tree.delete_node(20)
    print("In order traversal after deleting 20")
    print(numbers_tree.in_order_traversal())
    print("Delete 4 from the tree")
    numbers_tree.delete_node(4)
    print("In order traversal after deleting 4")
    print(numbers_tree.in_order_traversal())