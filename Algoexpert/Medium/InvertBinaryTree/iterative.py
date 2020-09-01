def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftandRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftandRight(tree):
    tree.left, tree.right = tree.right,tree.left
    
    
    