# do again

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def balanced(root):
            if self.res is False:
                return float(inf)
            if root is None:
                return 0
            
            left = balanced(root.left)
            right = balanced(root.right)
            if abs(left - right) > 1:
                self.res = False
            return max(left, right) + 1
        
        self.res = True
        balanced(root)
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ####################
        
        
#         # recursive
#         # base: if root is None, return 0
#         # if difference of left and right > 1, return False
#         # return True
#         # trying bottom up recursion, it's tricky to do this without a helper function
        
#         if root is None:
#             return (True, 0)
#         if root is False:
#             return False
        
#         left = self.isBalanced(root.left) 
#         right = self.isBalanced(root.right)
#         if left and right and abs(left[1] - right[1]) <= 1:
#             return (True, max(left[1], right[1]) + 1)
#         else:
#             return False