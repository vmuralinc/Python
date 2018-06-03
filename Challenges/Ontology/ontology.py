#!/usr/bin/python3
ontology = {}


def convert_string_to_tree(tree_string):
    """creates a dictionary to represent the tree from a linear string 
       representation, the parent is the key and the value contains the list 
       of children. nodes with no children do not have an entry
    
    Keyword arguments:
    tree_string -- string representation of a tree
    
    Returns:
    dictionary of topics
    """    
    tree_elem_list = tree_string.split(" ")
    i = 1
    heirarchy = []
    prev = tree_elem_list[0]
    while i < len(tree_elem_list):
        if (tree_elem_list[i] == "("):
            heirarchy.append(tree_elem_list[i-1])
            ontology[heirarchy[-1]] = []
        elif (tree_elem_list[i] == ")"):
            heirarchy.pop()
        else:
            ontology[heirarchy[-1]].append(tree_elem_list[i])
        i += 1


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


descendants_list = []      
def get_descendant_list(q_key):
    """Returns a list of topics that are descendants of a particular topic
    
    Keyword arguments:
    ontology -- the dictionary containing the parent and children
    q_key -- the name of the node whose descendants have to be listed
    """
    descendants_list.append(q_key)
    for topic in ontology.get(q_key, []):
        get_descendant_list(topic)
        
        
        
def query(q_string):
    """Returns the number of questions that match the input topic and question 
    among the descendant topics of the topic given in the input
       
    Keyword arguments:
    ontology -- the dictionary containing the parent and children
    q_string -- the string containing topic and question
    """
    [q_key, q_val] = q_string.split(" ", 1)
    count = 0
    global descendants_list
    descendants_list = []
    get_descendant_list(q_key)
    #print(descendants_list)
    for key in descendants_list:
        #print(key)
        for string in questions.get(key, []):
            if string.startswith(q_val):
                count += 1
    return count
       
       
if __name__ == '__main__':
    """main function used to get the input and perform the operations"""
    nodes = int(input())
    convert_string_to_tree(input().strip())
    #print_tree(ontology)
    questions = {}
    for i in range(int(input())):
        add_questions(questions, input().strip())
    #print(questions)
    for i in range(int(input())):
        print(query(input().strip()))