# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        
        # we want to keep track of the sum of each path
        # we also want to keep track of the max path sum
        self.res = root.val
        
        def findMaxPathSum(root):
            # we can do a bottom up approach
            # when we reach the end, we return 0
            if root is None:
                return 0

            # the left will keep track of the max path in the left side and vice versa
            left = findMaxPathSum(root.left)   # + root.val
            right = findMaxPathSum(root.right) # + root.val

            
            self.res = max(self.res, left + right + root.val)
            # we will return the max of 0, left + val, right + val
            #  the reason for this is htat we can have negative values, and it would be better
            #  to not take into account everything in that path so far
            #  we only want to return max of left or right since the max path sum needs to be
            #  calculated for parents
            return max(0, left + root.val, right + root.val)
        
        findMaxPathSum(root)
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#########################################
        
        
#         # each node can be the "pivot"
#         # we don't know where would be optimal, so we have to try them all
#         # bottom up, we can calculate the pivot at each node and return the max of left and right paths
        
#         def findMaxPathSum(root):
#             if root is None:
#                 return 0
            
#             left = findMaxPathSum(root.left)
#             right = findMaxPathSum(root.right)
#             res[0] = max(res[0], left + right + root.val)
            
#             return max(left + root.val, right + root.val, 0) # returning 0 lets us drop neg prefix
            
#         res = [float(-inf)]
#         findMaxPathSum(root)
#         return res[0]
        
        
################################################        
        
        
        # we need to find the maxsum of a path
        # either we use the current node as the "split" or we split on parent node
        # left and right recurse
        #  check if using current node as the split is max and replace max
        #  return the max of left + current or right + current to test if splitting at parent has a better max
        # time: linear, we visit each node once
        # space: h or logn... for the recursion stack, worst case is if tree is skewed then h == n, best case is logn
        
#         # below isn't necessary based on constraints but if
#         # we get an empty root then we would need it
#         if root is None:
#             return None        
        
#         def dfs(node):
#             if node is None:
#                 return 0
#             left = max(dfs(node.left), 0)
#             right = max(dfs(node.right), 0)
#             self.maxSum = max(self.maxSum, left + right + node.val)
#             return max(left + node.val, right + node.val)
        
#         self.maxSum = float(-inf)
#         dfs(node = root)
        
#         return self.maxSum