class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        
#         # 90 min, used lots of help
#         # if we simply wanted to check if p matches s then we can iterate and make sure both match
#         # if we end up oob but somehting still has more then false
#         if len(s) != len(p):
#             return False
#         for idx in range(len(s)):
#             if s[idx] != p[idx]:
#                 return False
#         return True
    
    
#         # to add the wildcard, we can simply go to the next iteration without checking
#         if len(s) != len(p):
#             return False
#         for idx in range(len(s)):
#             if p[idx] == '.':
#                 continue
#             if s[idx] != p[idx]:
#                 return False
#         return True
    
        # to add the star, we need to see if any combination of previous char from 0 to inf can fit
        # length of pattern or string can be greater than other: aaa:a*, a:aa*
        # we will have the wildcard but add extra conditionals
        #  if next char is a *, then we dfs on all possibilities until idx is greater either word
        #   we will try adding the char, and try not adding the char
        #  if idx of both are out of range at the same time, then we found a match
        
        def dfs(sdx, pdx):
            # print(sdx, pdx)
            if (sdx, pdx) in memo:
                return memo[(sdx, pdx)]
            if sdx >= len(s) and pdx >= len(p):
                return True
            if pdx >= len(p): # if we have no more pattern but more string
                return False
            
            # case when next is *
            if (pdx + 1 < len(p) and p[pdx + 1] == "*"):                 # if next has a star, check possibilities
                addChar = False
                if sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == "."): # adding the char if current is matching
                    addChar = dfs(sdx + 1, pdx)
                if addChar is False:                                     # adding char doesn't work, try skipping char
                    skipChar = dfs(sdx, pdx + 2)
                memo[(sdx, pdx)] = addChar or skipChar
                return memo[(sdx, pdx)]
            
            # case when next isn't *
            if sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == "."):
                memo[(sdx, pdx)] = dfs(sdx + 1, pdx + 1)
                return memo[(sdx, pdx)]
            
            # if next isn't a star, and current doesn't match, then return False
            return False
        
        memo = {}        
        return dfs(0, 0)
    
    
            