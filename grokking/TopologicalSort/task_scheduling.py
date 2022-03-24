from collections import deque

from numpy import source


def is_scheduling_possible(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return False
    
    in_degree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}
    
    for pre in prerequisites:
        parent,child = pre[0], pre[1]
        graph[parent].append(child)
        in_degree[child] += 1
    
    source = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            source.append(key)
    
    while source:
        vertex = source.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)
    return len(sorted_order) == tasks

def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
        
    