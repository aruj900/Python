def triplet_sum_close_to_target(arr,target):
    arr.sort()
    smallest_diff = float("inf")
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            tareget_diff = target - arr[i] - arr[left] - arr[right]
            if tareget_diff == 0:
                return target - tareget_diff
            
            if abs(tareget_diff) < abs(smallest_diff) or (abs(tareget_diff) == abs(smallest_diff) and tareget_diff > smallest_diff):
                smallest_diff = tareget_diff
            if tareget_diff > 0:
                left += 1
            else:
                right -= 1
    return target - smallest_diff

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
