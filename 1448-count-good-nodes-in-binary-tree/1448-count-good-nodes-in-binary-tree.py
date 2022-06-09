# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        
        def countNodes(root, greatestSoFar):
            if root is None:
                return
            
            if root.val >= greatestSoFar:
                self.res += 1
            countNodes(root.left, max(root.val, greatestSoFar))
            countNodes(root.right, max(root.val, greatestSoFar))

        self.res = 0
        countNodes(root, float(-inf))
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = [0]
        
#         def countNodes(root, currentMax):
#             if root is None: 
#                 return

#             if root.val >= currentMax: 
#                 count[0] += 1
#             countNodes(root.left, max(currentMax, root.val))
#             countNodes(root.right, max(currentMax, root.val))

#         countNodes(root, float(-inf))
#         return count[0]

