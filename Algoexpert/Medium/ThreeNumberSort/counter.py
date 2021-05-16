def threeNumberSort(array,order):
    valueCount = [0,0,0]

    for ele in array:
        orderIdx = order.index(ele)
        valueCount[orderIdx] += 1
    
    for i in range(3):
        value = order[i]
        count = valueCount[i]

        numElementBefore = sum(valueCount[:i])
        for n in range(count):
            currentIdx = numElementBefore + n
            array[currentIdx] = value
    return array