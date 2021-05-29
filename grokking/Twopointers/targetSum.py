def pair_with_targetsum(arr, target_sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        start = arr[left]
        end = arr[right]
        currentSum = start + end
        if currentSum == target_sum:
            return [left,right]
        elif currentSum < target_sum:
            left += 1
        else:
            right -= 1
    return [-1,-1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()