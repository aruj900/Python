class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    
    return find_path_helper(root,sequence,0)

def find_path_helper(current, seq, seq_idx):
    if current is None:
        return False
    
    seq_len = len(seq)
    if seq_idx >= seq_len or current.val != seq[seq_idx]:
        return False
    
    if current.left is None and current.right is None and seq_idx == seq_len - 1:
        return True
    
    return find_path_helper(current.left,seq,seq_idx+1) or find_path_helper(current.right,seq,seq_idx+1) 

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()