from heapq import *

def schedule_tasks(tasks, k):
    interval_count = 0
    task_freq = {}
    for ch in tasks:
        if ch not in task_freq:
            task_freq[ch] = 0
        task_freq[ch] += 1
    
    max_heap = []
    for ch, freq in task_freq.items():
        heappush(max_heap,(-freq,ch))
    
    while max_heap:
        wait_list = []
        n = k + 1
        while n > 0 and max_heap:
            interval_count += 1
            freq,ch = heappop(max_heap)
            if -freq  > 1:
                wait_list.append((freq + 1,ch))
            n -= 1
            
        for freq,ch in wait_list:
            heappush(max_heap,(freq,ch))
        if max_heap:
            interval_count += n
    return interval_count

def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
