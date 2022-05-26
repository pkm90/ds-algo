# keep doing...

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        
          
        
        
        
        

        
#         # bruteforce approach
#         res = set()
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         combo = (nums[i], nums[j], nums[k])
#                         sorted(combo)
#                         res.add(combo)
#         return res
                   
        
        nums.sort()
        res = []
        n = len(nums)
        seen = {}
        
        print(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
###################


#         # sum 3 numbers so that they equal 0
#         # if we sort this then we can solve it kinda like 2 sum
#         # we will have to have one iteration going through, and then use 2 ptr
#         #  for each iteration of the original iteration...hard to explain, see below
#         #  where we initialized the l, r pointers
        
#         n = len(nums)        
#         nums.sort()
#         print(nums)
#         res = []
        
#         for i, num in enumerate(nums):
#             if (i > 0 and num == nums[i-1]):
#                 continue
            
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 total = num + nums[l] + nums[r]
#                 # print(total, i, l, r)
#                 if total < 0:
#                     l += 1
#                 elif total > 0:
#                     r -= 1
#                 else:
#                     # here we have to keep shifting one of the pointers until we get a unique value
#                     # only need to shift one of the pointers since other gets shifted in logic above
#                     res.append([num, nums[l], nums[r]])
#                     l += 1
#                     while (nums[l] == nums[l-1] and l < r):
#                         l += 1
#         print(res)
#         return res        
        