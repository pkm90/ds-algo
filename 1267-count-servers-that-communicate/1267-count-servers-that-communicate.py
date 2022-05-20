class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        
        
        
        # go through grid and make edges between servers
        # unionfind
        # grab rank of each parent where where number of components is > 1
        
        # we can also count number of computers per row and col and store inside arrays
        # iterate through grid, and if current node has more than itself in the row and col then add him
        
        rows, cols = len(grid), len(grid[0])
        totalRow = [0] * rows
        totalCol = [0] * cols
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    totalRow[r] += 1
                    totalCol[c] += 1
                    
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1
                    and (totalRow[r] > 1 or totalCol[c] > 1)):
                    res += 1
         
        return res