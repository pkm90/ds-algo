# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return
        
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        
        
        return
    
        # iterative bfs > keep track of each level > return the level
        # going to do this recursively to practice recursion
        
#         if root is None: return 0
                
#         def dfs(root, step):
#             self.maxdepth = max(self.maxdepth, step)
#             if root.right: dfs(root.right, step+1)
#             if root.left: dfs(root.left, step+1)

#         depth, self.maxdepth = 1, 1
#         dfs(root, depth)
        
#         return self.maxdepth
    
        # practicing recursion
        # still need more practice, can't think of this so easily
        if root is None: return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)