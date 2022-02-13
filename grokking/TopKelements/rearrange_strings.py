from heapq import *
def rearrange_string(str):
    char_freq = {}
    for ch in str:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1
    max_heap = []
    for ch,freq in char_freq.items():
        heappush(max_heap,(-freq,ch))
    
    prev_ch, prev_freq = None,0
    result = []
    while max_heap:
        freq,ch = heappop(max_heap)
        if prev_ch and -prev_freq > 0:
            heappush(max_heap,(prev_freq,prev_ch))
        result.append(ch)
        prev_ch = ch
        prev_freq = freq + 1
        
    return ''.join(result) if len(result) == len(str) else ""

def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()