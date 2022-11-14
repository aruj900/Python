def find_second_maximum(lst):
    if len(lst) < 2:
        return 
    max_no = second_no = float("-inf")
    for i in range(len(lst)):
        if lst[i] > max_no:
            second_no = max_no
            max_no = lst[i]
        elif lst[i] > second_no and lst[i] != max_no:
            second_no = lst[i]
    if second_no == float("-inf"):
        return
    else:
        return second_no

            