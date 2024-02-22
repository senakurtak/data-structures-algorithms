from data_structure import Node, BST

values = [2,8,5,6,0,1,9,7,4,3]
my_tree = BST()

for v in values:
    my_tree.add(v)
    
my_tree.search(5)
my_tree.search(2)