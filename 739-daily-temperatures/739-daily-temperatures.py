class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        res = [0] * len(temperatures)
        
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                curr = stack.pop()
                res[curr[0]] = day - curr[0]
            stack.append((day, temp))
            
        return res
        
        
        
        ##################
        
        
        
#         # given some temps, return array with number of days until a warmer temp
        
#         # recursive solution (not tested)
#         # for each element, we will call a recursive helper function which will
#         # "search" for the next conditional temp and return it's step
#         # step is how many steps into the future we have taken
#         # basically:
#         # make a helper function that takes 3 parameters: list, temp, step
#         # base case: if len(list)==1, return 0
#         # if temp><list[0]: return helper(list[1:], temp, step+1)
#         # else: return step
        
#         # 2 pointer, iterative search, step is found by taking difference of index positions
        
#         # stack: the stack is a monotomically increasing/decreasing stack since we are removing 
#         # all elements that are greater/less than whatever position we are currently in
#         # so the stack becomes continuously increasing/decreasing...
#         # if stack contains nodes, then check the current with the stack and process until condition is no longer met
#         # for this question, we would pop nodes until the current is not greater than stack or stack is empty
#         # then we add the current to the stack and continue iterating
#         # basically:
#         # for each element, we compare it with the stack
#         # if condition, then we process which consists of checking temps and taking difference of index positions
#         # we add hte current element to the stack (value and index position, so we can calculate
#         # return the stored index differences
        
#         stack = []
#         res = [0]*len(temperatures)
#         for i, current in enumerate(temperatures):
#             while stack and current>stack[-1][1]:
#                 stackindex, stacktemp = stack.pop()
#                 res[stackindex] = i-stackindex
#             stack.append([i, current])
#         return res