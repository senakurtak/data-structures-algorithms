from data_structure import *

my_tree = BinaryTree()

my_tree.root = Node("D")
my_tree.root.left = Node("B")
my_tree.root.left.left = Node("A")
my_tree.root.left.right = Node("C")
temp = Node("E")
temp.left = Node("F")
temp.right = Node("G")
my_tree.root.right = temp

my_tree.preorder()
my_tree.inorder()
my_tree.postorder()

None