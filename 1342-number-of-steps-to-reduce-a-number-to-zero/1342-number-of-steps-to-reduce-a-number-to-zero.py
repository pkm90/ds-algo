class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        
        # can do math for this,
        # if num is even then return itself divided by two
        # if it is odd, return itself divided by two + 1
        
        res = 0
        while num != 0:
            res += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
        return res
    
        # if num % 2 == 0:
        #     return num / 2
        # else:
        #     return (num / 2) + 1