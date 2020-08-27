def moveToEnd(array,ele):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == ele:
            j -= 1
        if array[i] == ele:
            array[i],array[j] = array[j],array[i]
        i += 1
    return array

print(moveToEnd([2,1,2,3,8,2,7,2,2],2))