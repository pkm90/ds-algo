class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        print(l)
        if nums[l - 1] == target:
            print('found')
            return l - 1
        
        return -1