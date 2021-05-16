def stairCaseTraversal(height,maxsteps):
    current = 0
    waysToTop =[1]

    for currentHeight in range(1,height+1):
        startWindow = currentHeight - maxsteps -1
        endWindow = currentHeight -1

        if startWindow >= 0:
            current -= waysToTop[startWindow]
        
        current += waysToTop[endWindow]
        waysToTop.append(current)
    return waysToTop[height]