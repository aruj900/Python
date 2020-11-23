def maxEvents(events):
    events = sorted(events, key=lambda x: x[1])
    visited = set()
    for start,end in events:
        for day in range(start,end+1):
            if day not in visited:
                visited.add(day)
                break
    return len(visited)

print(maxEvents([[1,2],[2,3],[3,4]]))