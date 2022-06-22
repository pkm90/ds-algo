class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        
        
        
        # nums = [3,2,3,1,2,4,5,5,6]
        # nums.sort()
        nums = [ -1 * i for i in nums ]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return nums[0] * -1
        # print(nums)
        # return nums[-k]
        