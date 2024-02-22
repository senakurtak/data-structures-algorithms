class Node:
    #container ın yani datanın left right ı var. current.data nın yok
    def __init__(self, data) -> None: 
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None
    
    def add(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            self._add(self.root, newNode)  # Pass the root and new node
        
    def _add(self, current, newnode):  # Accept current and newnode parameters
        if newnode.data <= current.data:
            if current.left:
                self._add(current.left, newnode)  # Pass newnode when calling recursively
            else:
                current.left = newnode
        else:
            if current.right:
                self._add(current.right, newnode)  # Pass newnode when calling recursively
            else:
                current.right = newnode
    
    def search(self,data):
        self.counter = 0
        return self._search(self.root, data)
    
    def _search(self,current,data):
        self.counter += 1
        if not current:
            print("Not found", data, "in", self.counter, "comparisons")
            return None
        elif current.data == data:
            print("Found", data, "in", self.counter, "comparisons")
            return current.data, self.counter
        elif data < current.data:
            return self._search(current.left, data)
        else:
            return self._search(current.right, data)
'''
class BST:
    def __init__(self) -> None:
        self.root = None
    def add(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            self._add()
    def _add(self, current, newnode):
        if newnode.data <= current.data:
            if current.left:
                self._add(current.left)
            else:
                current.left = newnode
        else:
            if current.right:
                self._add(current.right, newnode)
            else:
                current.right = newnode
    
    def search(self,data):
        self.counter = 0
        return self._search(self.root, data)
    def _search(self,current,data):
        self.counter += 1
        if not current:
            print("Not found", data, "in", self.counter, "comparisons")
            return None
        elif current.data==data:
            print("Not found", data, "in", self.counter, "comparisons")
            return daya, self.counter
        elif data < current.data:
            return self._search(current.left, data)
        else:
            return self._search(current.right, data)
            '''