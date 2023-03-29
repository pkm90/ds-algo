class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        # time:  o(n)
        # space: o(n)
        
        # first idea was to create a function valid() and do things that way
        # check if substring of each substring is valid, solve smaller problem
        # base case is if there is only one string/char
        # if we reach base case, then append the string maybe...?
        
        # this doesn't currently work, can use as recursive practice
        def isValidSubstring(start, end):
            if start == end:
                # print("found")
                return True
            
            # if valid, do same on all subchar
            # print(start, end)
            # print(s[start], s[end])
            if finalChar[s[start]] <= finalChar[s[end]]:
                # print("true")
                return isValidSubstring(start + 1, end)
            else:
                return False
            
        finalChar = {}
        n = len(s)
        for i in range(n):
            finalChar[s[i]] = i
        print(finalChar)
            
        parts = []
        first = 0
        last = finalChar[s[0]]
        i = 0
        while i < len(s):
        # for i in range(n):
            # print(i)
            # first = i
            last = finalChar[s[i]]
            # print("checking: ", first, last, s[first:last + 1])
            if isValidSubstring(first, last):
                parts.append(s[first:last + 1])
                i = last + 1
                first = i
            else:
                i += 1

        print(parts)
        res = []
        for part in parts:
            res.append(len(part))
        print(res)
        return res
        
        
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

    
        