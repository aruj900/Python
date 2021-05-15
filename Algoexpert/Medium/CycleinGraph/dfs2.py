WHITE, GREY, BALCK = 0,1,2  
def CycleinGraph(edges):
    numberofNodes = len(edges)
    colors = [WHITE for _ in range(numberofNodes)]

    for node in range(numberofNodes):
        if colors[node] != WHITE:
            continue
        containsCycle = traverseAndColor(node,edges,colors)
        if containsCycle:
            return True
    return False

def traverseAndColor(node,edges,colors):
    colors[node] = GREY

    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        if neighborColor == GREY:
            return True

        if neighborColor != WHITE:
            continue
        containsCycle = traverseAndColor(neighbor,edges,colors)
        if containsCycle:
            return True
    colors[node] = BALCK
    return False
