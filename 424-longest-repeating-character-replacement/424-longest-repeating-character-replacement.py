class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        
        
        # iterate through s and keep track of contents within window
        # expand window while number of nondominant letters <= k
        # shrink window while number of nondominant letters > k
        contents = {}
        king = 0
        n = len(s)
        L = 0
        res = 0
        for R in range(n):
            contents[s[R]] = contents.get(s[R], 0) + 1
            
            # shrink window if invalid
            nondom = sum(contents.values()) - max(contents.values())
            while nondom > k:
                contents[s[L]] -= 1
                L += 1
                nondom = sum(contents.values()) - max(contents.values())
            
            res = max(res, R - L + 1)

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #######################################
        
        
#         # sliding window
#         # keep track of contents of window
#         # need to keep track of most frequent char to see what else needs to be replaced
#         # window needs to be within k number of elements (not including most frequent char)
#         #  window size - all char (not most frequent) <= k
#         # time: n, actually 26n since grabbing most frequent requires going through entire contents
#         # space: n, since we store contents
        
#         windowContents = {}
#         currWindow, maxWindow = 0, 0
#         left = 0
#         mostFrequentCount = 0
        
#         for right in s:
#             windowContents[right] = 1 + windowContents.get(right, 0)
#             currWindow += 1
            
#             # grab most frequent
#             mostFrequentCount = max(windowContents.values())
            
#             while currWindow - mostFrequentCount > k:
#                 windowContents[s[left]] -= 1
#                 left += 1
#                 currWindow -= 1
#                 # mostFrequentCount = max(windowContents.values()) # don't have a proof of why we don't need to do this...
#             maxWindow = max(maxWindow, currWindow)
            
#         return maxWindow