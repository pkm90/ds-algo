class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        
        
        
        
#         # extend into one array and search
#         nums = []
#         for r in matrix:
#             nums.extend(r)
        
#         l, r = 0, len(nums)
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] > target:
#                 r = mid
#             else:
#                 l = mid + 1
        
#         if nums[l - 1] == target:
#             return True
#         return False
        
        # search for the correct row, then search for the correct col in that row
        t, b = 0, len(matrix)
        while t < b:
            mid = (t + b) // 2
            if matrix[mid][0] > target:
                b = mid
            else:
                t = mid + 1
        
        nums = matrix[t - 1]
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l - 1] == target:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # binary search to find row
#         # binary search on above row
#         # solution is to do some math to track which row, and run binary search once: row = idx // n and col = idx % n.
    
#         rows, cols = len(matrix), len(matrix[0])
        
#         # find which row
#         # binary search to find which row
#         small_row, big_row, target_row = 0, rows - 1, None
#         while small_row < big_row:
#             mid = (small_row + big_row) // 2
#             if target >= matrix[mid][0] and target <= matrix[mid][-1]:
#                 target_row = matrix[mid]
#                 print('target row is mid')
#                 break
#             if target < matrix[mid][0]:
#                 big_row = mid - 1
#             else:
#                 small_row = mid + 1
#         target_row = matrix[big_row] if target_row is None else target_row
        
#         print(target_row)
        
#         # do binary search on selected row
#         l, r = 0, cols - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if target_row[mid] == target:
#                 return True
            
#             if target < target_row[mid]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
                
#         return False
#         return target_row[l] == target 