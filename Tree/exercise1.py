# Data structures exercise: General Tree
# Below is the management hierarchy of a company.

# ss

# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,



# Here is how your main function should will look like,

# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy

class TreeNode:
    def __init__(self, data):
        self.data = data  # data is a dict with 'name' and 'designation'
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
    
    def print_tree(self, tree_type):
        spaces = ' ' * self.get_level( ) *3
        prefixes = spaces + "|--" if self.parent else ""
        if tree_type == "name":
            print(prefixes + self.data['name'])
        elif tree_type == "designation":
            print(prefixes + self.data['designation'])
        elif tree_type == "both":
            print(prefixes + self.data['name'] + " (" + self.data['designation'] + ")")
        else:
            print("Invalid tree type. Please choose 'name', 'designation', or 'both'.")
            
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(tree_type) 
                
def build_management_tree():
    root = TreeNode({"name": "Nilupul", "designation": "CEO"})

    cto = TreeNode({"name": "Chinmay", "designation": "CTO"})
    hr_head = TreeNode({"name": "Gels", "designation": "HR Head"})
    infra_head = TreeNode({"name": "Vishwa", "designation": "Infrastructure Head"})
    Application_head = TreeNode({"name": "Aamir", "designation": "Application Head"})

    cto.add_child(infra_head)
    cto.add_child(Application_head)
    
    
    infra_head.add_child(TreeNode({"name": "Dhaval", "designation": "Cloud Manager"}))
    infra_head.add_child(TreeNode({"name": "Abhijit", "designation": "App Manager"}))
    
    hr_head.add_child(TreeNode({"name": "Peter", "designation": "Recruitment Manager"}))
    hr_head.add_child(TreeNode({"name": "Waqas", "designation": "Policy Manager"}))

    root.add_child(cto)
    root.add_child(hr_head)

    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    input_type = input("Enter tree type to print (name/designation/both): ")
    if input_type in ["name", "designation", "both"]:
        root_node.print_tree(input_type)
    else:
        print("Invalid input. Please enter 'name', 'designation', or 'both'.")  
        