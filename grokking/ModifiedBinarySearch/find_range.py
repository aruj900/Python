def find_range(arr,key):
    result = [-1,-1]
    result[0] = binary_search(arr,key,False)
    if result[0] != -1:
        result[1] = binary_search(arr,key,True)
    return result

def binary_search(arr,key,max_index):
    n = len(arr) - 1
    key_idx = - 1
    start, end = 0, n
    while start <= end:
        mid = (start + end)// 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            key_idx = mid
            if max_index:
                start = mid + 1
            else:
                end = mid - 1
    return key_idx

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()

         
    