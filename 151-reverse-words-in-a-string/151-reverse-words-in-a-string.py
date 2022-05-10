# 05/09/22: I'm looking at this problem and I remember doing these kinds of problems way easier before.
#  I'm thinking that I'm either burnt out or covid brain fog or something.
#  brain doesn't work the way it used to. every problem defaults to a bruteforce method, problem solving skills
#  require much more time, not sure what the issue is...

class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        
        
        # iterate through input in reverse
        # after a word is created (space is detected), reverse it and append to result
        # return result
        
        res = []
        word = []
        for char in s:
            if char.isalnum():
                word.append(char)
            elif word and char is " ":
            # if char is " ":
                word.append(" ")
                res.append(word)
                word = []
            # else:
            #     word.append(char)
        if word:
            word.append(" ")
            res.append(word)
        
        l, r = 0, len(res) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
            
        print(res)
        res[-1].pop() # removing last space
        
        words = []
        for word in res:
            words.append((''.join(word)))
        return ''.join(words)
            
        
        # for i, word in enumerate(res):
        #     # curr = word[i]
        #     l, r = 0, len(res) - 1
        #     while l < r:
        #         curr[l], curr[r] = curr[r], curr[l]
        #         l += 1
        #         r -= 1
        #     word[i] = curr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # create list of words
#         # reverse positions of words
#         # return string from list
        
#         # creating list of words, append last word at the end
#         cleaned = []
#         temp = []
#         for char in s:
#             if char.isalnum():
#                 temp.append(char)
#             elif temp:
#                 cleaned.append(temp)
#                 temp = []
#         if temp:
#             cleaned.append(temp)
#         print(cleaned)
        
#         # reversing words
#         l, r = 0, len(cleaned) - 1
#         while l < r:
#             cleaned[l], cleaned[r] = cleaned[r], cleaned[l]
#             l += 1
#             r -= 1
#         print(cleaned)
        
#         # turning list of words back into string, pop trailing space
#         res = []
#         for word in cleaned:
#             res.append(''.join(word))
#             res.append(' ')
#         res.pop()
#         return ''.join(res)
        
        
        
        

# # below is different from solution I came up with, mine doesn't work anymore, not sure why...
# # review, see if it's more elegant and better...
# # removes spaces, builds words one by one, if a word is finished then append to q
# # return the joined the strings in the q
# from collections import deque
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         left, right = 0, len(s) - 1
#         # remove leading spaces
#         while left <= right and s[left] == ' ':
#             left += 1
        
#         # remove trailing spaces
#         while left <= right and s[right] == ' ':
#             right -= 1
            
#         d, word = deque(), []
#         # push word by word in front of deque
#         while left <= right:
#             if s[left] == ' ' and word:
#                 d.appendleft(''.join(word))
#                 word = []
#             elif s[left] != ' ':
#                 word.append(s[left])
#             left += 1
#         d.appendleft(''.join(word))
        
#         return ' '.join(d)

# put each word into a list and then we have some options
# we can append strings backwards, reverse the list and then append it forwards, all while adding spaces between each word
# as for removing spaces, 2 pointers to get a segment of chars and append to list
# whenever there is a space, then start a new segment of chars
# to separate multiple spaces, let the pointers begin when there is not a space

# below solution goes
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         if s is None:
#             return None
        
#         left, right = 0, 0
#         words = []
#         word = ""
#         result = ""
#         index = 0
        
#         while index < len(s):
# #             if s[index] == " ":
# #                 word = ""
# #                 if len(word)>0:
# #                     words.append(word)
# #             else:
#             # build words char by char
#             # if current char isn't space, then add to word else we found a space so append the word
#             # problem is that this skips the last word if there is no whitespace after it
#             # there is another conditional below this to catch that edgecase
#             if s[index] != " ":
# #                 print([s[index]])
#                 word+=s[index]
# #                 print(word)
#             else:
#                 if (len(word)>0):
#                     words.append(word)
#                 word = ""
            
#             # this appends the last word
#             if (index==len(s)-1 and len(word)>0):
#                 words.append(word)
# #            elif len(word)>1:
#             index+=1
#         print(words)
#         left, right = 0, len(words)-1
#         while left < right:
#             words[left], words[right] = words[right], words[left]
#             left+=1
#             right-=1
        
        
#         words = " ".join(words)
# #         while index < len(words):
# #             result.join(words[index]+" ")
#         print(words)
# #         result.pop()
        
#         return words
