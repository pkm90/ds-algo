class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total < target:
                l += 1
            else:
                r -= 1
        
        
        
        
        
        ##################
        
#         # can do it same as previous, but since it's sorted let's use two pointer
#         # two pointer
#         l, r = 0, len(numbers)-1
        
#         while l < r:
#             total = numbers[l] + numbers[r]
#             if total == target:
#                 return [l+1, r+1]
            
#             if total < target:
#                 l += 1
#             else:
#                 r -= 1
#         return None # gauranteed to be a solution so we don't have to do this