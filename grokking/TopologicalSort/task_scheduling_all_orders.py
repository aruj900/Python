from collections import deque

from numpy import source


def print_orders(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return []
    
    in_degrees = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}
    
    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        graph[parent].append(child)
        in_degrees[child] += 1
    
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)
    
    print_all_orders(in_degrees,sorted_order,sources,graph)
    
def print_all_orders(in_degrees,sorted_order,sources,graph):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_next = deque(sources)
            sources_next.remove(vertex)
            
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources_next.append(child)
            
            print_all_orders(in_degrees,sorted_order,sources_next,graph)
            
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degrees[child] += 1
    if len(sorted_order) == len(in_degrees):
        print(sorted_order)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
                