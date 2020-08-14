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
            

def branchSum(tree):
    sums = []
    calculateSum(tree,0,sums)
    return sums

def calculateSum(node,runningSum,sums):
    
    if node is None:
        return
    
    newRunningSum = runningSum + node.data
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    calculateSum(node.left,newRunningSum,sums)
    calculateSum(node.right,newRunningSum,sums)
    
root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)  

print(branchSum(root))