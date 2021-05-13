class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrder):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"),float("inf"),preOrder,treeInfo)

def reconstructBstFromRange(low,high,preOrder,current):
    if current.rootIdx == len(preOrder):
        return None
    rootValue = preOrder[current.rootIdx]

    if rootValue <= low or rootValue >= high:
        return None
    
    current.rootIdx += 1
    leftSubTree = reconstructBstFromRange(low,rootValue,preOrder,current)
    rightSubTree = reconstructBstFromRange(rootValue,high,preOrder,current)
    return BST(rootValue,leftSubTree,rightSubTree)