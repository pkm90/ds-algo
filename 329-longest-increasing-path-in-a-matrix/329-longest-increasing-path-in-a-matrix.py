# 1.5hr

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        
        
        
        
        
        
        
        
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        visit = set()
        work = {} # { (row, col):0 for row, col in zip(range(rows), range(cols)) }
        choices = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        print(work)
        
        
        def search(r, c, prev):
            if (r >= rows or r < 0 or
                c >= cols or c < 0 or
                matrix[r][c] <= prev):
                return 0
            if (r, c) in work:
                return work[(r, c)]
            
            maxpath = 0
            for choice in choices:
                row, col = choice[0] + r, choice[1] + c
                maxpath = max(maxpath, 1 + search(row, col, matrix[r][c]))
            # maxpath = max(maxpath, 1 + search(r - 1, c))
            # maxpath = max(maxpath, 1 + search(r, c + 1))
            # maxpath = max(maxpath, 1 + search(r, c - 1))
            work[(r, c)] = maxpath
            return maxpath
        
        
        for r in range(rows):
            for c in range(cols):
                search(r, c, float(-inf))
                res = max(res, work[(r, c)])
                
        print(work)
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # finished it but had bug which extended troubleshooting...1.5 hours -.-
#         # we won't need to keep track of visited since it has to be strictly increasing,
#         #  any prev node will never be valid
#         # iterate through each node and run dfs on all 4 sides, keep track of length and update as needed        
        
#         # running into tle with basic dfs solution
#         #  trying memoization, we can store the max path at any point
#         rows, cols = len(matrix), len(matrix[0])
#         work = {}
        
#         def search(r, c, prev):
#             if (r >= rows or r < 0 or
#                 c >= cols or c < 0
#                 or matrix[r][c] <= prev):
#                 return 0
#             if (r, c) in work:
#                 return work[(r, c)]
            
#             maxLen = 0            
#             maxLen = max(1 + search(r + 1, c, matrix[r][c]),
#                          1 + search(r - 1, c, matrix[r][c]),
#                          1 + search(r, c + 1, matrix[r][c]), 
#                          1 + search(r, c - 1, matrix[r][c]),)
#             work[(r, c)] = maxLen
#             return work[(r, c)]
        
#         for row in range(rows):
#             for col in range(cols):
#                 search(row, col, float(-inf))
#         return max(work.values())
            
