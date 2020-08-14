def bubbleSort(array):
    
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            
            if array[j] > array[j+1]:
                swap(j,j+1,array)
    return array

def swap(i,k,array):
    array[i],array[k] = array[k],array[i]

print(bubbleSort([1,6,2,8,23]))