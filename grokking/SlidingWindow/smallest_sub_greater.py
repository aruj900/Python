def smallest_subarray_with_given_sum(s,arr):
    window_sum = 0
    min_length = float("inf")
    windowStart = 0
    
    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]
        
        while window_sum >= s:
            min_length = min(min_length,windowEnd - windowStart + 1)
            window_sum -= arr[windowStart]
            windowStart += 1
    if min_length == float("inf"):
        return 0
    return min_length
def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()