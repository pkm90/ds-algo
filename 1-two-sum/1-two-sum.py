class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        
        
        
        
        # bruteforce
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return (i, j)
            
        # bruteforce, 2ptrs and sort, hashmap
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i, j]
        
        
        # prevMap = {}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in prevMap:
        #         return[i, prevMap[diff]]
        #     prevMap[num] = i
                
#         # 2 ptrs
#         # not sure if this is gonna work, can't sort it
#         # we can sort it, but have to keep track of original indexes which is hassle
#         # time: nlogn
#         # space: 1
        
#         l, r = 0, len(nums)-1
#         sorted(nums)
#         while l < r:
#             total = nums[l] + nums[r]
#             if total == target:
#                 return [l, r]
#             if total > target:
#                 l += 1
#             else:
#                 r -= 1
#         return None
        
        # # hashmap
        # # time: n
        # # space: n
        # memo = {}
        # for i, num1 in enumerate(nums):
        #     num2 = target - num1
        #     if num2 in memo:
        #         return [memo[num2], i]
        #     memo[num1] = i