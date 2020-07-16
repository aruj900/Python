class Node:
    
    def __init__(self,data):
        
        self.left = None
        self.right = None
        self.data = data
    
    #Insert data
    
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
    
    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res        
    
root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)    





import collections

#nodes = collections.deque([root])
#c = nodes.popleft()
#print(c.data) 

def levelOrderPrint(tree):
    
   if not tree:
       return
   
   nodes = collections.deque([tree])
   #print(len(nodes))
   
   currentCount = 1
   nextcount = 0
   
   while len(nodes) != 0:
       currentNode = nodes.popleft()
       currentCount -= 1
       
       print(currentNode.data,end = " ")
       
       if currentNode.left:
           nodes.append(currentNode.left)
           nextcount +=1
        
       if currentNode.right:
           nodes.append(currentNode.right)
           nextcount +=1
       
       if currentCount == 0:
           print('\n')
           currentCount,nextcount = nextcount,currentCount


print(levelOrderPrint(root))
        
       
    