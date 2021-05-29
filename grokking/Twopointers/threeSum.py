def search_triplets(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == 0:
                triplets.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            else:
                right -= 1
    return triplets

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()
