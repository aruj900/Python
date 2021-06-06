class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
        
class TreeDiameter:
    def __init__(self):
        self.diameter = 0
    
    def find_diameter(self,root):
        self.calculate_height(root)
        return self.diameter
    
    def calculate_height(self, current):
        if current is None:
            return 0
        
        leftTreeHeight = self.calculate_height(current.left)
        rightTreeHeight = self.calculate_height(current.right)
        
        if leftTreeHeight is not None and rightTreeHeight is not None:
            dia = leftTreeHeight + rightTreeHeight + 1
            self.diameter = max(self.diameter,dia)
            
        return max(leftTreeHeight,rightTreeHeight) + 1

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
