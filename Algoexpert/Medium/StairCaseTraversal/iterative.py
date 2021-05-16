def stairCaseTraversal(height,maxsteps):
    waysToTop = [0 for _ in range(height+1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for current in range(2,height+1):
        step = 1
        while step <= maxsteps and step <= current:
            waysToTop[current] = waysToTop[current] + waysToTop[current - step]
            step += 1
    return waysToTop[height]