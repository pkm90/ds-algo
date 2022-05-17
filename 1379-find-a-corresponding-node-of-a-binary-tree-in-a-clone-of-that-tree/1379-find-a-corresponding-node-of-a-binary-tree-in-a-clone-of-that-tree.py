# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # iterate through both trees at once, if original.curr == target then return cloned.curr
        
        
        
        q = collections.deque([(original, cloned)])
        
        while q:
            normalCurr, clonedCurr = q.popleft()
            
            if normalCurr == target:
                return clonedCurr
            if normalCurr.left:
                q.append((normalCurr.left, clonedCurr.left))
            if normalCurr.right:
                q.append((normalCurr.right, clonedCurr.right))
            
            
            