
def twoSum(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == target:
            return [arr[left],arr[right]]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    return []

print(twoSum([1,3,2,9,5,6],11))