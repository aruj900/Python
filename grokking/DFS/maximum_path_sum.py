class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class MaximumPathSum:
    def find_maximum_path_sum(self,root):
        self.global_maxima = float("-inf")
        self.find_maximum_path_sum_helper(root)
        return self.global_maxima
    
    def find_maximum_path_sum_helper(self,current):
        if current is None:
            return 0
        maxPathLeft = self.find_maximum_path_sum_helper(current.left)
        maxPathRight = self.find_maximum_path_sum_helper(current.right)
        
        maxPathLeft = max(maxPathLeft,0)
        maxPathRight = max(maxPathRight,0)
        
        localMaximum = maxPathLeft + maxPathRight + current.val
        
        self.global_maxima = max(self.global_maxima,localMaximum)
        
        return max(maxPathRight,maxPathLeft) + current.val

def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()