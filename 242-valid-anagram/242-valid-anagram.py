class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
#         # can count numbers of char, and check if the counts are the same
#         countS = Counter(s)
#         countT = Counter(t)
#         return countS == countT
        
        # can sort the inputs and check equality
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # store count of all letters in hashmap
#         # each time a letter is used, decrement
#         # if any value in hashmap is not 0, return False else True
#         # time: n
#         # space: 1, we store more for each letter but max of 26 values
        
#         choices = Counter(s)
        
#         for char in t:
#             if char not in choices:
#                 return False
#             else:
#                 choices[char] -= 1
        
#         for value in choices.values():
#             if value is not 0:
#                 return False
#         return True