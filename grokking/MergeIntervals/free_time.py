from heapq import *

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class EmployeeInterval:
    def __init__(self,interval,emp_idx,interval_idx):
        self.interval = interval
        self.emp_idx = emp_idx
        self.interval_idx = interval_idx

    def __lt_(self,other):
        self.interval.start < other.interval.start

def find_free_time(schedule):
    if schedule is None:
        return []
    n = len(schedule)
    result,min_heap = [],[]
    for i in range(n):
        heappush(min_heap,EmployeeInterval(schedule[i][0],i,0))
    previous_interval = min_heap[0].interval
    while min_heap:
        top = heappop(min_heap)
        if previous_interval.end < top.interval.start:
            result.append(Interval(previous_interval.end,top.interval.start))
            previous_interval = top.interval
        else:
            if previous_interval.end < top.interval.end:
                previous_interval = top.interval
        employee_schedule = schedule[top.emp_idx]
        if len(employee_schedule) > top.interval_idx + 1:
            heappush(min_heap,EmployeeInterval(employee_schedule[top.interval_idx + 1],top.emp_idx,top.interval_idx + 1))
    return result