# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def validate(root, lower, upper):
            if root is None:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            
            left = validate(root.left, lower, root.val)
            right = validate(root.right, root.val, upper)
            
            return left and right
        
        return validate(root, float(-inf), float(inf))
        
        
        
        
        
        
        
        
        
        
        
        
#         def dfs(root):
#             if root is None:
#                 return True
            
#             left = dfs(root.left)
#             if prev[0] >= root.val:
#                 return False
#             prev[0] = root.val
#             right = dfs(root.right)
            
#             return left and right
        
#         prev = [float(-inf)]
#         res = dfs(root)
#         return res
        
#         def dfs(root, lower, upper):
#             if root is None:
#                 return True
            
#             if (root.val <= lower or root.val >= upper):
#                 return False
#             left = dfs(root.left, lower, root.val)
#             right = dfs(root.right, root.val, upper)
            
#             return left and right
        
#         res = dfs(root, float(-inf), float(inf))
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # inorder traversal in BST will be in ascending order
        # inorder is left>root>right
        
        # we can store values of an inorder traversal and check if it is ascending
        
        # alternatively, we can keep track of prev inorder value and make sure current is greater
        # recursive, base case
        #  if root is None, return True -- basically, it's true until we find an instance where inorder isn't ascending
        # process
        #  recursive on left, check for ascending, update the previous value to current, recursive on right
        #  return boolean of left AND right, if we get a false anywhere then the ascending is brokeing and we return a false
        
        # the normal way of doing this is to simply check boundaries for each node
        # we would have a left and right boundary
        #  if we move left, then every single node in the subtree must be less than the current
        #  if we move right, then every single node in that subtree must be greater than current
        #  in other words, if we move left, then we update the right boundary and vice versa
        # this can be done with bfs or dfs, it just depends on how we keep track of the boundaries
        
#         # inorder traversal on a bst returns nodes in ascending order
#         # below is checking an inorder traversal, and making sure that current is less than previous
#         if root is None: return None
        
#         def validate(root):
#             if root is None: 
#                 return True
            
#             a=validate(root.left)
#             if root.val<=self.prev:
#                 return False
#             self.prev = root.val
#             b=validate(root.right)
#             return a and b

#         self.prev = -math.inf
#         res = validate(root)
#         return res

#         # going to try doing this with divide+conquer
#         # if we do bottom up, 
#         # divide: recurse until we are at leaf nodes and return current (which is leaf)
#         # conquer: check bst properties, if at any point in time it is false then return false
#         #  returning false will not stop the recursion, how to make that false pop up all the way?
#         # combine: return current (which is parent of previous leaf, or parent of previous node)
#         # below needs another function that takes a range...for recursive we still need the upper
#         #  and lower bounds...
#         # finishing this next time I see it.
        
#         # base
#         # print(root)
#         # if (root.left is None and root.right is None):
#         #     return root
#         if root is None: return None
#         if root is False:
#             return False
#         # if root is True:
#         #     return root
        
#         # if root.left: 
#         left = self.isValidBST(root.left) #if root.left is not None else None
#         # if root.right: 
#         right = self.isValidBST(root.right)# if root.right is not None else None
            
#         # if left is None 
#         # left = True if left is None else left
#         # right = True if right is None else right
#         # print(left, right)
#         # print(left.val, root.val, right.val)
#         print('left, root, right', left, root, right)
#         if (left is not None and root.val <= left.val or
#             right is not None and root.val >= right.val):
#             print('returning false')
#             return False
#         # if (root.val <= left.val or root.val >= right.val):
#         #     print('returning false')
#         #     return False
        
#         return root
    
        ######################################
        
        # for a binary search tree, we know that inorder must be ascending
        # we can do an inorder traversal, and if any current isn't > prev, then return False
        # if we make it all the way through, then return True
        
        # alternatively, we can keep upper and lower bounds
        # iterate through tree, if current isn't within bounds, return False
        # update bounds for next nodes
        # if we get through whole tree then it is valid and return True
        
#         def validate(root, lower, upper):
#             if root is None:
#                 return True
            
#             if (root.val <= lower or root.val >= upper):
#                 return False
            
#             left = validate(root.left, lower = lower, upper = root.val)
#             right = validate(root.right, lower = root.val, upper = upper)
            
#             return left and right
        
#         res = validate(root = root, lower = float(-inf), upper = float(inf))
#         return res
        
        