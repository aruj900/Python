def heapify(arr,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def insert(arr,newNum):
    size = len(arr)
    
    if size == 0:
        array.append(newNum)
    
    else:
        arr.append(newNum)
        for i in range((size//2)-1,-1,-1):
            heapify(arr,size,i)
            
def deleteNode(arr,num):
    size = len(arr)
    i = 0
    for i in range(0,size):
        if num == arr[i]:
            break
    
    arr[i],arr[size-1] = arr[size-1],arr[i]
    for i in range((size//2)-1,-1,-1):
        heapify(arr,size,i)
        
def heap_sort(arr):
    n = len(arr)
    #Build max heap
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        # Swap
        arr[i],arr[0] = arr[0],arr[i]
        
        heapify(arr,i,0)

arr = [1,12,8,9,6,10]
print(heap_sort(arr))    
print(arr)    

