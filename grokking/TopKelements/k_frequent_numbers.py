from heapq import *

def find_k_frequent_numbers(nums, k):
    num_freq = {}
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 0
        num_freq[num] += 1
    
    min_heap = []
    for num, freq in num_freq.items():
        heappush(min_heap,(freq,num))
        if len(min_heap) > k:
            heappop(min_heap)
    
    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])
    return top_numbers

def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()