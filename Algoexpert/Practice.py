def mergeOverlappingIntervals(intervals):
    # Write your code here.
        intervals.sort(key=lambda x: x[0])
        prev, res = intervals[0], []
        for interval in intervals:
            if interval[0] > prev[1]:
                res.append(prev)
                prev = interval
            else: 
                prev = [prev[0], max(prev[1], interval[1])]
        res.append(prev)
        return res