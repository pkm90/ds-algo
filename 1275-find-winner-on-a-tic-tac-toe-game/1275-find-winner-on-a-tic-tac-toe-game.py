class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        
        
        
        # we only need to check one row and one column
        # if there is a winner, then print the winnder
        # if we find an empty square, then print pending
        # else, print draw
        
        # checks, count number of occurrences...if there are 3 anywhere then we have a winner
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
        