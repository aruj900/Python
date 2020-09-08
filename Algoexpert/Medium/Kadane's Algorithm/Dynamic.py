# O(n) T | O(1) S
def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar
print(kadanesAlgorithm([1,-2,4,-7,8,9,-5,-3]))