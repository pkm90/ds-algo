class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        # time:  o(n)
        # space: o(n)
        
        # first idea was to create a function valid() and do things that way
        # check if substring of each substring is valid, solve smaller problem
        # base case is if there is only one string/char
        # if we reach base case, then append the string maybe...?
        # both of below work
            
            
        # for some given substring
        # this will check if all subchar are within the last index of given char
        def isValidSubstring(start, end):
            if start == end:
                return True
            
            # if valid, do same on all subchar
            if finalChar[s[start]] <= finalChar[s[end]]:
                return isValidSubstring(start + 1, end)
            else:
                return False
            
        # creating hashmap of last indices
        finalChar = {}
        for i in range(len(s)):
            finalChar[s[i]] = i
        print(finalChar)
        
        parts = []
        first = 0
        last = finalChar[s[0]]
        i = 0
        while i < len(s):
            last = finalChar[s[i]]
            # print("checking: ", first, last, s[first:last + 1])
            # if valid, set i to skip used substr and reset beginning of next substr
            if isValidSubstring(first, last):
                parts.append(s[first:last + 1])
                i = last + 1
                first = i
            else:
                i += 1

        res = []
        for part in parts:
            res.append(len(part))
        
        print(parts)
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

    
        