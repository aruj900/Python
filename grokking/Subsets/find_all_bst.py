from turtle import left, right


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = left
        self.right = right

def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_rec(1,n)

def find_unique_trees_rec(start,end):
    result = []
    if start > end:
        result.append(None)
        return result
    for i in range(start,end+1):
        left_sub = find_unique_trees_rec(start,i - 1)
        right_sub = find_unique_trees_rec(i+1,end)
        for left_tree in left_sub:
            for right_tree in right_sub:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result

def main():
  print("Total trees: " + str(find_unique_trees(2)))
  print("Total trees: " + str(find_unique_trees(3)))


main()
    