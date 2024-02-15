
class Node:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
        self.next = None
    
class LinkedList:
    def __init__(self) -> Node:
        self.head = Node
    def add(self, name, number):
        newnode = Node(name, number)
        if (not self.head):
            self.head = newnode
        else:
            if (newnode.name<self.head.name):
                newnode.next = self.head
                self.head = newnode
            else:
                traverser = self.head
                while(not traverser.next):
                    if (newnode.name < traverser.next.name):
                        newnode.next = traverser.next
                        traverser.next = newnode
                        break
                if (not traverser.next):
                    traverser.next = newnode

    def size(self) -> int:
        traverser = self.head
        counter = 0
        while(traverser):
            counter+=1
            traverser=traverser.next
        return counter
    
    def print(self):
        traverser = self.head
        while(traverser):
            print(traverser.name, traverser.number)
            traverser = traverser.next
        return