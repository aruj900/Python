from collections import deque, defaultdict

class Node:
    def __init__(self):
        self.indegrees = 0
        self.children = []

def topologicalSort(vertices,edges):
    output = []
    if vertices <= 0:
        return output
    
    graph = defaultdict(Node)
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].children.append(child)
        graph[child].indegrees += 1
    
    sources = deque()
    for node in graph:
        if not graph[node].indegrees:
            sources.append(node)
    while sources:
        current = sources.popleft()
        for child in graph[current].children:
            graph[child].indegrees -= 1
            if not graph[child].indegrees:
                sources.append(child)
        output.append(current)
    if len(output) == vertices:
        return output
    else:
        return []