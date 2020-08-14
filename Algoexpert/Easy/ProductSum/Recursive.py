def productSum(array,multiplier = 1):
    sum = 0
    for ele in array:
        if type(ele) is list:
            sum += productSum(ele,multiplier+1)
        else:
            sum += ele
    return sum*multiplier

print(productSum([1,5,[2,3],5,7,[1,[6,-9],2],7]))