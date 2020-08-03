class Node:
    
    def __init__(self,k):
        self.data = k
        self.right = self.left = None
    
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

def calculateDepth(node):
    d = 0
    while(node is not None):
        d += 1
        node = node.left
    return d

def is_perfect(root,d,level=0):
    
    if (root is None):
        return True
    
    if (root.left is None and root.right is None):
        return (d == level +1)
    
    if (root.left is None or root.right is None):
        return False
    
    return (is_perfect(root.left,d,level + 1) and is_perfect(root.right,d,level+1))
    

root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(3)
root.insert(42)

if (is_perfect(root,calculateDepth(root))):
    print("The tree is perfect binary tree")
else:
    print("The tree is not a perfect binary tree")