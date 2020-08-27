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
                    self.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.insert(data)
        else:
            self.data = data



def trimbst(tree,minVal,maxVal):
    
    if not tree:
        return
    
    tree.left = trimbst(tree.left,minVal,maxVal)
    tree.right = trimbst(tree.right,minVal,maxVal)
    
    if minVal <= tree.val <= maxVal:
        return tree
    
    if tree.val < minVal:
        return tree.right
    
    if tree.val > maxVal:
        return tree.left
    

    
    
   
    
                    