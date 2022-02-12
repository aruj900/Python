def find_subsets(nums):
    subset = []
    subset.append([])
    for current_number in nums:
        n = len(subset)
        for i in range(n):
            set1 = list(subset[i])
            set1.append(current_number)
            subset.append(set1)
    return subset

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
