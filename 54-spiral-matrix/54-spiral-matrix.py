# try again in future

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # iterate through matrix while top < bot and left < right
        # follow the spiral matrix and append results
        # key thing is to understand how the top/bot/left/right impact each other
        
        res = []
        top, bot = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        print(top, bot, left, right)
        
        while top <= bot and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top > bot or left > right:
                break
            
            for i in range(right, left - 1, -1):
                res.append(matrix[bot][i])
            bot -= 1
            
            for i in range(bot, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         top, bot, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
#         res = []
#         while top < bot + 1 and left < right + 1:
#             # top
#             i = left
#             while i <= right:
#                 res.append(matrix[top][i])
#                 i += 1
#             top += 1
            
#             # right
#             i = top
#             while i <= bot:
#                 res.append(matrix[i][right])
#                 i += 1
#             right -= 1
            
#             # if top >= bot + 1 or left >= right + 1:
#             if not (top < bot + 1 and left < right + 1):
#                 break
                
#             # bot
#             i = right
#             while i >= left:
#                 res.append(matrix[bot][i])
#                 i -= 1
#             bot -= 1
            
#             # left
#             i = bot
#             while i >= top:
#                 res.append(matrix[i][left])
#                 i -= 1
#             left += 1  
        
#         return res
        
        
###################

        # basically just went through a simulation
        # identified functionally how it would work
        # we go in the following order: top > right > bot > left
        # every time we finish an line, we increment a counter for each
        # when we go through a line, we stay within bounds by using the counter
        # top and bot use right and left as bounds
        # left and right use top and bot as bounds
        # continue until counters are greater than the actual bounds? trying it out,
        
#         rows, cols = len(matrix), len(matrix[0])
#         top, bot = 0, rows
#         left, right = 0, cols
#         res = []
        
#         while top < bot and left < right:
#             for i in range(left, right): # top
#                 res.append(matrix[top][i])
#             top += 1
            
#             for i in range(top, bot): # right
#                 res.append(matrix[i][right - 1])
#             right -= 1
            
#             # checks that above didn't knock us out of bounds
#             if not (top < bot and left < right):
#                 break
            
#             for i in range(right - 1, left - 1, -1): # bot
#                 res.append(matrix[bot - 1][i])
#             bot -= 1
            
#             for i in range(bot - 1, top - 1, -1): # left
#                 res.append(matrix[i][left])
#             left += 1
        
#         return res
        
        