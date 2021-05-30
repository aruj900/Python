def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missing_number = []
    extra_number = set()
    
    for i in range(n):
        if len(missing_number) < k:
            if nums[i] != i + 1:
                missing_number.append(i+1)
                extra_number.add(nums[i])
    
    i = 1
    while len(missing_number) <k:
        candidate_number = i+n
        if candidate_number not in extra_number:
            missing_number.append(candidate_number)
        i += 1
    return missing_number

def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()

            