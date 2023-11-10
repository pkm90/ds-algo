class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

        # time: o(n^2)
        # space: o(1)
        
#         # go through each element one by one
#         for firstNumber in range(0, len(nums), 1): # start, stop, step
#             # print(nums[i])
            
#         # for every other element, see if it exists
#             for secondNumber in range(firstNumber + 1, len(nums), 1):
#                 if nums[i] == nums[j]:
#                     return True
        
#         return False

    
        
        # create hashset
        storage = set()
        
        # go through each element
        for num in nums:
            # check if exists, otherwise add
            if num in storage:
                return True
            storage.add(num)
            
        return False

        



