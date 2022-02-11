from heapq import *
import heapq

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    
    def find_sliding_window_median(self,nums,k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap,-nums[i])
            else:
                heappush(self.min_heap,nums[i])
            
            self.rebalance_heaps()
            
            if i - k + 1  >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = (-self.max_heap[0] + self.min_heap[0])/2.0
                else:
                    result[i - k + 1] = -self.max_heap[0]/ 1.0
                
                element_to_remove = nums[i - k + 1]
                if element_to_remove <= -self.max_heap[0]:
                    self.remove(self.max_heap,-element_to_remove)
                else:
                    self.remove(self.min_heap,element_to_remove)
                self.rebalance_heaps()
        return result
    
    def remove(self,heap,element):
        idx = heap.index(element)
        heap[idx] = heap[-1]
        del heap[-1]
        
        if idx < len(heap):
            heapq._siftup(heap,idx)
            heapq._siftdown(heap,0,idx)
    
    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap,-heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap,-heappop(self.min_heap))

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()