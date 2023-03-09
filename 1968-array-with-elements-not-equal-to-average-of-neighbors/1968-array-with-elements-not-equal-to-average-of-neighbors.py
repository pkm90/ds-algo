class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
#                R       
#         [1,2,4,5]
                
#         [1 4  5  2]
#            L
            
#         make sure ( (nums[i-1] + nums[i+1]) / 2) != nums[i]
        
    
        # sort input, append to result small, large, small, large
        
        # res = [0 for i in range(len(nums)) ] # [0,0,0,0,0,0]
        res = []
        left, right = 0, len(nums) - 1
        nums.sort()
        
        while left <= right:
            res.append(nums[left])
            left += 1
            
            if left > right:
                break
            
            res.append(nums[right])
            right -= 1
        
        
        return res
        
        
            
            
#         if I alternate small and large
        
#         small, large, small, large, ...
#         1, 5, 2, 
        
        
           
