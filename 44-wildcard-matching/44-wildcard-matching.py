class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        
#         # if we only have ?
#         def dfs(sdx, pdx):
#             if sdx >= len(s) and pdx >= len(p):
#                 return True
#             if sdx >= len(s) or pdx >= len(p):
#                 return False
            
#             if s[sdx] == p[pdx] or p[pdx] == "?":
#                 return dfs(sdx + 1, pdx + 1)
#             return False
        
#         memo = {}
#         return dfs(0, 0)
    
        # to add the * functionality
        # we need to try using the * and not using the *
        # ran into tle, added memo
        def dfs(sdx, pdx):
            if (sdx, pdx) in memo:
                return memo[(sdx, pdx)]
            if sdx >= len(s) and pdx >= len(p):
                return True
            if sdx >= len(s) or pdx >= len(p):
                if pdx < len(p):                   # checks if rest in pattern is *
                    # return all( "*" == char for char in p[pdx:])
                    for char in p[pdx:]:
                        if char != "*":
                            return False
                    return True
                return False
            
            if p[pdx] == "*":
                match = dfs(sdx + 1, pdx)          # use the star
                match = match or dfs(sdx, pdx + 1) # don't use the star
                memo[(sdx, pdx)] = match
                return match
            
            if s[sdx] == p[pdx] or p[pdx] == "?":
                memo[(sdx, pdx)] = dfs(sdx + 1, pdx + 1)
                return memo[(sdx, pdx)]
            
            return False
        
        memo = {}
        return dfs(0, 0)
            
            
    #####################        
        
        
#         # solution worked for bunch of test cases but failed in the following, looking up solution now:
#         # ""
#         # "******"
#         # "mississippi"
#         # "m??*ss*?i*pi"
        
#         # pattern must match string, p must match s
#         # s is all lowercase
#         # p is all lowercase + ? + *
#         # if we find a ?, move to next iteration
#         # elif we find a *, try all subsequences that match next char (if no next char, return True?)
#         # elif the char[p] != char[s], return False
        
#         # if len(s) == 0: return True
        
#         def check(si, pi):
#             # base, if we reach end of one then return True/False depending on situation
#             if len(s) == si or len(p) == pi:
#                 print('inside', si, pi)
#                 for char in p[pi:]:    # if p has characters leftover, check to make sure they're *
#                     if char != '*':
#                         return False
#                     else:
#                         return True
#                 return len(s) == si and len(p) == pi
            
#             if p[pi] == '?':
#                 # match = check(si + 1, pi + 1)
#                 if check(si + 1, pi + 1):
#                     return True
#             elif p[pi] == '*':
#                 # recurse all subsequences that match next char
#                 if len(p) == pi + 1: # checks if star is the last char
#                     return True
#                 for i, char in enumerate(s[si:]): # recurses all subsequences that match next char
#                     # print('looping', i, char)
#                     if p[pi + 1] == '?' or p[pi + 1] == '*': # checks if next character is ? or star
#                         if check(si + i, pi + 1):
#                             return True
#                     elif char == p[pi + 1]: # if next char isn't ? then check all subseq that match next char
#                         if check(si + i, pi + 1):
#                             return True
#             elif p[pi] != s[si]:
#                 return False
#             else:
#                 if check(si + 1, pi + 1):
#                     return True
            
#             # if we get this far without getting a True returned, then return False
#             return False
        
#         res = check(0, 0)
#         return res
    
