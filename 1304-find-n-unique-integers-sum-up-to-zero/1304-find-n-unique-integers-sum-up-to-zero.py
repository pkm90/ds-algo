class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ###############
        
        
        # if they just have to add up to 0, then we can add their complements
        # if n is odd then we can add 0
        res = []
        for i in range(1, (n // 2) + 1):
            res.append(i)
            res.append(-i)
        if n % 2 != 0:
            res.append(0)
        return res
        
        
        #################
        
        
#         # if even, do same number with positive and negative
#         # if odd, append 0

#         # cannot append 0 and -0, so we add 1 since we are taking the i'th value and -i'th value
#         # max number of iterations are modified cause we want to
#         # use i as what we are appending so run it for half as many iterations
#         res = []
#         for i in range(1, n//2 + 1): 
#             res.append(i)
#             res.append(-i)
#         if n % 2 != 0:
#             res.append(0)
#         return res