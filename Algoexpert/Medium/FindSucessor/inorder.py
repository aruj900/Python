class BST:
    def __init__(self,value,left=None,right=None,parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def findSuccessor(tree,node):
    inOrder = getInorderTraversal(tree)
    for idx, val in enumerate(inOrder):
        if val != node:
            continue
        if idx == len(inOrder) - 1:
            return None
        return inOrder[idx + 1]


def getInorderTraversal(node,order=[]):
    if node is None:
        return order
    
    getInorderTraversal(node.left,order)
    order.append(node.value)
    getInorderTraversal(node.right,order)
    return order