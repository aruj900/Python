from collections import deque


def find_trees(nodes, edges):
    if nodes <= 0:
        return []
    if nodes == 1:
        return [0]
    
    in_degrees = {i:0 for i in range(nodes)}
    graph = {i:[] for i in range(nodes)}
    
    for edge in edges:
        n1,n2 = edge[0],edge[1]
        graph[n1].append(n2)
        graph[n2].append(n1)
        
        in_degrees[n1] += 1
        in_degrees[n2] += 1
        
    leaves = deque()
    for key in in_degrees:
        if in_degrees[key] == 1:
            leaves.append(key)
    
    total_nodes = nodes
    while total_nodes > 2:
        level_size = len(leaves)
        total_nodes -= level_size
        for i in range(0,level_size):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 1:
                    leaves.append(child)
    return list(leaves)

def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()