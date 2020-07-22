

from math import ceil

def findMax(arr,rows,mid,max):
    
    max_index = 0
    for i in range(rows):
        if (max < arr[i][mid]):
            
            max = arr[i][mid]
            max_index = i
    
    return max,max_index

def findPeakRec(arr,rows,columns,mid):
    max = 0
    max, max_index = findMax(arr,rows,mid,max)
    
    if (mid == 0 or mid == columns -1):
        return max
    
    if (max >= arr[max_index][mid -1] and max >= arr[max_index][mid + 1]):
        return max

    if (max < arr[max_index][mid - 1]):
        return findPeakRec(arr,rows,columns,mid - ceil(mid/2))
    
    return findPeakRec(arr,rows,columns,mid + ceil(mid/2))

def findPeak(arr,rows,columns):
    return findPeakRec(arr,rows,columns,columns//2)

arr = [[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]]

rows = 4
columns = 4

print(findPeak(arr,rows,columns))