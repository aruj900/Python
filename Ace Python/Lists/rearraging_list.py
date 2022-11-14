def rearrange(lst):
    left_most = 0
    for curr in range(len(lst)):
        if lst[curr] < 0:
            if curr != left_most:
                lst[curr], lst[left_most] = lst[left_most],lst[curr]
            left_most += 1
    return lst