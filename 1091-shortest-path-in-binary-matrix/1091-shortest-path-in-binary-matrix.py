class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs
        # set variables, goal, q, etc
        # bfs from starting point
        #  if current is goal then return the sum
        #  if visited, then just continue
        #  nodes in queue will carry the position and sum
        #  valid nodes are within row+column bounds, equal 0, and haven't been visited
        #  need to keep track of diagonal and add two as opposed to one
        # if we go through bfs and sum isn't returned, a path isn't possible and return -1
        
        if grid[0][0] != 0: return -1
        rows, cols = len(grid), len(grid[0])
        goal = [rows-1, cols-1]
        visited = set()
        q = collections.deque()     
        q.append((0, 0, 1))
            
        def checkNode(row, col, cost):
            if (row<rows and row>=0 and
                col<cols and col>=0
                and grid[row][col] == 0
                and (row, col) not in visited):
                q.append((row, col, cost+1))
                visited.add((row, col))
            
        # bfs
        while q:
            # print(q)
            r, c, cost = q.popleft()
            # print(r, c, cost)
            if [r, c] == goal:
                return cost

            # check up and down
            checkNode(r+1, c, cost)
            checkNode(r-1, c, cost)
            checkNode(r, c+1, cost)
            checkNode(r, c-1, cost)
            
            # check diagonal
            checkNode(r+1, c+1, cost)
            checkNode(r+1, c-1, cost)
            checkNode(r-1, c+1, cost)
            checkNode(r-1, c-1, cost)

        return -1
        
        