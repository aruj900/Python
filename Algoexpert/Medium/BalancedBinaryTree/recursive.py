class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height

def balanceBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node == None:
        return TreeInfo(True,-1)
    
    leftTreeInfo = getTreeInfo(node.left)
    rightTreeInfo = getTreeInfo(node.right)

    isBalanced = (leftTreeInfo.isBalanced and rightTreeInfo.isBalanced and abs(leftTreeInfo.height
    - rightTreeInfo.height <= 1))

    height = max(leftTreeInfo.height,rightTreeInfo.height) + 1
    return TreeInfo(isBalanced,height)



