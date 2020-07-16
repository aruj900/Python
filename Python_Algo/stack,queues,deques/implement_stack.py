class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def peek(self):
        self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)
    

s = Stack()
print(s.isEmpty())

s.push(1)
s.push('two')
s.push(True)

print(s.size())

print(s.isEmpty())

s.pop()
s.pop()
s.pop()

print(s.isEmpty())

    