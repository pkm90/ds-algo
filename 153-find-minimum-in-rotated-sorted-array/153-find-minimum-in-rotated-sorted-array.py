class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        
        
        
        # binary search through entire thing
        # we're looking for pivot, which is also minimum
        # middle should never be > right, if it is then hte pivot is between mid : right
        
        # we can either do template or keep track of min
        # keep track of the minimum
#         res = float(inf)
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = (l + r) // 2
#             res = min(res, nums[mid])
            
#             if nums[mid] > nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return res


                
        # template
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] < nums[r]:
#                 r = mid
#             else:
#                 l = mid + 1
#         print(l, r)
#         return nums[l]
        
        
        
        
        
        
        
        
        ###################################3
        
#         # this is just finding pivot
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] < nums[r]:
#                 r = mid
#             else:
#                 l = mid + 1
                
#         # since l is the smallest k that matches condition
#         return nums[l]


       #########################
        
#         # find pivot...pivot is where the left > curr < right
#         # if mid > right, we know htat pivot is somewhere in the right side
        
#         l, r = 0, len(nums) - 1
        
#         while l < r:
#             mid = (r + l) // 2
#             if nums[mid] < nums[mid - 1]: return nums[mid]
            
#             if nums[r] < nums[mid]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
                
#         print(l, r)
#         return nums[l]
#         # return min(nums[l], nums[r])
        
        
        
        ####################33
        
        
        
        # we have to move towards the pivot
        # since the array was sorted in ascending, that means we can use the right pointer
        #  to determine which partition the pivot is inside
        # if middle > right, then the pivot is for sure somewhere in the right partition
        
#         l, r = 0, len(nums)-1
        
#         # for every iteration, as long as middle is less than the right, then we bring right down to middle
#         #  otherwise, bring left up to middle
#         while l < r:
#             mid = l + (r - l) // 2
#             if nums[r] > nums[mid]: # since right > mid, right partition is sorted and we know the pivot is in left partition
#                 r = mid
#             else:                   # since right < mid, we know hte pivot is in hte right partition
#                 l = mid + 1         # we do +1 here because else is checking for equality as well (since original conditional wasn't checking for equality)
        
#         return nums[l]