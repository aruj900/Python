def permute(array):
    
    out = []
    if len(array) == 1:
        out = [array]
    
    else:
        for i , let in enumerate(array):
            
            for perm in permute(array[:i] + array[i+ 1:]):
                out += [[let] + perm]
    return out

print(permute([1,2,3]))