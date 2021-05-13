class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrder):
    if len(preOrder) == 0:
        return None
    
    current = preOrder[0]
    rightIdx = len(preOrder)

    for idx,value in enumerate(preOrder):
        if value > current:
            rightIdx = idx
            break
    
    leftSubTree = reconstructBst(preOrder[1:rightIdx])
    rightSubTree = reconstructBst(preOrder[rightIdx:])
    return BST(current,leftSubTree,rightSubTree)