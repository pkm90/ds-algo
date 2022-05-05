# do again, good practice for strings

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        

        
        
        

        ################
        
        
        # 40 min
        # to start off, how does a dictionary work?
        # we go based off of the words...
        #  for each two adjacent words, the first differing char tells us that
        #  the first word's diff char comes before the next word's differing char
        # the for two adjacent words, if there are no differing char then the
        #  second word must be shorter
        # we can go through the input and create the adj list while checking if the words are valid
        # if all the words are valid then we can do top sort and return the result of it
        #  after the top sort, we should have all char in the visit set otherwise we have a cycle
        
        # create variables 
        adj = { char:[] for word in words for char in word }
        indegree = { char:0 for char in adj.keys() }
        visit = set()
        q = collections.deque()
        res = []
        
        # populate variables and check for validity
        for idx in range(len(words) - 1):
            w1, w2 = words[idx], words[idx + 1]
            wordLen = min(len(w1), len(w2))
           
            if (w1[:wordLen] == w2[:wordLen]    # checks one of the validity conditions 
                and len(w2) < len(w1)): 
                return ""
            
            for jdx in range(wordLen):          # finds first differing char, populate adj and indegree
                if w1[jdx] != w2[jdx]:
                    adj[w1[jdx]].append(w2[jdx])
                    indegree[w2[jdx]] += 1
                    break
        
        for char, value in indegree.items():
            if value == 0:
                q.append(char)
        
        # sanity checks
        print(adj)
        print(indegree)
        print(q)
        
        # top sort
        while q:
            curr = q.popleft()
            if curr in visit:
                continue
            visit.add(curr)
            
            res.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        print(len(visit), len(adj))
        # make sure no cycles
        return ''.join(res) if len(visit) == len(adj) else ""
        
        
        
        ###############
        
        
#         # we are given an actual alien dictionary
#         # return needs to have all the unique letters of the alien langauge, sorted in lexicographical order
        
#         # only way we can tell if a char is earlier is where the first letter of hte first and next words differ
#         # if they have hte same prefix and first word isn't smaller in length then dict is invalid
        
#         # we need to keep track of which letters come before others, adj list can work here
#         adj = {}
#         for word in words:
#             for char in word:
#                 adj[char] = []
                
#         # now we need to populate this, go through each word and find the first differing char
#         # the w1 comes before w2, kinda like a prerequisite/requirement
#         for i in range(len(words) - 1): # -1 since we're grabbing i and i + 1, avoids index oob
#             w1, w2 = words[i], words[i + 1]
#             minLen = min(len(w1), len(w2))
#             if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
#                 return ""
            
#             for j in range(minLen):
#                 if w1[j] != w2[j]:
#                     adj[w1[j]].append(w2[j])
#                     break
        
#         # we need to know which characters don't have prereqs, we can count number of indegrees for this
#         indegree = { char: 0  for word in words for char in word }
#         for pre, chars in adj.items():
#             for char in chars:
#                 indegree[char] += 1
        
#         # we will add to result whenever there is a character with no requirements
#         # go through no req chars first and append their neighbors to queue
#         q = collections.deque()
#         for char, value in indegree.items():
#             if value == 0:
#                 q.append(char)
        
#         visit = set()
#         res = []
#         while q:
#             curr = q.popleft()
#             if curr in visit:
#                 continue
#             visit.add(curr)
            
#             res.append(curr)
#             for char in adj[curr]:
#                 indegree[char] -= 1
#                 if indegree[char] == 0:
#                     q.append(char)
                
#         # to check for cycle, we can compare visited number of total char
#         if len(visit) != len(adj.keys()):
#             return ''
#         else:
#             return ''.join(res)
        
        
        #########################
        
        
#         for word in words:
#             for char in words:
#                 # populate adj and indegree, same as below
#                 break
                
#         adj = { char: [] for word in words for char in word }
#         indegree = { char: 0 for word in words for char in word }
#         visit = set()
#         res = []
        
#         # creating adj list, checking for edgecase in prompt, populating empty indegree
#         for i in range(len(words) - 1):
#             w1, w2 = words[i], words[i + 1]
#             minLen = min(len(w1), len(w2))
            
#             # this is the edgecase they mentioned, ape must come before apes
#             if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
#                 print('inside')
#                 return ""
#             # this finds the first differing char
#             for j in range(minLen):
#                 if w1[j] != w2[j]:
#                     adj[w1[j]] = adj.get(w1[j], []) + [w2[j]]
#                     adj[w2[j]] = adj.get(w2[j], [])
#                     indegree[w1[j]] = indegree.get(w1[j], 0)
#                     indegree[w2[j]] = indegree.get(w2[j], 0)
#                     break
                    

#         # creating the indegrees and adding to queue
#         for key in adj:
#             for nei in adj[key]:
#                 indegree[nei] += 1
            
#         q = collections.deque()
#         for key, value in indegree.items():
#             if value == 0:
#                 q.append(key)
                    
#         print(adj)
#         print(indegree)
#         print(q)
        
#         while q:
#             curr = q.popleft()
#             if curr in visit:
#                 continue
#             visit.add(curr)
#             res.append(curr)
            
#             for nei in adj[curr]:
#                 indegree[nei] -= 1
#                 if indegree[nei] == 0:
#                     q.append(nei)

#         # we have to make sure that all characters are accounted for in the result
#         #  to do this, we check the length of result and length of indegree/adj
#         # if there are some letters that we didn't add to the result
#         #  then either we have an invalid input (maybe cycle) and return ''
#         return ''.join(res) if len(res) == len(indegree) else ''
    
    
    #########################
    
    # used below for some guidance
    
#         graph = {}
#         dependencyCount = {}

#         # add all possible values in graph
#         for word in words:
#             for char in word:
#                 graph[char] = []
#                 dependencyCount[char] = 0

#         # make our graph
#         for i in range(1, len(words)):
#             word1 = words[i-1]
#             word2 = words[i]
#             index = 0; length = min(len(word1),len(word2))
#             while index < length and word1[index] == word2[index]:
#                 index+=1

#             # you can use break and have a different loop but most interviewers don't like breaks
#             if index < length:
#                 graph[word1[index]].append(word2[index])
#                 dependencyCount[word2[index]]+=1

#         # figure out the staring point. The starting point has to be nodes that aren't dependent on someone else - hence the 0.
#         seed = [];
#         for key, val in dependencyCount.items():
#             if val == 0:
#                 seed.append(key)
#         result  = []
#         print(seed)
#         print(dependencyCount)
#         print(graph)
        
#         # Straight forward BFS
#         while len(seed) > 0:
#             curr = seed.pop(0)
#             result.append(curr)
#             for nei in graph[curr]:
#                 dependencyCount[nei] = dependencyCount[nei]  - 1
#                 if dependencyCount[nei] == 0:
#                     seed.append(nei)
#         print(result)
#         print(len(dependencyCount))
#          # It must have all the nodes in the graph
#         return ''.join(result) if len(result) == len(dependencyCount) else ''