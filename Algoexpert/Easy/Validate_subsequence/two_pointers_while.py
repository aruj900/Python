def validSub(array,sequence):
    arrIdx = 0
    seqIdx = 0
    
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx +=1
    return seqIdx == len(sequence)

print(validSub([1,3,5,7,9,-3,7,8],[3,9,8]))