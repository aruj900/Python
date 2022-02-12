def get_permutations(nums):
    out = []
    if len(nums) == 1:
        out = [nums]
    elif len(nums) == 2:
        out = [nums,nums[::-1]]
    else:
        for i,num in enumerate(nums):
            for perm in get_permutations(nums[:i] + nums[i+1:]):
                out += [[num]+perm]
    return out