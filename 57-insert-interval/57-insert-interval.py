class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        
        # find the right place, insert it
        # if new interval overlaps, then merge them together
        
        
        res = []
        start, end = float(inf), float(-inf)
        
        for i, curr in enumerate(intervals):
            # checks if we need to continue merging or not
            # if currentStart > newEnd
            if curr[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
                # break
                
            # if there are no overlaps then append to result and continue
            # if currentEnd < newStart
            if curr[1] < newInterval[0]:
                res.append(curr)
                # start, end = 0, 0
            else:
                start = min(curr[0], newInterval[0])
                end = max(curr[1], newInterval[1])
                newInterval = [start, end]
                # if something overlaps with newInterval then merge, append, break
        
        # if we never appended newInterval, then the right place is at the end
        res.append(newInterval)
        return res        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ############################
        
        
#         # only two conditions we need to check to see if the interval overlaps 
#         # check if new interval goes before current, or after current
#         #  if it is after current interval, then append interval to result and continue
#         #  if it is before current interval, then append the merged interval, extend rest, return
#         #  if it is neither condition, then we need to merge the interval
#         # finally, in case the interval goes in the very end, append the newInterval and return
#         # time: linear, since we just iterate through intervals once
#         # space: linear, since we basically recreate the intervals
#         #  can we do better than linear space? yes, if we modify the input
        
#         inStart, inEnd = newInterval[0], newInterval[1]
#         res = []
        
#         for i, interval in enumerate(intervals):
#             # if current end is less than new start, add current interval to res and continue
#             if interval[1] < inStart:
#                 res.append(interval)
#                 continue
#             # if insert end is before the current beginning, we found right place, append, extend, return
#             if inEnd < interval[0]:
#                 res.append(newInterval)
#                 res.extend(intervals[i:])
#                 return res
#             newInterval[0] = min(newInterval[0], interval[0])
#             newInterval[1] = max(newInterval[1], interval[1])
        
#         # in case the right place is at the very end, we will simply append and return
#         res.append(newInterval)
#         return res