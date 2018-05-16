class Node():
    """Contains one data and N children"""
    def __init__(self, data):
        """Initializes data and empty child list
        
        Keyword argument:
        data -- adds a data to the Node
        """
        self.data = data
        self.children = []
    
    def addChild(self, child):
        """Adds a child Node to the self Node
        
        Keyword arguments:
        child -- a Node object to be add as a child to self object
        """
        self.children.append(child)


def convert_string_to_tree(tree_string):
    """creates a tree from a linear string representation
    
    Keyword arguments:
    tree_string -- string representation of a tree
    
    Returns:
    Node object
    """
    tree_elem_list = tree_string.split(" ")
    root = Node(tree_elem_list[0])
    i = 1
    heirarchy = []
    node = root
    while i < len(tree_elem_list):
        if (tree_elem_list[i] == "("):
            heirarchy.append(node)
        elif (tree_elem_list[i] == ")"):
            heirarchy.pop()
        else:
            node = Node(tree_elem_list[i])
            heirarchy[-1].addChild(node)
        i += 1
    return root
    

def get_descendant_list(node, q_key, found_node = 0):
    """Returns a list of data of nodes that are descendants of a particular node
    
    Keyword arguments:
    node -- the root node of the tree that you are considering
    q_key -- the data that you want to match in your tree node and find descendants for
    """
    if node.children == []:
        if found_node == 1 or node.data == q_key:
            found_node = 1
            return [node.data]
        else:
            return []
    else:
        if found_node == 1 or node.data == q_key:
            found_node = 1
            data_list =  [node.data]
        else:
            data_list =  []
        for child in node.children:
            data_list += get_descendant_list(child, q_key, found_node)
        return data_list


def add_questions(questions, q_string):
    """Splits the topic names and the question being asked and the stores the question 
    matched with the topic as key
       
    Keyword arguments:
    questions -- hash into which the question has to be stored
    q_string -- the question to be added
    """
    [key, val] = q_string.split(": ")
    if questions.get(key, None):
        questions[key].append(val)
    else:
        questions[key] = [val]

    
def print_tree(node, prefix=""):
    """Navigate through the tree and print the data"""
    print(prefix + node.data)
    if node.children != []:
        prefix += "   "
        for child in node.children:
            print_tree(child, prefix)
            
            
                
def query(root, q_string):
    """Returns the number of questions that match the input topic and question 
    among the descendant topics of the topic given in the input
       
    Keyword arguments:
    root - root node of the topics tree
    """
    [q_key, q_val] = q_string.split(" ", 1)
    count = 0
    node = root
    keys_list = get_descendant_list(root, q_key) 
    #print(keys_list)
    for key in keys_list:
        for string in questions.get(key, []):
            if q_val in string:
                count += 1
    return count
       
       
if __name__ == '__main__':
    """main function used to get the input and perform the operations"""
    nodes = int(input())
    tree = convert_string_to_tree(input().strip())
    #print_tree(tree)
    questions = {}
    for i in range(int(input())):
        add_questions(questions, input().strip())
    #print(questions)
    for i in range(int(input())):
        print(query(tree, input().strip()))
    