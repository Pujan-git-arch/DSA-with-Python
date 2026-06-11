class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""  # root node has no prefix # if the node has a parent, add prefix # print the data of the node
        print(prefix +self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics") # root node of the tree # create a tree with the following structure: # Electronics # |__ Laptop # |__ Macbook # |__ Surface # |__ Thinkpad # |__ Cell Phone # |__ iPhone # |__ Google Pixel # |__ Vivo # |__ TV # |__ Samsung # |__ LG # |__ Sony
    
    Laptop = TreeNode("Laptop")
    Laptop.add_child(TreeNode("Macbook"))
    Laptop.add_child(TreeNode("Surface"))
    Laptop.add_child(TreeNode("Thinkpad")) 
    
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    
    TV = TreeNode("TV")
    TV.add_child(TreeNode("Samsung"))
    TV.add_child(TreeNode("LG"))
    TV.add_child(TreeNode("Sony"))
    
    
    
    root.add_child(Laptop)
    root.add_child(cellphone) # add the cell phone node as a child of the root node
    root.add_child(TV)
    
    return root
if __name__ == '__main__':
    root = build_product_tree() # build the product tree and store the root node in a variable called root  # print the tree structure starting from the root node
    root.print_tree()  # call the print_tree method on the root node to display the tree structure
    
    
    
        
        
    
        
    