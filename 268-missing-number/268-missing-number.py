class Solution:
    def missingNumber(self, nums):
#         missing = len(nums)
#         missing = 4
#         print(missing)
#         print('------')
#         for i, num in enumerate(nums):
#             missing ^= i ^ num
#             # print(missing)
#             # missing = missing ^ i ^ num
#             print(missing)
#             # print(i, num, missing)
#         return missing
    
#     ## wtf???
    
    
        total = sum(nums)
        other = 0
        for num in range(len(nums) + 1):
            other += num
        return other - total