from heapq import *

def sort_character_by_frequency(str):
    char_map = {}
    for i in str:
        if i not in char_map:
            char_map[i] = 0
        char_map[i] += 1
    
    max_heap = []
    for ch,freq in char_map.items():
        heappush(max_heap,(-freq,ch))
    
    sorted_string = []
    while max_heap:
        freq, ch = heappop(max_heap)
        for _ in range(-freq):
            sorted_string.append(ch)
    return ''.join(sorted_string)

def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()