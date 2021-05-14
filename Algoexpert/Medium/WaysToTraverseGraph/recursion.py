def waysToTraverseGraph(width,height):
    if width == 1 or height == 1:
        return 1
    return waysToTraverseGraph(width-1,height) + waysToTraverseGraph(width,height-1)

