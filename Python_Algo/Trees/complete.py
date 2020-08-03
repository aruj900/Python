class Node:
    def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
   
        
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))

def is_complete(root,index,numberNodes):
    
    if root is None:
        return True
    
    if index >= numberNodes:
        return False
    
    return (is_complete(root.left, 2*index + 1,numberNodes) and is_complete(root.right, 2*index + 2 ,numberNodes))

root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(3)
root.insert(42)



if is_complete(root,0,count_nodes(root)):
    print("This is complete tree")
else:
    print("This is not complete tree")
