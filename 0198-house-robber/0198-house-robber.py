########
## this is a great problem to see how dp is logged in recursion, run below to see:
########
# # this question gave me lots of trouble to figure out, try again on own
# # general thought process was correct, but I tried to store the outputs inside variables
# # this is a problem for two reasons:
# #  first reason: the output for a specific state changed so the returns during one state would mess with another state
# #   instead of storing the variables/outputs, I can simply return the entire max
# #   I still need practice with thinking abotu things this way and understanding that
# #   I don't need to store the variables:
#         def robbing(houses):
#             if len(houses)<=0:
#                 return 0

#             h1 = houses[0] + robbing(houses[2:])
#             h2 = robbing(houses[1:])
#             return max(h1, h2)
#         maxrob = robbing(nums)
#         return maxrob
# # second reason: above solution works but there is needless computation, and a hashmap can store the work
# # we just need:
# # - a good way to store the state as a key inside a hashmap and how to differentiate keys, only immutable types can be keys: integer, float, string, or Boolean 
# # - understand the value we are storing, in this case we are storing the max that we can rob at any state
# # - when to store/retrieve:
#         dp = {}
        
#         def robbing(houses):
#             if str(houses) in dp:
#                 return dp[str(houses)]
#             if len(houses)<=0:
#                 return 0

#             h1 = houses[0] + robbing(houses[2:])
#             h2 = robbing(houses[1:])
#             dp[str(houses)] = max(h1, h2)
#             return dp[str(houses)]

#         maxrob = robbing(nums)
#         return maxrob    
    
    
#     def rob(self, nums: List[int]) -> int:
#         # we want to maximize amount of money stolen
#         # we can think about problem like this:
#         # recurrence relation: either we rob the first house and get the max of the rest (minus second), or we skip the first house and get the max of everything (minus first)
#         #  rob = max( arr[0] + rob[2:n] , rob[1:n] )
#         #  result of entire problem depends on the two parameters inside above max function
#         #  each rob can be broken up into subproblems of their own 
#         # 
#         # we can think of it as two options:
#         #  either we steal the first option and skip second
#         #  or we steal second option and skip first
#         # we repeat this until there are no more houses left
#         # this way, we only  need ot keep track of two variables...totals of robbing first and second houses
        
#         dp = {}
        
#         def robbing(houses):
#             if str(houses) in dp:
#                 return dp[str(houses)]
#             if len(houses)<=0:
#                 return 0
            
#             h1 = houses[0] + robbing(houses[2:])
#             h2 = robbing(houses[1:])
#             dp[str(houses)] = max(h1, h2)
#             print('new dp  ', dp)
#             return dp[str(houses)]

#         maxrob = robbing(nums)
#         print('final dp', dp)
#         return maxrob
    
class Solution:
    def rob(self, nums: List[int]) -> int:        
        # we will have the following variables: house1, house2, storage
        # we only need the totals from last two houses to compute max of current house
        #  so we take the max(current + first, second) and store it, we're done with this iteration
        #   but...in the next iteration, the house1 and house2 will be different.
        #   house1 grabbed the current loot, so in the next iteration it needs to be house2
        #   likewise, house2 didn't grab the current loot so it will become the new house1
        #   regardless of if the current loot was max, in the next iteration house2 will
        #   be the new house1 since only it can grab the loot so we have to swap the variables
        #   house1 = house2
        #   house2 = max of itself or house1+loot
        # now in the next iteration, we again only need totals from last two houses
        # so we do the same thing, max(current + first, second)
        # first = current + first
        # ...
        
        house1, house2, storage = 0, 0, 0
        # we only need to know the loot from last two houses to figure out what max of current can be
        # [house1, house2, n, n+1, ...]
        for n in nums:
            storage = max(n + house1, house2) # we store the max from current and totals from last two houses 
            house1 = house2 # we swap the houses since the next iteration, house2 will be valid to grab loot
            house2 = storage # we store the max of our current loot into house2 variable
       
        return house2 # return house2, since it stores the max of current+house1 and house2 at that iteration
    