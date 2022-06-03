class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        
        
        
        # [1,2,3,4,5]
        # [4,5,1,2,3]
        # [3,4,5,1,2]
        # [2,3,4,5,1]
        # middle should always be less than right
        # if mid > right, then we know pivot is between mid and right
        # else, pivot is between left and mid
        
        # find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        # l is the smallest x that matches condition, smallest num that is less than r
        pivot = l
        print(l)
        
        # find which partition target is in
        l, r = 0, len(nums) - 1
        if target <= nums[r]:
            l = pivot
        else:
            r = pivot
        
        # search on the applicable half
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
    
        return l if nums[l] == target else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # find pivot first
#         # use pivot to find target
#         # find which partition target is inside
#         # then do a new binary search
        
#         if len(nums) == 0: return -1
        
#         # find pivot
#         l, r = 0, len(nums) - 1
#         pivot = None
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] < nums[mid - 1]: # no longer increasing, found pivot
#                 pivot = mid
            
#             if nums[mid] > nums[r]: # pivot is in right partition
#                 l = mid + 1
#             else:
#                 r = mid - 1
        
#         pivot = l if pivot is None else pivot
        
#         # find which partition target is inside
#         l, r = 0, len(nums) - 1
#         if target <= nums[r]:
#             l = pivot
#         else:
#             r = pivot
        
#         # binary search to find target
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid         

#             if target < nums[mid]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
        
#         if nums[l] == target:
#             return l
#         else:
#             return -1
        
        
        
        ####################
        
        
        
        
        
#         # find pivot, check if target is to the left/right of pivot, binary search
#         # or search while finding pivot
#         # to do this, there are a few scenarios:
#         # not going to do that,
        
#         # search for pivot,
#         # if mid > right, then we know the pivot is inside this region
#         # eventually l and r will converge onto the pivot
#         n = len(nums)
#         l, r = 0, n - 1
#         while l < r:
#             m = l + (r - l) // 2
#             if nums[m] > nums[r]:
#                 l = m + 1
#             else:
#                 r = m
        
#         # set pivot, binary search based on whether target is above/below the partitions
#         pivot = l
#         if target <= nums[n - 1]:
#             l, r = pivot, n - 1
#         else:
#             l, r = 0, pivot - 1
        
#         # finally, the binary search
#         print('before search', l, r)
#         while l <= r:
#             m = l + (r - l) // 2
#             if target == nums[m]:
#                 return m
            
#             if target < nums[m]:
#                 r = m - 1
#             else:
#                 l = m + 1

#         return -1

            