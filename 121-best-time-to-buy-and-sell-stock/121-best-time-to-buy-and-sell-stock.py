class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        
        
        
        
        
#         # bruteforce
#         n = len(prices)
#         res = 0
#         for left in range(n):
#             for right in range(left + 1, n):
#                 res = max(res, prices[right] - prices[left])
#         return res
        
        
        # we need to calculate the max profit between any two days 
        # iterate through prices, keep track of minprice,
        # and update result: current - minprice
        res = 0
        minPrice = float(inf)
        for price in prices:
            res = max(res, price - minPrice)
            minPrice = min(minPrice, price)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # 2ptrs, keep track of min and maxprofit, return maxprofit
#         small = float(inf)
#         maxprofit = 0
#         for price in prices:
#             small = min(small, price)
#             maxprofit = max(maxprofit, price - small)
            
#         return maxprofit
        
        
        ############
        
#         # sliding window?
#         # just iterate?
#         # time: n
#         # space: 1
        
#         # originally kept track of max, but we don't even need that...see below"
        
#         big, small, maxprofit = float(-inf), float(inf), 0
        
#         for price in prices:
#             if price < small:
#                 small = price
#             maxprofit = max(price - small, maxprofit)
        
#         return maxprofit
    
