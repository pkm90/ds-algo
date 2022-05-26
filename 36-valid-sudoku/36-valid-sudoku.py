# good hash practice, do again

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        rows = [ set() for i in range(9) ]
        cols = [ set() for i in range(9) ]
        squares = collections.defaultdict(set) # (row//3, col//3) : set
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if not val.isdigit():
                    continue
                
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                if val in squares[(r//3, c//3)]:
                    return False
                squares[(r//3, c//3)].add(val)
                
        return True
                
                
                