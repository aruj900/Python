from heapq import *
class Element:
    def __init__(self,number,freq,order):
        self.number = number
        self.freq = freq 
        self.order = order
    
    def __lt__(self,other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.order > other.order

class FreqStack:
    order = 0
    max_heap = []
    freq_map = {}
    
    def push(self,num):
        if num not in self.freq_map:
            self.freq_map[num] = 0
        self.freq_map[num] += 1
        heappush(self.max_heap,Element(num,self.freq_map[num],self.order))
        self.order += 1
    
    def pop(self):
        num = heappop(self.max_heap).number
        if self.freq_map[num] > 1:
            self.freq_map[num] -= 1
        else:
            del self.freq_map[num]
        return num
    
def main():
  frequencyStack = FreqStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
        
        
main()