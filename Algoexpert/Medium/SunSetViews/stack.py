def sunsetViews(arr,dir):
    stack = []
    start = 0 if dir == "EAST" else len(arr) -1
    step = 1 if dir == "EAST" else -1

    idx = start
    while idx >= 0 and idx < len(arr):
        height = arr[idx]
        while len(stack) > 0 and arr[stack[-1]] <= height:
            stack.pop()
        stack.append(idx)
        idx += step
    if dir == "WEST":
        return stack[::-1]
    return stack
