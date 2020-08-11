def twoSum(arr,target):
    nums = {}
    for num in arr:
        if target - num in nums:
            return [target - num,num]
        else:
            nums[num] = True
    return []

print(twoSum([1,3,2,9,5,6],11))