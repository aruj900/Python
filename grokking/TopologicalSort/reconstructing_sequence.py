from collections import deque
from typing import Sequence


def can_construct(originalSeq, sequences):
    sorted_order = []
    if len(originalSeq) == 0:
        return False
    in_degree = {}
    graph = {}
    for seq in sequences:
        for num in seq:
            in_degree[num] = 0
            graph[num] = []
    
    for seq in sequences:
        for i in range(1,len(seq)):
            parent,child = seq[i-1], seq[i]
            graph[parent].append(child)
            in_degree[child] += 1
    if len(in_degree) != len(originalSeq):
        return False
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    
    while sources:
        if len(sources) > 1:
            return False
        if originalSeq[len(sorted_order)] != sources[0]:
            return False
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    return len(sorted_order) == len(originalSeq)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
            
            