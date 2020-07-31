def binary_search(arr,ele):
    
    first = 0
    last = len(arr) -1
    
    found = False
    
    while first <= last and not found:
        mid = (first + last)//2
        if arr[mid] == ele:
            found = True
            return mid
        elif ele < arr[mid]:
            last = mid -1
        else:
            first = mid + 1
    return -1

arr = [1,3,5,7,9,10,14]

print(binary_search(arr,14))        
