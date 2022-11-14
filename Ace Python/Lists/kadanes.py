def find_max_sub(lst):
    maxEndingHere = lst[0]
    maxSoFar = lst[0]
    for i in range(1,len(lst)):
        num = lst[i]
        maxEndingHere = max(num,maxEndingHere+num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar
        