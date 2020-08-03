class Node:
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
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
            

def isFullTree(root):
        
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if root.left is not None and root.right is not None:
            return (isFullTree(root.left) and isFullTree(root.right))
        
        return False
    
root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(3)
root.insert(42)



if isFullTree(root):
    print("This is full tree")
else:
    print("This is not full tree")