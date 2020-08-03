def quick_sort(arr):
    quick_sort_helper(arr,0,len(arr)-1)
    
def quick_sort_helper(arr,first,last):
    if first < last:
        splipoint = partition(arr,first,last)
        
        quick_sort_helper(arr,first,splipoint-1)
        quick_sort_helper(arr,splipoint+1,last)
        

def partition(arr,first,last):
    
    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last
    
    done = False
    
    while not done:
        
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
        
        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            rightmark -= 1
            
        if rightmark < leftmark:
            done = True
        
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    
    return rightmark

arr = [5,8,3,10,1]
quick_sort(arr)
print(arr)
