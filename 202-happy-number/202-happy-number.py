class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        visit = set()
        while n != 1:
            if n in visit:
                return  False
            visit.add(n)
            
            total = 0
            while n != 0:
                digit = n % 10
                total += digit**2 # can't use carrot, must use **
                n = n // 10
            n = total
        
        return True