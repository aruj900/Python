def threeNumberSort(array,order):
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1
    
    thirdIdx = len(array) - 1
    for idx in range(len(array)-1,-1,-1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1
    return array

