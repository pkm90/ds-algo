class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        
        # simply put the number they want into the result and return it
        # time: n
        # space: n
        
        # None will fail, 
        
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            res[i] = nums[nums[i]]
        return res