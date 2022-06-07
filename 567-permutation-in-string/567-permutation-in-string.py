# do again...

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         return "Nothing"
#         print('asfd')
        
        ###########################
        l = 0
        requirements = Counter(s1)
        contents = Counter(s2[0:len(s1)])
        
        if requirements == contents:
            return True
        for r in range(len(s1), len(s2), 1):
            contents[s2[l]] -= 1
            contents[s2[r]] += 1
            l += 1

            if requirements == contents:
                return True
        
        return False
        
        
        #####################################
        
#         req = Counter(s1)
#         contents = {}
#         n = len(s2)
#         l = 0
        
#         def invalid():
#             for key, value in contents.items():
#                 if key not in req or value > req[key]:
#                     return True
#             return False
        
#         for r in range(n):
#             val = s2[r]
#             contents[val] = contents.get(val, 0) + 1
            
#             while l <= r and invalid():
#                 contents[s2[l]] -= 1
#                 if contents[s2[l]] == 0:
#                     del contents[s2[l]]
#                 l += 1
                        
#             if sum(contents.values()) >= sum(req.values()):
#                 print(contents)
#                 print(req)
#                 return True
                
#         print(contents)
#         print(req)
#         return False
        
        