def waysToTraverse(width,height):
    numberofWays = [[0 for _ in range(width+1)] for _ in range(height+1)]
    for widthIdx in range(1,width+1):
        for heightIdx in range(1,height+1):
            if widthIdx == 1 or heightIdx == 1:
                numberofWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberofWays[heightIdx][widthIdx-1]
                waysUp = numberofWays[heightIdx-1][widthIdx]
                numberofWays[widthIdx][heightIdx] = waysLeft + waysUp
    return numberofWays[-1][-1]