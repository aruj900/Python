arr = [34,23,56,78,45,12,38]
for i in range(1,len(arr)):
    key = arr[i]
    j= i-1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j-1
    arr[j+1] = key
print(arr)