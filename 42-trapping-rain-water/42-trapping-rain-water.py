class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        
        
        
        
        
        
        
        # add nothing until the first height
        # keep track of the max so far and add difference of this and curr until last peak
        # do the same thing for reverse of numbers after peak
        
        peak = [float(-inf), -1] # [ height, idx ]
        front = None
        back = None
        res = 0
        
        # find peak and separate heights
        for i, h in enumerate(height):
            if peak[0] < h:
                peak = [h, i]
        
        front = height[:peak[1]]
        back = height[peak[1]:]
        back.reverse()
        
        # go through and calculate water
        maxSoFar = 0
        for h in front:
            diff = maxSoFar - h
            if diff > 0:
                res += diff
            maxSoFar = max(maxSoFar, h)
            
        maxSoFar = 0
        for h in back:
            diff = maxSoFar - h
            if diff > 0:
                res += diff
            maxSoFar = max(maxSoFar, h)
        
        return res
        
        
        
        