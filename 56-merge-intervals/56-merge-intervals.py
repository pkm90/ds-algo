class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        
        
        
        # is the input sorted or do we have to sort?
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]
        prev = intervals[0]
        for curr in intervals:
            if prev[1] < curr[0]:
                res.append(prev)
                prev = curr
                continue
            else: # prev[1] >= curr[0]: # if prevEnd >= currStart then we merge
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
        
        print(prev)
        if prev[1] >= intervals[-1][0]:
            res.append(prev)
        return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ########################################
        
        # iterate through the intervals
        #  if currStart < prevEnd then merge
        #  else, append previous
        # if the last element was merged then append
        # return result
        # time: nlogn, we sort which is nlogn, but if input was sorted then it would be just n since we iterate once
        # space: n, since we just have the result array
        
        if intervals is None:
            return None
        
        intervals.sort()
        
        res = []
        prev = intervals[0]
        
        for curr in intervals:
            if curr[0] <= prev[1]:
                prev[0] = min(prev[0], curr[0])
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(prev)
                prev = curr
        
        # checks to see if the last element was merged
        # !!! same condition as the iteration, we can't just check if last interval end is same as prev end: [[1,4],[2,3]]
        if intervals[-1][0] <= prev[1]:
            res.append(prev)
        return res