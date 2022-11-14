def longestSubstringWithoutDuplication(string):
    # Write your code here.
    window_start = 0
    start_index = []
    max_length = 0
    char_index_map = {}
    
    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(string)):
        right_char = string[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        if right_char in char_index_map:
          # this is tricky; in the current window, we will not have any 'right_char' after its previous index
          # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
          window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
        start_index.append([max_length,window_start])
    print(start_index)
    for l in start_index:
        if l[0] == max_length:
            start = l[1]
            break
    return string[start:start+max_length]
print(longestSubstringWithoutDuplication("clementisacap"))

