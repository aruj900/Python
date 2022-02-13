from heapq import *
from collections import deque
import queue

def reorganize_string(str, k):
    if k <= 1:
        return str
    char_freq = {}
    for ch in str:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1
    
    max_heap = []
    for ch,freq in char_freq.items():
        heappush(max_heap,(-freq,ch))
    
    queue = deque()
    result = []
    while max_heap:
        freq,ch = heappop(max_heap)
        result.append(ch)
        queue.append((ch , freq+1))
        if len(queue) == k:
            char,frequency = queue.popleft()
            if -frequency > 0:
                heappush(max_heap,(frequency,char))
    return ''.join(result) if len(result) == len(str) else ""

def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()
