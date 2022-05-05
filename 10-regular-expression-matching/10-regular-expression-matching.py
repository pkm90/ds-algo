class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        
#         # 150
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
            print(sdx, pdx)
            if sdx >= len(s) and pdx >= len(p):
                return True
            if pdx >= len(p): # if we have no more pattern but more string
                return False
            
            # # still have string, there's a match, next pattern isn't *
            # if (sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == ".") and (pdx + 1 < len(p) and p[pdx + 1] != "*")):
            #     # match = True
            #     match = dfs(sdx + 1, pdx + 1)
            # else:
            #     match = False
            
                
            # match = sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == ".")
            
            match = False
            if (pdx + 1 < len(p) and p[pdx + 1] == "*"):# if next has a star, check possibilities
                if sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == "."):
                    match = dfs(sdx + 1, pdx)             # adding the char, only if current is matching
                # match = match and dfs(sdx + 1, pdx)     # adding the char, only if current is matching
                match = match or dfs(sdx, pdx + 2)      # not adding the char  
                return match
                # match = dfs(sdx, pdx + 2) or (match and dfs(sdx + 1, pdx))
            
            # we've gone through the case when next is *
            # this is if we have a match and next isn't *
            if sdx < len(s) and (s[sdx] == p[pdx] or p[pdx] == "."):
                match = dfs(sdx + 1, pdx + 1)
            return match
        
        
            # if match:
            #     match = dfs(sdx + 1, pdx + 1)
            return match
                
            
            # if s[sdx] == p[pdx] or p[pdx] == ".":
            #     match = match or dfs(sdx + 1, pdx + 1)
            # if match:
            #     match = match or dfs(sdx + 1, pdx + 1)
            
            return match
        
        return dfs(0, 0)
                
            
            
            
            