class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        
        
        
        # we only need to check one row and one column
        # if there is a winner, then print the winnder
        # if we find an empty square, then print pending
        # else, print draw
        
        
        # checks
        rowa, cola, d1a, d2a = [0, 0, 0],[0, 0, 0], 0, 0
        rowb, colb, d1b, d2b = [0, 0, 0],[0, 0, 0], 0, 0
        
        # storing moves
        A = []
        B = []
        for i in range(len(moves)):
            if i % 2 == 0:
                A.append(moves[i])
            else:
                B.append(moves[i])
        
        # adding moves to checks
        for r, c in A:
            rowa[r] += 1
            cola[c] += 1
            if r == c:
                d1a += 1
            if ((r == 1 and c == 1) or
                (r == 0 and c == 2) or
                (r == 2 and c == 0)):
                d2a += 1
        
        for r, c in B:
            rowb[r] += 1
            colb[c] += 1
            if r == c:
                d1b += 1
            if ((r == 1 and c == 1) or
                (r == 0 and c == 2) or
                (r == 2 and c == 0)):
                d2b += 1
         
        # checking for winners
        if (any(3 == count for count in rowa) or
            any(3 == count for count in cola) or
            d1a == 3 or d2a == 3):
            return "A"
        if (any(3 == count for count in rowb) or
            any(3 == count for count in colb) or
            d1b == 3 or d2b == 3):
            return "B"
        
        if len(moves) < 9:
            return "Pending"
        
        return "Draw"
        
                
#         for i in range(3):
#             if 
        
#         # checking vert
#         for c in rows:
#             if moves[0][c] == moves[1][c] and moves[1][c] == moves[2][c]:
#                 return str(moves[0][c])
#             check.clear()
#             player = moves[0][c]
#             check.add(moves[0][c])
#             check.add(moves[1][c])
#             check.add(moves[2][c])
#             if player is None:
#                 return "Pending"
#             if len(check) == 1:
#                 return str(player)
        
#         # checking hori
#         for r in cols:
#             check.clear()
#             player = moves[r][0]
#             check.add(moves[r][0])
#             check.add(moves[r][1])
#             check.add(moves[r][2])
#             if player is None:
#                 return "Pending"
#             if len(check) == 1:
#                 return str(player)
        
#         # checking diag
        
        
        
        
        
        
#         return "Draw"
        