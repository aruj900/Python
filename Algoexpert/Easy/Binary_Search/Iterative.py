#O(n) Y | O(n) S
def binarySearch(array,target):
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
    while left <= right:
        middle = (left + right)//2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        
        elif target < potentialMatch:
            right = middle -1
        
        else:
            left = middle + 1
    return -1

print(binarySearch([1,4,7,9,14,16,56],1))