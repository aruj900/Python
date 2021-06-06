class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_paths(root, S):
    return count_paths_helper(root,S,[])

def count_paths_helper(current, S, current_path):
    if current is None:
        return 0
    current_path.append(current.val)
    path_count, path_sum = 0,0
    
    for i in range(len(current_path)-1,-1,-1):
        path_sum += current_path[i]
        
        if path_sum == S:
            path_count += 1
    
    path_count += count_paths_helper(current.left,S,current_path)
    path_count += count_paths_helper(current.right,S,current_path)
    
    del current_path[-1]
    return path_count

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
