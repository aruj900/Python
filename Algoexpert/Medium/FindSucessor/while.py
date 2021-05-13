class BST:
    def __init__(self,value,left=None,right=None,parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def findSuccessor(tree,node):
    if node.right is not None:
        return getLeftMost(node.right)
    return getRightParent(node)


def getLeftMost(node):
    while node.left is not None:
        node = node.left
    return node

def getRightParent(node):
    while node.parent is not None and node.parent.right == node:
        node = node.parent
    return node