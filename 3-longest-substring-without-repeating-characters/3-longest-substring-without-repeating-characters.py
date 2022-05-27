class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        
        
        
        
        
        # # bruteforce
        # # find every single substring and check if all char is unique
        # # 
        # n = len(s)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         window = s[i:j]
        #         unique = set(window)
        #         if len(window) == len(unique):
        #             res = max(res, len(unique))
        # return res
    
    
        # keep track of everything inside window
        # if we have something, then shrink window until valid
        contents = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in contents:
                contents.remove(s[left])
                left += 1
            contents.add(s[right])
            res = max(res, len(contents))
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ################################
        
        
        # sliding window
        # keep track of characters inside and max window size
        # if there are more than 1 of any character, start making it smaller
        # return max window size
        # time: n,  we iterate through array once...worst case is 2n where window gets as big as n, then small as 1
        # space: n, window contents can go up to n in the worst case 
        
#         windowContents = {}
#         maxWindowSize, currWindowSize = 0, 0
#         left = 0
        
#         for right in s:
#             # iterate contents and window size
#             windowContents[right] = 1 + windowContents.get(right, 0)
#             currWindowSize += 1
#             # if right in windowContents:
#             #     windowContents[right] += 1
#             # else:
#             #     windowContents[right] = 1

#             # if contents are valid, iterate max window size
#             if windowContents[right] <= 1:
#                 maxWindowSize = max(maxWindowSize, currWindowSize)
            
#             # make window size smaller if needed
#             while windowContents[right] > 1:
#                 windowContents[s[left]] -= 1
#                 left += 1
#                 currWindowSize -= 1
                
#         return maxWindowSize
                    
# # optimization would be to store the index of a char instead of counting them, then we can go in truly linear time
# # if a character exists inside hte table, then move the window to the index of char + 1
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = [None] * 128

#         left = right = 0

#         res = 0
#         while right < len(s):
#             r = s[right]

#             index = chars[ord(r)]
#             if index != None and index >= left and index < right:
#                 left = index + 1

#             res = max(res, right - left + 1)

#             chars[ord(r)] = right
#             right += 1
#         return res