class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        res = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            print(nums[mid], target)
            if nums[mid] <= target:
                print('l')
                res = mid
                l = mid + 1
            else:
                print('r')
                r = mid - 1
        
        return l
        