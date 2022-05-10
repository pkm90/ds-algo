class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        
        
        
        
        
        
        
        visit = set()
        count = 0
        
        def findLand(row, col):
            if (row >= rows or row < 0 or
               col >= cols or col < 0
               or (row, col) in visit
               or grid[row][col] == "0"):
                return
            visit.add((row, col))
            
            findLand(row + 1, col)
            findLand(row - 1, col)
            findLand(row, col + 1)
            findLand(row, col - 1)

            # if valid, add to visited and check adj land
            
        
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col] == "1":
                    count += 1
                    findLand(row, col)
                    
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def explore(row, col):
#             # validate if cell is valid and explore
#             if (row >= 0 and row < rows and
#                 col >= 0 and col < cols
#                 and (row, col) not in visited
#                 and grid[row][col] == '1'):
#                 visited.add((row, col))
#                 explore(row + 1, col)
#                 explore(row - 1, col)
#                 explore(row, col + 1)
#                 explore(row, col - 1)
            
        
#         rows, cols = len(grid), len(grid[0])
#         visited, count = set(), 0
#         # choices = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
#         for row in range(rows):
#             for col in range(cols):
#                 if (grid[row][col] == '1' and (row, col) not in visited):
#                     count += 1
#                     explore(row, col)
#         return count
        
        
#         from collections import deque
        
#         # initialize variables
#         rows, cols = len(grid), len(grid[0])
#         print(rows,cols)
#         q = deque()
#         visited = set()
#         islands = 0
        
#         # add function for cleaner checks
#         def addtoq(r,c):
#             if (r<rows and r>=0
#                 and c<cols and c>=0
#                 and (r,c) not in visited
#                 and grid[r][c]=='1'):
#                     q.append([r,c])
#                     visited.add((r,c))
        
#         # bfs if current is a 1
#         def bfs(row, col):
#             q.append([row,col])
#             while len(q)>0:
#                 r, c = q.popleft()
#                 visited.add((r,c))
                
#                 addtoq(r+1, c)
#                 addtoq(r-1, c)
#                 addtoq(r, c+1)
#                 addtoq(r, c-1)
        
#         # search through grid
#         for r in range(rows):
#             for c in range(cols):
#                 if (grid[r][c]=='1'
#                     and (r,c) not in visited):
#                     # run bfs
#                     bfs(r,c)
#                     islands+=1
#                 else:
#                     visited.add((r,c))
        
#         return islands




# second attempt passed
#         from collections import deque
        
#         # search through the grid
#         # if island found: 
#         #  search for adjacent land and mark
#         #  iterate the num islands
        
#         if grid is None:
#             return None
#         rows, cols = len(grid), len(grid[0])
#         numislands = 0
#         visited = set()
#         q = deque()

        
#         def checknode(row, col):
#             # if in range, is land, not already visited: add to q and visited
#             r, c = row, col
#             if (r<rows and r>=0
#                 and c<cols and c>=0
#                 and grid[r][c]=='1'
#                 and (r, c) not in visited):
#                 q.append([r, c])
#                 visited.add((r, c))
        
#         def islandssearch(row, col):
#             # add adjacent land nodes
#             q.append([row,col])
#             visited.add((row,col))
#             while q:
#                 r, c = q.pop()
#                 checknode(r+1, c)
#                 checknode(r-1, c)
#                 checknode(r, c+1)
#                 checknode(r, c-1)
                
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]=='1' and (r,c) not in visited:
#                     print('inside')
#                     # search for adjacent land and mark
#                     islandssearch(r,c)
#                     numislands+=1
#         return numislands
    
    ######################################################
        # iterate through the grid
        # if we find land, then find the rest of hte land and mark visited
        # count number of times land has been found
        # return the count
        
#         rows, cols = len(grid), len(grid[0])
#         q = collections.deque()
#         visited = set()
#         count = 0
                    
#         def findLand(r, c):
#             q.append([r, c])
#             visited.add((r, c))
#             while q:
#                 r, c = q.popleft()
#                 checkNode(r + 1, c)
#                 checkNode(r - 1, c)
#                 checkNode(r, c + 1)
#                 checkNode(r, c - 1)
            
#         def checkNode(r, c):
#             if (r < rows and r >= 0 and
#                 c < cols and c >= 0
#                 and (r, c) not in visited
#                 and grid[r][c] == '1'):
#                 q.append([r, c])
#                 visited.add((r, c))
                
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == '1' and (row,col) not in visited:
#                     count += 1
#                     findLand(row, col)
                    
#         return count