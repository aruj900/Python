from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        levelsize = len(queue)
        current_level = []
        for _ in range(levelsize):
            current_Node = queue.popleft()
            current_level.append(current_Node.val)
            if current_Node.left:
                queue.append(current_Node.left)
            if current_Node.right:
                queue.append(current_Node.right)
        result.append(current_level)
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)l
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()