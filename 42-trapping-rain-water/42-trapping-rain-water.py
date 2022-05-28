# maybe again?
class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        # find last peak
        peak = [0, 0] # [index, peak]
        for i in range(len(height) - 1, -1, -1):
            if height[i] > peak[1]:
                peak = [i, height[i]]
                        
        # separate heights
        front = height[:peak[0]]
        back = height[peak[0]:]
        back.reverse()
                
        # calculate water
        res = 0
        peak = 0
        for num in front:
            peak = max(peak, num)
            if peak - num > 0:
                res += peak - num
        
        peak = 0
        for num in back:
            peak = max(peak, num)
            if peak - num > 0:
                res += peak - num
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ##############################3
        
        
#         # add nothing until the first height
#         # keep track of the max so far and add difference of this and curr until last peak
#         # do the same thing for reverse of numbers after peak
        
#         peak = [float(-inf), -1] # [ height, idx ]
#         front = None
#         back = None
#         res = 0
        
#         # find peak and separate heights
#         for i, h in enumerate(height):
#             if peak[0] < h:
#                 peak = [h, i]
        
#         front = height[:peak[1]]
#         back = height[peak[1]:]
#         back.reverse()
        
#         # go through and calculate water
#         maxSoFar = 0
#         for h in front:
#             diff = maxSoFar - h
#             if diff > 0:
#                 res += diff
#             maxSoFar = max(maxSoFar, h)
            
#         maxSoFar = 0
#         for h in back:
#             diff = maxSoFar - h
#             if diff > 0:
#                 res += diff
#             maxSoFar = max(maxSoFar, h)
        
#         return res