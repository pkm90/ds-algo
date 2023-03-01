class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # continue while left <= right
        # start at mid and update the midpoint every iteration
        # / is normal div, returns float
        # // is floor div, returns int, cuts off everything after decimal
        
        
        
        left = 0
        right = len(nums) - 1
        
        # below works since it runs at most n times
        # useful for debugging as it removes infinite loops
        while left <= right:
        # for i in range(len(nums)):
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1