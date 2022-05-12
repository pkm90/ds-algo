# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        
        
        
        print(p)
        trav = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            trav.append(root)
            inorder(root.right)
            
        inorder(root)
        
        for i in range(len(trav)):
            print(trav[i])
            if trav[i].val == p.val:
                if i + 1 < len(trav):
                    print(trav[i + 1])
                    return trav[i + 1]
                else:
                    return None
        
        
        
        
        
        
        # one option is to do an in-order traversal and add all nodes to a list
        # search through the list and return the value that comes right after P
        # if we want to be fancy, then we can start from the middle of the list and increase/decrease from there
        # o(n) search, logn list search, n space
        
        # alternatively, we can do a dfs and move towards our value
        # if the value is found, if current==p, return current.right if possible, else return None
        
#         if root is None: return None
             
#         def getSucessor(root):
#             root = root.right
#             while root.left:
#                 root = root.left
#             return root
#             if root is None:
#                 return None
#             if root.left is None:
#                 return root.val
#             nextSmallest(root.left)
        
#         def search(root, p):
#             if root == p:
#                 return nextSmallest(root)

#             # if root.left: search(root.left, p)
#             # if root.right: search(root.right, p)
#             if p.val < root.val:
#                 search(root.left, p)
#             if p.val > root.val:
#                 search(root.right, p)
        
#         res = search(root, p)
#         return res