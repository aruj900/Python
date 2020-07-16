def nth_to_last_node(n,head):
    
   left = head
   right = head
   
   if not right.nextnode:
       print("It exceed the length og the list")
       
   for  i in  range(n-1):
       right.nextnode
   
   while right.nextnode:
       right = right.nextnode
       left = left.nextnode
   return left 
       
        
class Node(object):
    
    def __init__(self,value):
        self.value = value 
        self.nextnode = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d     
d.nextnode = e 

print(nth_to_last_node(2,a).value)


