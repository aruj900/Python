from heapq import *

def find_maximum_distinct_elements(nums, k):
    distinct_count = 0
    if len(nums) <= k:
        return 0
    num_freq = {}
    for i in nums:
        if i not in num_freq:
            num_freq[i] = 0
        num_freq[i] += 1
    
    min_heap = []
    for num, freq in num_freq.items():
        if freq == 1:
            distinct_count += 1
        else:
            heappush(min_heap,(freq,num))
    
    while k > 0 and min_heap:
        freq,num = heappop(min_heap)
        k -= freq - 1
        if k >= 0:
            distinct_count += 1
    if k > 0:
        distinct_count -= k
    return distinct_count

def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
        