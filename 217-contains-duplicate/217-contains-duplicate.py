class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        
        # # can sort it and check if any elements are the same
        # # time: nlogn
        # # space: n if we count the space required to sort, otherwise 1
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False
    
#         # can use hashmap and add elements
#         # time: n
#         # space: n
#         visit = set()
#         for num in nums:
#             if num in visit:
#                 return True
#             visit.add(num)
#         return False
        
        # can put the input into a set and check length
        temp = set(nums)
        if len(temp) == len(nums):
            return False
        return True
        
        #################
        
#         # hashmap, iterate and add elements
#         # if an element exists, return True
#         # time: n
#         # space: n
        
#         visited = set()
#         for i in nums:
#             if i in visited:
#                 return True
#             visited.add(i)
            
#         return False
    
        # alternatively, sort and search
        # time: nlogn
        # space: 1 if we're modifying original array, else n
        
        # can heapify it and pop elements until there are no more...if any two elements are same then ...