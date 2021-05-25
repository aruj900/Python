def find_string_anagrams(str1, pattern):
    window_start, matched = 0,0
    char_freq = {}
    
    for ch in pattern:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1
    
    result_indicies = []
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1
        if matched == len(char_freq):
            result_indicies.append(window_start)
    
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char]+= 1
    return result_indicies

def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()
            