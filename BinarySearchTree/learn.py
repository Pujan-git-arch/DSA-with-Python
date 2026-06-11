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
    strings_tree = build_tree(strings)
    print(strings_tree.in_order_traversal())
    print(strings_tree.search("USA"))
    print(strings_tree.search("Canada"))