def length_of_longest_substring(str1, k):
    window_start,max_length,max_repeat = 0,0,0
    frequency_map = {}
    
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat = max(max_repeat,frequency_map[right_char])
        
        if (window_end - window_start + 1 - max_repeat) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length,window_end - window_start +1)
    return max_length

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()