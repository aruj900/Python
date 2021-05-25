def find_average_of_sub(k,arr):
    result = []
    windowSum, windowStart = 0.0,0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k -1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result
def main():
  result = find_average_of_sub(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()