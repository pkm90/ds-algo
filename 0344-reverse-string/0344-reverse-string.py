class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        
        
        # res = []
        # for i in range(len(s) -1, -1, -1):
        #     print(s[i])
        #     res.append(s[i])
        
        
        # index, len-index
        
#         for i in range(0, len(s)//2, 1):
#             # print(i)
#             left = s[i]
#             right = s[len(s) - 1 - i]
            
#             s[i] = right
#             s[len(s) - 1 - i] = left
            
        
        
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        
        
        
        
        