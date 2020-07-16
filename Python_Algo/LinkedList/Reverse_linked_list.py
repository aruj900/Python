def reverse(head):
    
    current = head
    previous = None
    nextnode = None
    
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous

class Node(object):
    def __init__(self,value):
        self.value = value 
        self.nextnode = None
        
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a      

reverse(a)
print(b.nextnode.value)  