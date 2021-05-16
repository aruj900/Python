def stairCaseTraversal(height,maxsteps):

    if height <= 1:
        return 1
    numberOfWays = 0
    for step in range(1,min(maxsteps,height)+1):
        numberOfWays += stairCaseTraversal(height-step,maxsteps)
    return numberOfWays