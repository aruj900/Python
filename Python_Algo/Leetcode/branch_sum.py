
s = 7

def hasPathWithGivenSum(t, s):
    if t is None:
        return s == 0    

    return hasPathWithGivenSum(t.left, s - t.value) or hasPathWithGivenSum(t.right, s - t.value)


print(hasPathWithGivenSum(t,s))