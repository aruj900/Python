def smallestDiff(array1,array2):
    array1.sort()
    array2.sort()
    id1 = 0
    id2 = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while id1 < len(array1) and id2 < len(array2):
        firstNum = array1[id1]
        secondNum = array2[id2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            id1 += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            id2 += 1
        else:
            return [firstNum,secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

