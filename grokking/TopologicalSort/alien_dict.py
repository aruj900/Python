from collections import deque


def find_order(words):
    if len(words) == 0:
        return ""
    in_degree = {}
    graph = {}
    for word in words:
        for ch in word:
            in_degree[ch] = 0
            graph[ch] = []
    
    for i in range(len(words)-1):
        w1,w2 = words[i],words[i+1]
        for j in range(min(len(w1),len(w2))):
            parent,child = w1[j],w2[j]
            if parent != child:
                graph[parent] = child
                in_degree[child] += 1
                break
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    
    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order) != len(in_degree):
        return ""

    return ''.join(sorted_order)

def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()