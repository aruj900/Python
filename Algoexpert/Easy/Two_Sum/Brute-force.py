def twoSum(array, targetSum):
    for i in range(len(array) -1):
        firstNum = array[i]
        for j in range(i + 1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
    return []

print(twoSum([1,3,2,9,5,6],11))