def CycleinGraph(edges):
    numberofNodes = len(edges)
    visited = [False for _ in range(numberofNodes)]
    currentlyinStack = [False for _ in range(numberofNodes)]

    for node in range(numberofNodes):
        if visited[node]:
            continue
        containsCycle = isNodeCycle(edges,node,visited,currentlyinStack)
        if containsCycle:
            return True
    return False

def isNodeCycle(edges,node,visited,currentlyinStack):
    visited[node] = True
    currentlyinStack[node] = True
    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeCycle(edges,neighbor,visited,currentlyinStack)
            if containsCycle:
                return True
        elif currentlyinStack[neighbor]:
            return True

    currentlyinStack[node] = False
    return False