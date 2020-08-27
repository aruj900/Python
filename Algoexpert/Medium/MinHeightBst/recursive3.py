def minHeightBst(array):
    return constructMinHeightBst(array,0,len(array)-1)

def constructMinHeightBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, bst, midIdx + 1, endIdx)
    return bst
    

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self,value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
    