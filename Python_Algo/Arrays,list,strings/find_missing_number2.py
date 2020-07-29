import collections

def finder2(arr1,arr2):

    d = collections.defaultdict(int)
    
    for num in arr2:
        d[num] +=1
    
    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -=1
    

arr1 = [2,4,7,3,9]
arr2 = [2,4,9,7]

print(finder2(arr1,arr2)) 
                    