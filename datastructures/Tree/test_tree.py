import Tree

root = Tree.Node(1)
root.insert_left(2)
root.insert_right(3)
root.get_left().insert_left(4)
root.get_left().insert_right(5)

print('In order traversal')
Tree.inorder(root)
print('Post order traversal')
Tree.post_order(root)
print('Pre order traversal')
Tree.pre_order(root)