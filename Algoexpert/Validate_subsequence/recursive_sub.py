def validSub(arr,sub):
    if sub == []:
        return True
    if sub[0] in arr:
        return validSub(arr[arr.index(sub[0])+1:],sub[1:])
    else:
        return False
print(validSub([1,3,5,7,9,-3,7,8],[3,9,8]))
    
        