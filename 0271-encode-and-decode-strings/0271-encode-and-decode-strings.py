class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = []
        
        for s in strs:
            temp = str(len(s)) + "#"
            res.append(temp + s)
        
        print(res)
        res = "".join(res)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
            
        res = []
        idx = 0
        while idx < len(s):
            temp = []
            strlen = ""
            
            # grab len of string
            while s[idx] != "#":
                strlen += s[idx]
                idx += 1
                
            # grab string
            strlen = int(strlen)
            strEnd = idx + strlen + 1
            res.append(s[idx + 1:strEnd])
            idx = strEnd

        print(res)
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))