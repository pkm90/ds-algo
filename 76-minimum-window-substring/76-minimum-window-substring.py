class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        
        # we can count the contents of a sliding window
        # while it is valid, make it smaller until it is invalid
        # return the smallest valid window
        
        if len(t) > len(s):
            return ''
        
        reqs = Counter(t)
        contents = {}
        res = [float(inf), float(inf), float(inf)]
        l = 0
        
        def valid():
            # print('inside')
            for key, val in reqs.items():
                if key not in contents or contents[key] < val:
                    return False
            return True
        
        for r in range(len(s)):
            val = s[r]
            contents[val] = contents.get(val, 0) + 1
            # print(contents)
            
            while valid():
                if r - l < res[0]:
                    res = [r - l, l, r]
                    # print(s[l:r + 1])
                # print(s[l:r + 1])
                contents[s[l]] -= 1
                l += 1
        
        return s[res[1]:res[2] + 1] if res[0] != float(inf) else ''
        
        