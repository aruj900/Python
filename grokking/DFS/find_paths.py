class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def find_paths(root,required_sum):
    all_paths = []
    find_paths_helper(root,required_sum,[],all_paths)
    return all_paths

def find_paths_helper(current,required_sum,current_path,all_paths):
    if current is None:
        return
    
    current_path.append(current.val)
    
    if current.val == required_sum and current.left is None and current.right is None:
        all_paths.append(list(current_path))
    else:
        find_paths_helper(current.left,required_sum-current.val,current_path,all_paths)
        find_paths_helper(current.right,required_sum-current.val,current_path,all_paths)
    
    del current_path[-1]
    
def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()
