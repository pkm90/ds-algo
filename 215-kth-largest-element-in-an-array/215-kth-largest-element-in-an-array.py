class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        
        
        # sort
        nums.sort()
        return nums[-k]
        
        # heap
        nums = [ -1 * i for i in nums ]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return nums[0] * -1