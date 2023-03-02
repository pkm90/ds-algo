class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # return true/false
        
        
        # validate each rule one by one
        # if any are broken, return false, else true
        
        
        #[ [0,1,2,3,4,...],
        #  [0,1,2,3,4,...],
        #  [0,1,2,3,4,...], ]
        
        # brute-force, literally check every single row for unique
        # check cols for unique
        # check box: 00, 01, 02, 10,11,12, 20,21,22
        
        # hashsets store unique values
        # store all the unique values of each row and col
        # 5,5,5  len(set) == 1
        

        # space: set() for each row
        # 10 rows, 10 * 9 == 10 sets, 10 * 9
        # 100 rows, 100 * 9 == 100 sets, 100 * 9
#         # o(n) linear
#         setRows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
#         setCols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        
#         # create sets of unique values for each row and col
#         for row in range(len(board)):
#             for col in range(len(board)):
#                 currRow = board[row][col]
#                 currCol = board[col][row]
#                 if currRow == ".":
#                     continue
#                 if currCol == ".":
#                     continue
                
#                 if currRow in setRows[row]:
#                     return False
#                 if currCol in setCols[col]:
#                     return False
#                 setRows[row].add(currRow)
#                 setCols[col].add(currCol)
            
        
        
        
        rows = [ set() for i in range(9) ]
        cols = [ set() for i in range(9) ]
        box = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                if (val in rows[r]
                    or val in cols[c]
                    or val in box[(r//3, c//3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                box[(r//3, c//3)].add(val)
                
        # print(box)
        for k,v in box.items():
            print(k, v)
        
                
        return True
            
        
        print(setRows)
        print(setCols)
        
        
        # check 3x3
        return True
        
        