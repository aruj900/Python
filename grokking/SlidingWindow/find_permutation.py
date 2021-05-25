def find_permutation(str1, pattern):
    window_start , matched = 0,0
    pattern_freq = {}
    
    for ch in pattern:
        if ch not in pattern_freq:
            pattern_freq[ch] = 0
        pattern_freq[ch] += 1
    
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_freq:
            pattern_freq[right_char] -= 1
            if pattern_freq[right_char] == 0:
                matched += 1
        if matched == len(pattern_freq):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_freq:
                if pattern_freq[left_char] == 0:
                    matched -= 1
                pattern_freq[left_char] += 1
    return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
    