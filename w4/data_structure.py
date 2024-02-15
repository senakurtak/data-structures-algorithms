class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class Node2:
    def __init__(self, x) -> None:
        self.data = x
        self.children = [] 
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def preorder(self): #start
        self._preorder(self.root)
        print("")
        
    def inorder(self): #start
        self._inorder(self.root)
        print("") 
                  
    def postorder(self): #start
        self._postorder(self.root)
        print("")
               
    def _preorder(self, node): #recursive
        if node:
            print(node.data, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
            
    def _inorder(self, node): #recursive
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)
            
    def _postorder(self, node): #recursive
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=" ")