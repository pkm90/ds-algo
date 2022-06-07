# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def sameTree(rootp, rootq):
            if rootp is None and rootq is None:
                return True
            if bool(rootp) != bool(rootq):
                return False
            if rootp.val != rootq.val:
                return False
            
            left = sameTree(rootp.left, rootq.left)
            right = sameTree(rootp.right, rootq.right)
            return left and right
        
        # iterative
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            if curr.val == subRoot.val and sameTree(curr, subRoot):
                return True
        
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
            
#         # recursive
#         def dfs(rootp, rootq):
#             if rootp is None:
#                 return False
#             same = False
#             if rootp.val == rootq.val:
#                 same = sameTree(rootp, rootq)
#             left = dfs(rootp.left, rootq)
#             right = dfs(rootp.right, rootq)
            
#             return same or left or right
        
#         return dfs(root, subRoot)
        
        
        #################
        
        
        
        # iterative, iterate until same value is found
        #  then start storing nodes
        #  check if path is same as the subroot
        
        # recursive
        # base is if root is None return None
        # look for same root as subroot
        #  when it's found, check if left and right children are same and return True
        # otherwise, return false # subroot is not found
        
        # we have to iterate through the bigtree and run another function to check if tree is same
        # otherwise, we get issues with similar root nodes being higher
        # example: [1,1] [1]
        
        def sameTree(l, r):
            if l is None and r is None:
                return True
            if bool(l) != bool(r):
                return False
            if l.val != r.val:
                return False
            
            left = sameTree(l.left, r.left)
            right = sameTree(l.right, r.right)
            return left and right
        
        if root is None:
            return False
        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right