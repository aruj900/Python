def stairCaseTraversal(height,maxsteps,memoize):

    if height in memoize:
        return memoize[height]
    numberOfWays = 0
    for step in range(1,min(maxsteps,height)+1):
        numberOfWays += stairCaseTraversal(height-step,maxsteps,memoize)
    memoize[height] = numberOfWays
    return numberOfWays