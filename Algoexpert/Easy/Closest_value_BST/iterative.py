def findClosestValueBst(tree,target):
    return findClosestValueBstHelper(tree,target,float("inf"))

def findClosestValueBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        
        if (abs(target - closest) > abs(target - currentNode.value)):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        
        elif target > currentNode.value:
            currentNode = currentNode.right
        
        else:
            break
    return closest


        