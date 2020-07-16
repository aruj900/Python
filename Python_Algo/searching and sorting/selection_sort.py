def selection_sort(arr):
    
   for fillslot in range(len(arr)-1,0,-1):
       
       max = 0
       for k in range(1,fillslot+1):
           if arr[k] > arr[max]:
               max = k
       temp = arr[fillslot]
       arr[fillslot] = arr[max]
       arr[max] = temp        


arr = [5,8,3,10,1]
selection_sort(arr)
print(arr)
        