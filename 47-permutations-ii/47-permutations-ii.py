# do again until easy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        
        
        
        
        
        ##########################
        
        # backtrackting
        # keep track of the choices
        # go through possible choices if available  

        path, res = [], [] 
        n = len(nums)
        choices = Counter(nums)
        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            
            for key, value in choices.items():
                if value > 0:
                    choices[key] -= 1
                    path.append(key)
                    dfs()
                    choices[key] += 1
                    path.pop()
                    
        dfs()
        return res
            
    ##############################
        
        
#         # neetcode's
#         # use a hashmap to keep track of what's available
#         # iterate over keys of hashmap during the dfs so we avoid duplicates
#         def dfs(path):
#             if len(path) == len(nums):
#                 res.append(path.copy())
#                 return
            
#             for letter, available in choices.items():
#                 if available != 0:
#                     choices[letter] -= 1
#                     dfs(path + [letter])
#                     choices[letter] += 1
        
#         choices = Counter(nums)
#         print(choices)
#         res = []
#         dfs([])
#         return res
        
        
        
#         # main thing is that we need to avoid duplicate values
#         # we sort the list first and then skip any duplicates during permutation
#         def dfs(idx, choices, path):
#             # print(choices)
#             if len(choices) == 0:
#                 res.append(path.copy())
#                 return
        
#             for i in range(0, len(choices)):
#                 if i > 0 and choices[i] == choices[i - 1]:
#                     continue
#                 dfs(i, choices[:i] + choices[i + 1:], path + [choices[i]])
                
#         res = []
#         choices = sorted(nums.copy())
#         dfs(0, choices, [])
#         return res
        