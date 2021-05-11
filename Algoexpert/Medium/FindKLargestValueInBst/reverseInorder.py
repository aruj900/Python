class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self,visited,value):
		self.visited = visited
		self.value = value
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    treeInfo = TreeInfo(0,-1)
    reverseInorder(tree,k,treeInfo)
    return treeInfo.value

def reverseInorder(node,k,treeInfo):
	if node is None or treeInfo.visited >= k:
		return
	
	reverseInorder(node.right,k,treeInfo)
	if treeInfo.visited < k:
		treeInfo.visited += 1
		treeInfo.value = node.value
		reverseInorder(node.left,k,treeInfo)
	
