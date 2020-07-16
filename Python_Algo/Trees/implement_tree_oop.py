class BinaryTree(object):
    
    def __init__(self,robj):
        self.key = robj
        self.leftchild = None
        self.rightchild = None
        
    def insertLeft(self,newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t
    
    def insertRight(self,newNode):
        if self.insertRight == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getRightChild(self):
        return self.rightchild
    
    def getLeftChild(self):
        return self.leftchild
    
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
r = BinaryTree('a')

a = r.getRootVal()
print(a)

r.insertLeft('b')

b = r.getLeftChild().getRootVal()

print(b)