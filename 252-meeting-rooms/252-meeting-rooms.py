class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        intervals.sort()
        if not intervals:
            return True
        
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd > start:
                return False
            else:
                prevEnd = end
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # check if there are any overlapping intervals
#         # an check if an interval starts before previous ends, start < prevEnd
        
#         if len(intervals) == 0: return True
        
#         intervals.sort()
#         lastEnd = -1
        
#         for start, end in intervals:
#             if start < lastEnd:
#                 return False
#             lastEnd = end
            
#         return True