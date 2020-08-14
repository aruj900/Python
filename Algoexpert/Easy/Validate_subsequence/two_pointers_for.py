def validSub(arr,sub):
    seqId = 0
    for value in arr:
        if seqId == len(sub):
            break
        if sub[seqId] == value:
            seqId += 1
    return seqId == len(sub)

print(validSub([1,3,5,7,9,-3,7,8],[3,9,8]))