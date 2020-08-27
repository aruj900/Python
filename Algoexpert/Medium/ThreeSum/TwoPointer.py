def threeNumberSum(array,target):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == target:
                triplets.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
    return triplets

print(threeNumberSum([12,3,1,2,-6,5,-8,6],0))