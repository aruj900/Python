# Avg O(log(n)) ST and worst case is O(n) ST
class Node:
    
    def __init__(self,data):
        self.data = data
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



def findClosestvalueBST(root,target):
    return findClosestvalueBSTHelper(root,target,float("inf"))

def findClosestvalueBSTHelper(root,target,closest):
    if root is None:
        return closest
    
    if abs(target - closest) > abs(target - root.data):
        closest = root.data
    
    if target < root.data:
        return findClosestvalueBSTHelper(root.left,target,closest)
    
    elif target > root.data:
        return findClosestvalueBSTHelper(root.right,target,closest)
    
    else:
        return closest
    
root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)  


print(findClosestvalueBST(root,32))