class Node:
    left = None
    value = None
    right = None
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert_left(self, left):
        if(self.left == None):
            self.left = Node(left)
        else:
            return None
        
    def insert_right(self, right):
        if(self.right == None):
            self.right = Node(right)
        else:
            return None
        
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
        
def inorder(root):
    if(root.left):
        inorder(root.left)
    print(root.value)
    if(root.right):
        inorder(root.right)

def post_order(root):
    if(root.left):
        post_order(root.left)
    if(root.right):
        post_order(root.right)
    print(root.value)
    
def pre_order(root):
    print(root.value)
    if(root.left):
        pre_order(root.left)
    if(root.right):
        pre_order(root.right)