#!/usr/bin/python3

def convert_string_to_tree(tree_string):
    """creates a dictionary to represent the tree from a linear string 
       representation, the parent is the key and the value contains the list 
       of children. nodes with no children do not have an entry
    
    Keyword arguments:
    tree_string -- string representation of a tree
    
    Returns:
    dictionary of topics
    """
    ontology = {}
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
    return ontology


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

                
def get_descendant_list(ontology, q_key):
    """Returns a list of topics that are descendants of a particular topic
    
    Keyword arguments:
    ontology -- the dictionary containing the parent and children
    q_key -- the name of the node for which the the descendants have to be listed
    """
    if not ontology.get(q_key, None):
        return [q_key]
    else:
        data_list = [q_key]
        for child in ontology[q_key]:
            data_list += get_descendant_list(ontology, child)
        return data_list
        
        
def query(ontology, q_string):
    """Returns the number of questions that match the input topic and question 
    among the descendant topics of the topic given in the input
       
    Keyword arguments:
    ontology -- the dictionary containing the parent and children
    q_string -- the string containing topic and question
    """
    [q_key, q_val] = q_string.split(" ", 1)
    count = 0
    keys_list = get_descendant_list(ontology, q_key) 
    #print(keys_list)
    for key in keys_list:
        for string in questions.get(key, []):
            if string.startswith(q_val):
                count += 1
    return count
       
       
if __name__ == '__main__':
    """main function used to get the input and perform the operations"""
    nodes = int(input())
    ontology = convert_string_to_tree(input().strip())
    #print_tree(ontology)
    questions = {}
    for i in range(int(input())):
        add_questions(questions, input().strip())
    #print(questions)
    for i in range(int(input())):
        print(query(ontology, input().strip()))