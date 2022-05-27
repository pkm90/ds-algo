class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        
        # bruteforce, go through each combination of two points and find area
        # tle, as expected
#         n = len(height)
#         res = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 fat = j - i
#                 tall = min(height[i], height[j])
#                 area = fat * tall
#                 res = max(res, area)
#         return res
    
        # 2 ptr, start outwards and go inwards
        # we shift the smaller of the two ptr since the max area is bounded by smaller
        n = len(height)
        res = 0
        l, r = 0, n - 1
        while l < r:
            fat = r - l
            tall = min(height[l], height[r])
            area = fat * tall
            res = max(res, area)
            
            if tall == height[l]:
                l += 1
            else:
                r -= 1
        return res
        
        
        
        
        
        
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   ###############################     
        
        
        
        
#         # start from outside, keep track of max, calculate area
#         # move the smaller pointer inward since the area is capped by the smaller pointer
#         maxHeight = 0
#         l, r = 0, len(height) - 1
        
#         while l < r:
#             area = min(height[l], height[r]) * (r - l)
#             maxHeight = max(maxHeight, area)
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
        
#         return maxHeight
        
        
        
###################
        
#         # keep track of max
#         # we can start from outside to maximize width
#         # we then work our way inside
#         # which pointer do we move? we move the smaller one since
#         #  moving the larger one cannot increase height as the height
#         #  is bounded by the min of both points
        
#         n = len(height)
#         l, r = 0, n - 1
#         maxHeight = 0
        
#         while l < r:
#             h = min(height[l], height[r])
#             w = r - l
#             area = w * h
#             maxHeight = max(maxHeight, area)
            
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
        
#         return maxHeight