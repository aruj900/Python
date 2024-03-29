class Queue2Stacks(object):
    
    def __init__(self):
        self.instack = []
        self.outstack = []
        
    def enqueue(self,element):
        self.instack.append(element)
        pass
    
    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        pass
    
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())