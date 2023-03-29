class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        
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
                start = end + 1
        
        res = []
        for part in parts:
            res.append(len(part))
            
        # print(parts)
        return res
        
        # given a string
        # find first and last occurences of the first char
        # a: [0,2,7,9]

    
#     start = 0
#     iterate through string:
  
#           keep track of largest idx of previous chars
#   if i == largest:
#     parts.append(input[start:largest])
#     set/reset start


    
        