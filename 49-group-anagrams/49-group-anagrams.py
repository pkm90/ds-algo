class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        
        
        
        # can sort inputs and input into hashmap
        # return values of hashmap
        anagrams = {}
        for word in strs:
            w  = ''.join(sorted(word))
            anagrams[w] = anagrams.get(w, []) + [word]
        
        res = []
        for anas in anagrams.values():
            res.append(anas)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # can sort the string and use that as the key
        # or can transform each string into a character count and use that as key
        # here is the ord(char) of every lowercase char:
# a 97
# b 98
# c 99
# d 100
# e 101
# f 102
# g 103
# h 104
# i 105
# j 106
# k 107
# l 108
# m 109
# n 110
# o 111
# p 112
# q 113
# r 114
# s 115
# t 116
# u 117
# v 118
# w 119
# x 120
# y 121
# z 122

#         res = []
#         anagrams = {}
        
#         for word in strs:
#             counter = [0] * 256
#             for char in word:
#                 counter[ord(char)] += 1
            
#             counter = tuple(counter)
#             if counter in anagrams:
#                 anagrams[counter].append(word)
#             else:
#                 anagrams[counter] = [word]

#         for group in anagrams.values():
#             res.append(group)
            
#         return res