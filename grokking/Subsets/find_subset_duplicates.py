def find_subset(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    start_idx,end_idx = 0,0
    for i in range(len(nums)):
        start_idx = 0
        if i > 0 and nums[i] == nums[i-1]:
            start_idx = end_idx + 1
        end_idx = len(subsets) - 1
        for j in range(start_idx,end_idx+1):
            set1 = list(subsets[i])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets
            
        
    