class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        
        
#         # 40 min :(
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ######################
    
    
#         # brute force would be to continue deleting windows of k until there are no changes, n^2 and 1
#         # we can use a stack to help us and make this N and N
#         #  store input inside stack, while current == prev, remove them if >= k
#         #  reverse stack, join it, return it
#         # stack gave tle
        
#         stack = []
#         for char in s:
#             storage = [char]
#             while stack and stack[-1] == char:
#                 storage.append(stack.pop())
#                 if len(storage) >= k:
#                     storage.clear()
#             stack.extend(storage)
        
#         return ''.join(stack)
    
    
#         # this still gives tle since the all() checks for everything up to -k
#         stack = []
#         for char in s:
#             stack.append(char)
#             while (len(stack) >= k and all( c == char for c in stack[-k:] )):
#                 del stack[-k:]
#                 # stack = stack[:len(stack) - k]
#         return ''.join(stack)
    
    
        # this passed, we stored and incremented the last character
        # finally we recreated res and returned it
        stack = []
        for char in s:
            if stack and stack[-1][1] == char:
                stack[-1][0] += 1
            else:
                stack.append([1, char])

            while stack and stack[-1][0] >= k:
                stack.pop()

        res = [ char[1] * char[0] for char in stack ]
        return ''.join(res)
