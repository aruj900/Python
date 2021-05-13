class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,height,diameter):
        self.height = height
        self.diameter = diameter

def diameterBst(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)
    
    leftTreeData = getTreeInfo(tree.left)
    rightTreeData = getTreeInfo(tree.right)

    longestPathRoot = leftTreeData.height + rightTreeData.height
    maxDiameterSoFar = max(leftTreeData.diameter,rightTreeData.diameter)

    currentDiameter = max(longestPathRoot,maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeData.height,rightTreeData.height)

    return TreeInfo(currentDiameter,currentHeight)