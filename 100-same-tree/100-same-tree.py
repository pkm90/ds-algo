# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        
        
        
        if bool(p) != bool(q):
            return False
        if p is None:
            return True
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
        
        
        
#         qu = collections.deque()
#         qu.append((p, q))
        
#         while qu:
#             currP, currQ = qu.popleft()
#             if bool(currP) != bool(currQ):
#                 return False
#             if not currP:
#                 continue
            
#             if currP.val != currQ.val:
#                 return False
#             qu.append((currP.left, currQ.left))
#             qu.append((currP.right, currQ.right))
            
#         return True
        
        
        
        
        
        
        
        
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # left needs to be same as right
        # get a path including null nodes, and compare
#         qu = collections.deque()
#         qu.append(p)
#         leftPath, rightPath = [], []
        
#         while qu:
#             curr = qu.popleft()
#             if curr is None:
#                 leftPath.append(None)
#                 continue
#             leftPath.append(curr.val)
#             qu.append(curr.left)
#             qu.append(curr.right)
        
#         qu.append(q)
#         while qu:
#             curr = qu.popleft()
#             if curr is None:
#                 rightPath.append(None)
#                 continue
#             rightPath.append(curr.val)
#             qu.append(curr.left)
#             qu.append(curr.right)
        
#         return leftPath == rightPath
    
        # recursive solution?
        if p is None and q is None:
            return True
        if bool(p) != bool(q):
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right
        