class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        
        
        
        
        
        
        # we can try some arbitrary number
        # if she finishes then we can try a lower number
        # keep trying until we find the number right above a failure
        
        # bruteforce, we try numbers and iterate one by one
#         res = float(inf)
#         def eatBananas(vel, hours):
#             for pile in piles:
#                 hours += math.ceil(pile / vel)
#             return hours
                
#         for speed in range(1, max(piles) + 1, 1):
#             hours = eatBananas(vel = speed, hours = 0)
#             if hours <= h:
#                 res = min(res, speed)
#             if res < float(inf):
#                 return res
#         return res
        
        
        # optimize using binary search
        res = float(inf)
        l, r = 1, max(piles) + 1
        
        while l < r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
                
            if time <= h:
                r = mid
                # res = min(res, mid)
            else:
                l = mid + 1
        
        # print(l, res)
        return l # since l is hte smallest number that matches hte condition
        
        
        