class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        # beautiful solution: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/821099/Two-Pointers-PythonC%2B%2B-O(N)-Time-O(1)-Space
        # below solution based on it
        
        res = 0
        left, right = 0, 0                
    
        # find the violating left and right
        # then we extend it until it numbers are within the min and max range
        for l in range(1, len(nums)):
            if nums[l - 1] > nums[l]:
                left = l - 1
                print(left)
                break
        for r in range(len(nums) - 2, -1, -1):
            if nums[r] > nums[r + 1]:
                right = r + 1
                print(right)
                break
                
        windowMin = min(nums[left:right + 1])
        windowMax = max(nums[left:right + 1])
        print(windowMin, windowMax)
        
        while left > 0 and windowMin < nums[left - 1]:
            left -= 1
        while right < len(nums) - 1 and windowMax > nums[right + 1]:
            right += 1
                
        # edgecase for sorted inputs
        if right == left:
            return 0
        res = right - left + 1
        print(res)
        return res