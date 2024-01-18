class queue: # FIFO -> First in First Out
    def __init__(self):
        self.array = []
    def push(self, x):
        self.array.append(x)
    def pop(self):
        if not self.isEmpty():
            temp = self.array[0]
            del self.array[0]
            return temp
        else:
            return "NAN"
    def peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0
    def size(self):
        len(self.array)
        
    
class stack: # LIFO -> Last in First Out
    def __init__(self):
        self.array = []
    def push(self, x):
        self.array.append(x)
    def pop(self):
        if not self.isEmpty():
            temp = self.array[-1]
            del self.array[-1]
            return temp
        else: 
            return "NAN"
    def peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0
    def size(self):
        len(self.array)
        
        
my_structure = queue()
my_structure.push(1)
my_structure.push(2)
my_structure.push(3)

while not my_structure.isEmpty():
    print(my_structure.pop())


your_structure = stack()
your_structure.push(1)
your_structure.push(2)
your_structure.push(3)

while not your_structure.isEmpty():
    print(your_structure.pop())