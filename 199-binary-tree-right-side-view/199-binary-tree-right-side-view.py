# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        
        # level order
        # grab rightmost element for each level
        
        q = collections.deque([root])
        res = []
        levels = []
        while q:
            currLevel = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr is None:
                    continue
                currLevel.append(curr.val)
                q.extend([curr.left, curr.right])
            levels.append(currLevel)
        
        print(levels)
        for level in levels:
            if level:
                res.append(level[-1])
        return res
        
        def rightView(root):
            if root is None:
                return
            res.append(root.val)
            if root.right:
                rightView(root.right)
            else:
                rightView(root.left)
            
        rightView(root)
        return res