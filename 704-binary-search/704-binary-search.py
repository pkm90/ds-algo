class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ###################
        
        # trying out the template: https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template.-solved-many-problems
        
        l, r = 0, len(nums) # have to cover entire search space
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
                
        # if nums[l] == target:
        #     return l
        # return -1
        
        print(l)
        if nums[l - 1] == target: # since l is the minimal k that satisfies condition
            print('found')
            return l - 1
        
        return -1