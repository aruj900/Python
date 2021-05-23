def sunsetViews(arr,dir):
    res = []

    startIdx = 0 if dir == "WEST" else len(arr) - 1
    step = 1 if dir == "WEST" else -1

    idx = startIdx
    maxHeight = 0
    while idx >= 0 and idx < len(arr):
        height = arr[idx]
        if height > maxHeight:
            res.append(idx)
        maxHeight = max(height,maxHeight)
        idx += step
    
    if dir == "EAST":
        return res[::-1]
    return res

