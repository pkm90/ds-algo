# do again, good practice for strings

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        

        
        
        

        
        # 115
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
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      