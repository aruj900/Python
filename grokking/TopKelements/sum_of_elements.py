from heapq import *

def find_sum_of_elements(nums, k1, k2):
    min_heap = []
    for i in nums:
        heappush(min_heap,i)
    
    for _ in range(k1):
        heappop(min_heap)
    
    ele_sum = 0
    for _ in range(k2 - k1 -1):
        ele_sum += heappop(min_heap)
    return ele_sum

def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()


