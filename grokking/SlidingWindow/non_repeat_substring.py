def non_repeat_substring(str1):
    window_start = 0
    char_index = {}
    max_length = 0
    
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        
        if right_char in char_index:
            window_start = max(window_start,char_index[right_char] + 1)
        
        char_index[right_char] = window_end
        max_length = max(max_length,window_end-window_start+1)
    return max_length

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()