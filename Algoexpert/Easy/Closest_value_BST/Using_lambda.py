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

def findClosestValueBst(root,target):
    closest = root.data
    while root:
        closest = min(root.data,closest,key= lambda x:
            abs(target - x))
        root = root.left if target < root.data else root.right
    return closest

root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)  


print(findClosestValueBst(root,32))