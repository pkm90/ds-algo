class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        
        
        
        # nums = [3,2,3,1,2,4,5,5,6]
        nums.sort()
        # print(nums)
        return nums[-k]
        