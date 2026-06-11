# Build below location tree using TreeNode class



# Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() <= level: # check if the current node's level is less than or equal to the input level #example: if the input level is 2, then only print nodes that are at level 0, 1, and 2. Nodes at level 3 or higher should not be printed
            # if it is, print the node's data with appropriate indentation #Example: if the node is at level 2, it should be indented with 6 spaces (3 spaces for each level)
            spaces = ' ' * self.get_level() * 3
            prefixes = spaces + "|--" if self.parent else ""
            print(prefixes + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(level)
                
def build_location_tree():
    root = TreeNode("Global")
    
    india = TreeNode("India")
    Gujarat = TreeNode("Gujarat")
    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bangalore"))
    Karnataka.add_child(TreeNode("Mysore"))
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))
    india.add_child(Gujarat)
    india.add_child(Karnataka)
    
    usa = TreeNode("USA")
    New_Jersey = TreeNode("New Jersey")
    California = TreeNode("California")
    New_Jersey.add_child(TreeNode("Princeton"))
    New_Jersey.add_child(TreeNode("Trenton"))
    California.add_child(TreeNode("San Francisco"))
    California.add_child(TreeNode("Mountain View"))
    California.add_child(TreeNode("Palo Alto"))
    
    usa.add_child(New_Jersey)
    usa.add_child(California)
   
    
    root.add_child(india)
    root.add_child(usa)
    
    return root

if __name__ == '__main__':
    root_node = build_location_tree()
    input_level = int(input("Enter tree level to print: "))
    root_node.print_tree(input_level)