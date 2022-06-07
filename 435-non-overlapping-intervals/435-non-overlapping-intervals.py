class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        if not intervals:
            return 0
        
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]
        print(intervals)
        for start, end in intervals[1:]:
            if prevEnd > start:
                prevEnd = min(prevEnd, end)
                count += 1
                continue
            prevEnd = end
        return count