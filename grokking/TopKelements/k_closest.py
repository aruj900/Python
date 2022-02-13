from heapq import *
from unittest import result

def find_closest_elements(arr, K, X):
    index = binary_search(arr,X)
    low, high = index - K , index + K
    low = max(low,0)
    high = min(high,len(arr) - 1)
    min_heap = []
    for i in range(low,high+1):
        heappush(min_heap,(abs(arr[i]-X),arr[i]))
    result = []
    for _ in range(K):
        result.append(heappop(min_heap)[1])
    result.sort()
    return result

def binary_search(arr,key):
    if key < arr[0]:
        return 0
    if key > arr[len(arr) - 1]:
        return len(arr) - 1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if key < arr[mid]:
            end = mid -1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    if abs(arr[start] - key) < abs(key - arr[end]):
        return start
    return end

def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()