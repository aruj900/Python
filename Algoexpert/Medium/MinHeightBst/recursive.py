def minHeightBst(array):
    return constructMinHeightBst(array,None,0,len(array)-1)

def constructMinHeightBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return 
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)
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
    