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
        
        