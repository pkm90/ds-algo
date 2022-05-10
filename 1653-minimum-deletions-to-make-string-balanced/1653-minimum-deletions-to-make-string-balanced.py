# finished but don't fully understand solution,
# same as https://leetcode.com/problems/flip-string-to-monotone-increasing/submissions/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        
        
        
        
        # prefix sums -.-
        # find how many need to be flipped before current
        # find how many need to be flipped after current
        # return the min of sum of both
        
        prefixA, prefixB = [], [0]
        countA, countB = 0, 0
        minSwaps = float(inf)
        
        for char in s:
            if char == 'b':
                countB += 1
            prefixB.append(countB)
            
        for char in s[::-1]:
            if char == 'a':
                countA += 1
            prefixA.append(countA)
        
        prefixA.reverse()
        prefixA.append(0)
        # print(prefixA)
        # print(prefixB)
        
        for i in range(len(prefixA)):
            minSwaps = min(minSwaps, prefixB[i] + prefixA[i])
        
        return minSwaps
        
        
        # tried dfs and bfs bruteforce, off by one error not gonna debug
#         minSwaps = [float(inf)]
#         visit = set()
#         def dfs(swaps, front):
#             print(front)
#             back = front[::-1]
#             if (swaps, str(front)) in visit:
#                 return
#             visit.add((swaps, str(front)))
#             if 'a' not in front or 'b' not in front:
#                 if swaps == 0: minSwaps[0] = 0
#                 return
#             if minSwaps[0] == 0:
#                 return
#             # checks if string is balanced
#             # print(front.index('b'), (len(back) - back.index('a')))
#             if front.index('b') > (len(back) - back.index('a') - 1):
#                 print(swaps)
#                 minSwaps[0] = min(minSwaps[0], swaps)
#                 return
            
#             # try the first b
#             dfs(swaps + 1, front[:front.index('b')] + front[front.index('b') + 1:])
            
#             # try the last a
#             lastA = len(back) - back.index('a') - 1
#             dfs(swaps + 1, front[:lastA] + front[lastA + 1:])
        
#         dfs(0, list(s))
#         return minSwaps[0] if minSwaps[0] != float(inf) else 0
    
    
#         minSwaps = [float(inf)]
#         q = collections.deque()
#         q.append((0, list(s)))
#         visit = set()
        
#         while q:
#             swaps, front = q.popleft()
#             back = front[::-1]
#             if (swaps, str(front)) in visit:
#                 continue
#             visit.add((swaps, str(front)))
#             # print(swaps, front)
#             if 'a' not in front or 'b' not in front:
#                 continue
#             if minSwaps[0] == 0:
#                 continue
#             # checks if string is balanced
#             # print(front.index('b'), (len(back) - back.index('a')))
#             if front.index('b') > (len(back) - back.index('a') - 1):
#                 # print(swaps)
#                 minSwaps[0] = min(minSwaps[0], swaps)
#                 continue
            
#             # try first b
#             q.append((swaps + 1, front[:front.index('b')] + front[front.index('b') + 1:]))
            
#             # try the last a
#             lastA = len(back) - back.index('a') - 1
#             q.append((swaps + 1, front[:lastA] + front[lastA + 1:]))
            
        # return minSwaps[0] if minSwaps[0] != float(inf) else 0


            