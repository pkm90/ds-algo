class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        
        
        # 1220
        # sliding window with requirements, keep track of the largest window
        # extend window until string is happy
        #  while string is happy, check max window, continue to extend until it is unhappy
        
        
        # create variables
        res = [0, 0, 0] # [ left, right, size ]
        reqs = {'a': a, 'b': b, 'c': c}
        left = 0
        
        # sliding window
        
        
        # return
        
        
        # misundertsood question -- we have to make the longest happy string
        # I think we can be greedy, choose largest to append
        #  try to keep the choices close together, diff between them is < 1
        #  if diff is > 1, then append 2
        #  else append 1
        # 
        
        # smallest = min(a, b, c)
        # largest = max(a, b, c)
        choices = {'a': a, 'b': b, 'c': c}
#         reqs = [a, b, c]
#         smallest, largest = 0, 0
#         for i in range(reqs):
#             if reqs[i] < smallest:
#                 smallest = i
#             elif reqs[i] > largest:
#                 largest = i
        
#         largest = max(reqs, key = reqs.get)
        # smallest = 
        
        path = ['dummy', 'dummy']
        
        maxHeap = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(maxHeap)
        
        # q = collections.deque()
        # q.append(heapq.heappop(maxHeap))
        
#         while q:
            
#             for _ in range(1):
                
        
        # prev = len(path)
        # while maxHeap[2][0] > 0:
        while maxHeap:
            # print(maxHeap)
            count, char = heapq.heappop(maxHeap)
            # print(count, char)
            if count >= 0:
                continue
                
            # if we already used curr, then use mid
            if path[-1] == char and path[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                if count2 >= 0:
                    heapq.heappush(maxHeap, [count, char])
                    continue
                count2 += 1
                path.append(char2)
                heapq.heappush(maxHeap, [count2, char2])
            else:
                count += 1
                path.append(char)
            heapq.heappush(maxHeap, [count, char])
                
        return ''.join(path[2:])
    
#             # if diff > 1 for other 2, then append 2
#             if (curr[0] - maxHeap[0][0] > 1 or
#                 curr[0] - maxHeap[1][0] > 1 or
#                 curr[0] - maxHeap[2][0] > 1):
#                 curr[0] -= 2
#                 heapq.heapify(maxHeap)
#                 path.append(curr[1])
#                 path.append(curr[1])
#             else:
#                 curr[0] -= 1
#                 heapq.heapify(maxHeap)
#                 path.append(curr[1])
                
#         return ''.join(path[1:])
            
                
                
#         checkDiff():
#             max(maxHeap)
            
#             curr = heapq.heappop(maxHeap)
#             q.append(curr)
            
#         while q:
            
            
        
        
        
        
#         largest = max(choices)
#         smallest = min(choices)
#         mid = [ key for key in choices ]
#         mid.remove(largest)
#         mid.remove(smallest)
#         mid = mid[0]
        
#         def getOrder(a, b, c):
#             largest, smallest = a, a
#             if a < b:
#                 smallest, largest = a, b
#             else:
#                 smallest, largest = b, a
            
            
        
#         # for choice in [['a', a], ['b', b]]
        
#         def makeHappy(small, med, large, prev):
#             if choices['a'] == 0 and choices['b'] == 0 and choices['c'] == 0:
#             # if i == 0 and j == 0 k == 0:
#                 res.append(''.join(path[1:]))
            
#             if large == path[-1]:
#                 med, large = large, med
            
            
            
#             for key, val in choices.items():
#                 if largest - val > 1:
#                     choices[largest] -= 2
#                     path.append(largest)
#                     path.append(largest)
#                     makeHappy(largest)
#                     return
#             choices[largest] -= 1
#             path.append(largest)
#             makeHappy()
        
        
        