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
        elements= []
        # The in-order traversal of a binary search tree is a depth-first traversal that visits the left subtree, then the current node, and finally the right subtree. This means that the elements will be returned in sorted order.
        #visiting the left subtree first ensures that we get all the smaller elements before the current node, and visiting the right subtree last ensures that we get all the larger elements after the current node.
        if self.left:
            elements += self.left.in_order_traversal() # if the current node has a left child, then recursively call the in_order_traversal method on the left child and add the result to the list of elements #Example: if the current node has a left child with data 5, then call the in_order_traversal method on that child and add the result to the list of elements
        # After visiting the left subtree, we add the data of the current node to the list of elements. This ensures that the current node is visited after all the smaller elements in the left subtree have been visited.
        elements.append(self.data) # add the data of the current node to the list of elements #Example: if the current node has data 10, then add 10 to the list of elements
        # Finally, if the current node has a right child, we recursively call the in_order_traversal method on the right child and add the result to the list of elements. This ensures that all the larger elements in the right subtree are visited after the current node.
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        # The pre-order traversal of a binary search tree is a depth-first traversal that visits the current node first, then the left subtree, and finally the right subtree. This means that the elements will be returned in the order they were added to the tree.
        # visiting the current node first ensures that we get the elements in the order they were added to the tree, and visiting the left subtree before the right subtree ensures that we get all the elements in the left subtree before any elements in the right subtree.
        elements.append(self.data) # add the data of the current node to the list of elements #Example: if the current node has data 10, then add 10 to the list of elements
        if self.left:
            elements += self.left.pre_order_traversal() # if the current node has a left child, then recursively call the pre_order_traversal method on the left child and add the result to the list of elements #Example: if the current node has a left child with data 5, then call the pre_order_traversal method on that child and add the result to the list of elements
        if self.right:
            elements += self.right.pre_order_traversal() # if the current node has a right child, then recursively call the pre_order_traversal method on the right child and add the result to the list of elements #Example: if the current node has a right child with data 15, then call the pre_order_traversal method on that child and add the result to the list of elements
        return elements
    
    def post_order_traversal(self):
        elements = []
        # The post-order traversal of a binary search tree is a depth-first traversal that visits the left subtree, then the right subtree, and finally the current node. This means that the elements will be returned in the order they were removed from the tree.
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
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete_node(min_value)
        return self
    
        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
    
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34 , 18, 4]
    strings = ["India", "USA", "Germany", "China", "Japan", "Australia", "Brazil", "France", "Italy", "Spain"]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(2))
    # strings_tree = build_tree(strings)
    # print(strings_tree.in_order_traversal())
    # print(strings_tree.search("USA"))
    # print(strings_tree.search("Canada"))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    
    print(numbers_tree.delete_node(20))
    print(numbers_tree.in_order_traversal())
     