class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        if len(s) == 0:
            return 0
        l = 0
        res = 1
        window = []
        window.append(s[l])
        
        for r in range(1,len(s)):
            #         r
            # a b c a a
            # a         1
            # a b       2
            # a b c     3
            #   b c a   3
            #         a 3
            
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.append(s[r])
            res = max(res, len(window))
            
        return res
            