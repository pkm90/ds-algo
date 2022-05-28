# do this again in future

# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """


# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """


# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """



# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """



class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        
        for s in strs:
            res.append(str(len(s) + 1) + "#" + s)
        
        return ''.join(res)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        res = []
        s = list(s)
        
        i = 0
        while i < len(s):
            digit = []
            while s[i].isdigit():
                digit.append(s[i])
                i += 1
            digit = int(''.join(digit))
            
            res.append(''.join(s[i + 1:i + digit]))
            i += digit
        
        return res













































########################3

# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
#         res = []
#         for s in strs:
#             res.append(str(len(s)) + "#" + s)
        
#         print(res)
#         return ''.join(res)
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """
#         res = []
#         s = list(s)
#         print(s)
        
#         i = 0
#         while i < len(s):
#             curr = s[i]
            
#             # grab digit
#             digit = []
#             while curr.isdigit():
#                 digit.append(curr)
#                 i += 1
#                 curr = s[i]
#             digit = int(''.join(digit))
            
#             # append string
#             string = s[i + 1 : i + digit + 1]
#             res.append(''.join(string))
            
#             i += digit + 1
            
#         return res

##############33333333333333

# class Codec:
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
#         res = ''
#         for s in strs:
#             res += str(len(s)) + '?' + s
#         return res
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """
#         res = []
#         i = 0
        
#         while i < len(s):
#             numChar = i
#             while s[numChar] != '?':
#                 numChar += 1
#             length = int(s[i:numChar])
            
#             # numChar is at the delimiter, the ? so we need to + 1
#             res.append(s[numChar + 1:numChar + 1 + length])
            
#             i = numChar + 1 + length
            
#         return res

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(strs))