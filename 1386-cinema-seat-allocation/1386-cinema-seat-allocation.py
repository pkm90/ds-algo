class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        
        
        # iterate through each row, count number of valid possibilities 
        # the only possible seats can be 2345, 4567, or 6789
        # first check 2345 and 6789, if both aren't possible then check 4567
        # reserved seats should be in a set so we can check easily
        # if 2345 and 6789 are not valid, then check if 4567 is valid
        # tle...answer is to start with max number of families and subtract based on columns
        
        
#         seats = collections.defaultdict(set)

#         for i,j in reservedSeats:
#             if j in [2,3,4,5]:
#                 seats[i].add(0)
#             if j in [4,5,6,7]:
#                 seats[i].add(1)
#             if j in [6,7,8,9]:
#                 seats[i].add(2)
#         print(seats)
#         res = 2*n
#         for i in seats:
#             if len(seats[i]) == 3:
#                 res -= 2
#             else:
#                 res -= 1

#         return res
        
        
        
        res = 2 * n
        left = [2,3,4,5]
        mid = [4,5,6,7]
        right = [6,7,8,9]
        reserved = { row:set() for row, col in reservedSeats }
        for row, col in reservedSeats:
            if col in left:
                reserved[row].add('left')
            if col in right:
                reserved[row].add('right')
            if col in mid:
                reserved[row].add('mid')
        
        print(reserved)
        for row, col in reserved.items():
            if len(reserved[row]) == 0:
                continue
            if len(reserved[row]) == 3:
                res -= 2
            else:
                # print(len(reserved[row]))
                res -= 1
                # res -= len(reserved[row])
        return res
                
        
        
        
            # count = 0
            # if left in col:
            #     count += 1
            # if col in right:
            #     count += 1
            # if col in mid:
            #     count += 1
            # res -= 2 if count == 3 else count
            # print(res)
            # if count == 3:
            #     res -= 2
            # else:
            #     res -= count
        # return res
            
            
#         rows, cols = n + 1, 11
#         reserved = set( tuple(seat) for seat in reservedSeats )
#         reservedRows = set( seat[0] for seat in reserved )
#         res = 0
        
#         def checkRow(row):
#             outside, middle = 2, 1
#             # check 2345 and 6789
#             # for c in range(1, cols):
#             if ((row, 2) in reserved or
#                 (row, 3) in reserved or
#                 (row, 4) in reserved or
#                 (row, 5) in reserved):
#                 outside -= 1
#             if ((row, 6) in reserved or
#                 (row, 7) in reserved or
#                 (row, 8) in reserved or
#                 (row, 9) in reserved):
#                 outside -= 1
#             if (outside or
#                 (row, 4) in reserved or
#                 (row, 5) in reserved or
#                 (row, 6) in reserved or
#                 (row, 7) in reserved):
#                 middle -= 1
#             return max(outside, middle)
#             # print(row, count)
#             # return 2 if count == 3 else count
        
#         for row in range(1, rows):
#             if row in reservedRows:
#                 # print('success', row, reservedRows)
#                 res += checkRow(row)
#             else:
#                 res += 2
            
#         return res
