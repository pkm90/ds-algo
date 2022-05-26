class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        
        
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ##################
        
        
#         # clean the input and then 2 ptrs
#         cleaned = []
#         for char in s:
#             if char.isalnum():
#                 cleaned.append(char.lower())
#         cleaned = ''.join(cleaned)
        
#         l, r = 0, len(cleaned) - 1
#         while l < r:
#             if cleaned[l] != cleaned[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True
        
        
        # remove whitespace and non-lowercase-letters
        # check if it is the same as it's reverse
        # not sure what they're looking for, can we use builtins?
        #  assuming we can use builtins...
        #   turn string to list, pop anything htat isn't alphabet, char.isalpha()
        #   otherwise, replace current with it's lowercase 
        #   can use isdigit(), isalpha(), or isalnum()
        #  reverse, can we use string.reverse()...?
        # otherwise check if it's a palindrome using two pointers
        # time: n, 2n but still linear
        # space: n, 2n
        
#         stringList = []
#         for i, char in enumerate(s):
#             if char.isalnum():
#                 stringList.append(char)
#             # if char.isdigit():
#             #     stringList.append(temp[i])
#             # if char.isalpha():
#             #     stringList.append(temp[i].lower())
                
#         print(stringList)
        
#         left, right = 0, len(stringList) - 1
#         while left < right:
#             l = stringList[left].lower()
#             r = stringList[right].lower()
#             if l != r:
#                 return False
#             left += 1
#             right -= 1
            
#         return True
        
        
                