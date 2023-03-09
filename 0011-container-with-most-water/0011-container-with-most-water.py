class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        
        
        
        
        
        res = -inf
        left, right = 0, len(height) - 1
        
        while left < right:
            vol = (right - left) * min(height[left], height[right])
            res = max(res, vol)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 vol = (j - i) * min(height[i], height[j])
#                 res = max(res, vol)
        
                
        return res