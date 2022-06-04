class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # standard binary search
        # the left and right will cross so we return left
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # if nums[mid] == target:
            #     return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        print(l, r)
        return l
        
        
        # in this example we change while condition to check if mid outside
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    
        if nums[l] < target:
            return l + 1
        else:
            return l
