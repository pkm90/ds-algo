class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        
        
        # 950
        
        # brute force would be to continue deleting windows of k until there are no changes, n^2 and 1
        # we can use a stack to help us and make this N and N
        #  store input inside stack, while current == prev, remove them if >= k
        #  reverse stack, join it, return it
        # stack gave tle
        
#         stack = []
#         for char in s:
#             storage = [char]
#             while stack and stack[-1] == char:
#                 storage.append(stack.pop())
#                 if len(storage) >= k:
#                     storage.clear()
#             stack.extend(storage)
        
#         return ''.join(stack)
    
        stack = []
        for char in s:
            # print(stack)
            if stack and stack[-1][1] == char:
                stack[-1][0] += 1
            else:
                stack.append([1, char])
            # stack.append(char)
            # print(all(c == char for c in stack[-k:]))
            while stack and stack[-1][0] >= k:
                stack.pop()
            # while (len(stack) >= k and all( c == char for c in stack[-k:] )):
                # print(stack)
                # del stack[-k:]
                # stack = stack[:len(stack) - k]
                # print(stack)
#                 storage.append(stack.pop())
#                 if len(storage) >= k:
#                     storage.clear()
#             stack.extend(storage)
        res = [ char[1] * char[0] for char in stack ]
        return ''.join(res)
        return ''.join(stack)