#O(n^2) T | O(1) space
def selectionSort(array):
    for i in range(len(array)-1,0,-1):
        max1 = 0
        for k in range(1,i+1):
            if array[k] > array[max1]:
                max1 = k
        swap(i,max1,array)
    return array

def swap(i,j,array):
    array[i],array[j] = array[j],array[i]
    
arr = [5,8,3,10,1]
selectionSort(arr)
print(arr)
    