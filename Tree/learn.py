class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
        
def build_product_tree():
    root = TreeNode("Electronics")
    
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
    root.add_child(cellphone)
    root.add_child(TV)
    
    return root


    
    
        
        
    
        
    