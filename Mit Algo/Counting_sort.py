def counting_sort(array):
    size = len(array)
    output = [0]*size
    
    count = [0] * 10
    
    for i in range(0,size):
        count[array[i]] += 1
    
    for i in range(1,10):
        count[i] += count[i-1]
    
    i = size -1
    
    while i >= 0:
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
        i -= 1
    
    for i in range(0,size):
        array[i] = output[i]
        
data = [4,2,5,7,3,8,4,9,2]

counting_sort(data)

print(data)