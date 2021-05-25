def fruits_into_baskets(fruits):
    window_start = 0
    char_freq = {}
    max_fruits = 0
    
    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        
        
        while len(char_freq) > 2:
            left_char = fruits[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1
        max_fruits = max(max_fruits,window_end-window_start +1)
    return max_fruits
def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
