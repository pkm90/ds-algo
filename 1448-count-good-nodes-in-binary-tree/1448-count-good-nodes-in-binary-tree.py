# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        count = [0]
        
        def countNodes(root, currentMax):
            if root is None: 
                return

            if root.val >= currentMax: 
                count[0] += 1
            countNodes(root.left, max(currentMax, root.val))
            countNodes(root.right, max(currentMax, root.val))

        countNodes(root, float(-inf))
        return count[0]

