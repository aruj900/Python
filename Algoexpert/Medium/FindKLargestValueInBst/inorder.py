def findKthLargestValueBst(tree,k):

    out = []
    inOrder(tree,out)
    return out(len(out) - k)

def inOrder(node,out):
    if node is None:
        return
    
    inOrder(node.left,out)
    out.append(node.value)
    inOrder(node.right,out)
    