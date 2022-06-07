# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
#         def getHeight(root):
#             if root is None:
#                 return 0
            
#             left = getHeight(root.left) + 1
#             right = getHeight(root.right) + 1
#             return max(left, right) + 1
        
        def getDiam(root):
            if root is None:
                return 0
            
            left = getDiam(root.left)
            right = getDiam(root.right)
            self.diam = max(self.diam, left + right)
            return max(left, right) + 1
        
        self.diam = 0
        getDiam(root)
        return self.diam
    
#         if root is None:
#             return 0
        
#         leftHeight = self.diameterOfBinaryTree(root.left) + 1
#         rightHeight = self.diameterOfBinaryTree(root.right) + 1
#         diam = 
        
#         return max(left + right, diam)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.diameter = 0
    
#     def helper(self, root):
#         if root is None:
#             return 0
        
#         left = self.helper(root.left)
#         right = self.helper(root.right)
        
#         self.diameter = max(self.diameter, left + right)
        
#         return max(left, right) + 1
        
#     # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # height of a subtree is the max length from root to some leaf node
#         # we can grab the height of each subtree and continuously update max diameter
#         # bottom up
#         # base: if root is None return 0
#         # update max diameter
#         # recursively call left and right
#         # return max of left and right, this simulates taking only one path
        
#         self.helper(root)
#         return self.diameter