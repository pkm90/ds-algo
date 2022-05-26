# do this again in future

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
            # res.append(s + '1')
        return ''.join(res)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        res = []
        s = list(s)
        string = []
        i = 0
        while i < len(s):
            num = []
            while s[i].isdigit():
                num.append(s[i])
                i += 1
            num = int(''.join(num))
            
            res.append(''.join(s[i + 1:i + num]))
            i = i + num

        return res
        


























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