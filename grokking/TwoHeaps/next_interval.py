from heapq import *

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

def find_next_interval(intervals):
    n = len(intervals)
    max_start_heap, max_end_heap = [], []
    result = [0 for x in range(n)]
    
    for end_idx in range(n):
        heappush(max_start_heap, -intervals[end_idx].start,end_idx)
        heappush(max_end_heap, -intervals[end_idx].end,end_idx)
    
    for _ in range(n):
        top_end, end_idx = heappop(max_end_heap)
        result[end_idx] = -1
        if -max_start_heap[0][0] >= -top_end:
            top_start, start_idx = heappop(max_start_heap)
            
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_idx = heappop(max_start_heap)
            result[end_idx] = start_idx
            heappush(max_start_heap,(top_start,start_idx))
    return result
                
        
    
        
        