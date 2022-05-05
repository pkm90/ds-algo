# good problem!
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        
        # kinda like 2 sum but have to find max number of pairs
        # numbers that match each other are unique combinations
        # we can keep track of how many times a number exists and is used
        # iterate through array, if we use a number then increment it's counter
        # never use more numbers than exists
        
        res = 0
        choices = Counter(nums)
        for choice, count in choices.items():
            choices[choice] = [0, count] # [used, max we can use]
        print(choices)
            
        for num in nums:
            diff = k - num
            if (diff in choices 
                and choices[diff][0] < choices[diff][1]
                and choices[num][0] < choices[num][1]):
                choices[diff][0] += 1
                choices[num][0] += 1
                res += 1
                    
            # this catches the case where num and diff are the same and we exceed max
            # it catches that case and fixes it
            if diff == num and choices[diff][0] > choices[diff][1]:
                choices[diff][0] -= 1
                res -= 1
                
        return res
    
    
    #######################
    
    
        # we can sort the input and use 2 ptr
        # each time k is found then we increase count and iterate both left and right
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            pair = nums[l] + nums[r]
            if pair == k:
                l += 1
                r -= 1
                res += 1
            elif pair < k:
                l += 1
            elif pair > k:
                r -= 1
        
        return res
    
    
    