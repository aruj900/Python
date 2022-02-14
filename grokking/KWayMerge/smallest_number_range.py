from heapq import *

from numpy import maximum

def find_smallest_range(lists):
    min_heap = []
    start, end = 0,float("inf")
    maximum = float("-inf")
    
    for arr in lists:
        heappush(min_heap,(arr[0],0,arr))
        maximum = max(maximum,arr[0])
    
    while len(min_heap) == len(lists):
        num, i , arr = heappop(min_heap)
        if end - start > maximum - num:
            start = num
            end = maximum
        if len(arr) > i + 1:
            heappush(min_heap,(arr[i+1],i+1,arr))
            maximum = max(maximum,arr[i+1])
    return [start,end]

def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()