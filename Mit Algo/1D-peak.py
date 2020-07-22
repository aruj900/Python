def findPeakUtil(arr,low,high,n):
    mid = (low+high)//2
    
    
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid
    
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr,low,(mid-1),n)
    
    else:
        return findPeakUtil(arr,(mid + 1),high,n)
        


def findPeak(arr):
    n = len(arr)
    return findPeakUtil(arr,0,n-1,n)

arr = [1,11,12,15,19,30]

print(findPeak(arr))