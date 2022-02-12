def count_trees(n):
    return count_trees_rec({},n)

def count_trees_rec(map,n):
    if n in map:
        return map[n]
    if n <= 1:
        return 1
    count = 0
    for i in range(1,n+1):
        count_left = count_trees_rec(map,i-1)
        count_right = count_trees_rec(map, n - i)
        count += (count_left*count_right)
        
    return count
def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()
        