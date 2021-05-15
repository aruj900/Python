def getPermutation(arr):
    subsets = [[]]
    for ele in arr:
        for i in range(len(subsets)):
            current = subsets[i]
            subsets.append(current+[ele])
    return subsets

print(getPermutation([1,2,3]))