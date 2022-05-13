# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
        def dfs(currNode):
            if currNode is None:
                return None
            
            left = dfs(currNode.right)
            right = dfs(currNode.left)
            currNode.left = left
            currNode.right = right
            return currNode
            
        dfs(root)
        return root
