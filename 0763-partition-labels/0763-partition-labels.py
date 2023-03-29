class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        # time:  o(n)
        # space: o(n)
        
        # first idea was to create a function valid() and do things that way
        
        # mark's idea:
        # keep track of last occurence of char
        # if i == largest occurence of seen char
        #    we found a valid substring
        
        
        # track last indice of each char        
        finalChar = {}
        n = len(s)
        for i in range(n):
            finalChar[s[i]] = i
        
        # iterate through input, do stuff
        parts = []
        start = 0
        end = -inf
        for i in range(n):
            char = s[i]
            end = max(end, finalChar[char])
            
            if i == end:
                parts.append(s[start:end + 1])
                # parts.append(end - start + 1)
                start = end + 1
                
        # return parts
        
        res = []
        for part in parts:
            res.append(len(part))
            
        print(parts)
        return res

    
        