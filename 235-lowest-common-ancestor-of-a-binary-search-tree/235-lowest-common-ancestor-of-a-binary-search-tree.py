# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        
#         # we want to be in a position where p and q are on different sides
#         # if p and q are on the same side, then move toward that side
#         # tle, as expected
#         def lca(root, p, q):
#             if root is None:
#                 return False
#             if root is p or root is q:
#                 return root
            
#             # check if either is in left, and either is in right
#             left = lca(root.left, p, q)
#             right = lca(root.right, p, q)
#             if left and right:
#                 return root
            
#             if left:
#                 return lca(root.left, p, q)
#             else:
#                 return lca(root.right, p, q)
        
#         return lca(root, p, q)
        
        
        # to optimize, we can check if current is within bounds and move towards that bound
        
        
        
        def dfs(root, lower, upper):
            if root is None:
                return False
            if root is lower or root is upper:
                return root
            
            # left = dfs(root.left, lower, upper)
            # right = dfs(root.right, lower, upper)
            
            if root.val < lower:
                return dfs(root.right, lower, upper)
            elif root.val > upper:
                return dfs(root.left, lower, upper)
            return root
        
        lower = min(p.val, q.val)
        upper = max(p.val, q.val)
        return dfs(root, lower, upper)
            
        # if root is < lower, move right vice versa
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # recursive
#         def find(node):
#             if node.val >= bounds[0] and node.val <= bounds[1]:
#                 return node
            
#             if node.val < bounds[0]:
#                 res = find(node.right)
#             else:
#                 res = find(node.left)
#             return res
        
#         lower = min(p.val, q.val)
#         upper = max(p.val, q.val)
#         bounds = [lower, upper]
#         res = find(root)    
        
#         return res
                
#         # iterative
#         small, big = min(p.val, q.val), max(p.val, q.val)
#         while root.val < small or root.val > big:
#             if root.val < small:
#                 root = root.right
#             else:
#                 root = root.left
                
#         return root


#         Q = collections.deque([root])
#         small, big = min(p.val, q.val), max(p.val, q.val)
        
#         while Q:
#             curr = Q.pop()
#             if curr is None:
#                 return None
#             if curr.val >= small and curr.val <= big:
#                 return curr
            
#             if curr.val < small:
#                 Q.append(curr.right)
#             else: # same as elif(curr.val > big), since return conditional didn't work
#                 Q.append(curr.left)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # we know that p and q are not the same
        # this means that the root will be inbetween p and q
        # we can continously move the root until left and right subtrees contain a p or q
        #  if both subtrees contain both p and q, then we move that way
        #  if one subtree contain p xor q, then we can say that the current node is the other p or q
        # we will move the root by checking if it is within bounds
        #  we don't know if p or q is greater, so we do that first and then set the lower and upper bound
        #  if root is less than lower, then we move right
        #  if root is greater than upper, then we move left
        # alternatively, we continuously move root until it is between p<=root and q>=root
        #  this way we get into a position where a subtree has p xor q and the root can be the other p or q
        
#         # iterative
#         if root is None:
#             return None
        
#         lower, upper = min(p.val, q.val), max(p.val, q.val)
        
#         #print(lower, upper)
#         while (root.val<=lower or root.val>=upper):
#             if (root.val>=lower and root.val<=upper):
#                 return root
#            # print(root)
#             if root.val>=upper:
#                 root=root.left
#             else: # root is <=lower
#                 root=root.right
#         return root

#         # recursive
#         lower, upper = min(p.val, q.val), max(p.val, q.val)
#         print(root.val, lower, upper)

#         if root is None:
#             return None
#         if (root.val>=lower and root.val<=upper):
#             return root
        
#         if root.val>=upper:
#             return self.lowestCommonAncestor(root=root.left, p=p, q=q)
#         else: #root is <=lower
#             return self.lowestCommonAncestor(root=root.right, p=p, q=q)

#####################
#         # we want to find the node that is between them
#         # iterate through tree or recurse...
#         lower, upper = min(p.val, q.val), max(p.val, q.val)
        
#         while root.val < lower or root.val > upper:
#             if root.val < lower:
#                 root = root.right
#             else:
#                 root = root.left
#         return root