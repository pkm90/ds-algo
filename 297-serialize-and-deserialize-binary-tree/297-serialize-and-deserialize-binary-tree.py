####
# do again
####

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
        

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # we can do a bfs while appending nulls, comma delimiter?
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            curr = q.popleft()
            if curr is None:
                res.append('N,')
                continue
                
            res.append(str(curr.val) + ',')
            for child in [curr.left, curr.right]:
                q.append(child)
                
        print(res)
        return ''.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        print(data)
        listData = data.split(',')
        if listData[0] == 'N':
            return None
        else:
            root = TreeNode(val = listData.pop(0))
        
        q = collections.deque()
        q.append(root)
        while q:
            curr = q.popleft()
            print(curr)
            if curr is None:
                continue
            
            lVal, rVal = listData.pop(0), listData.pop(0)
            curr.left = None if lVal == 'N' else TreeNode(val = lVal)
            curr.right = None if rVal == 'N' else TreeNode(val = rVal)
            q.append(curr.left)
            q.append(curr.right)
            
        # print(root)
        return root

        
        
        
        
  















        
# class Codec:
#     # do a bfs, log all children including Nulls
#     # when recreating, we can put the string into a list and recreate
#     # 

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         q = collections.deque([root])
#         res = ''
#         while q:
#             curr = q.popleft()
#             if curr is None:
#                 res += 'N,'
#                 continue
#             res += str(curr.val) + ','
#             for child in [curr.left, curr.right]:
#                 q.append(child)
#         print(res)
#         return res
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         listData = data.split(',')
#         if listData[0] is 'N':
#             return []
        
#         root = TreeNode(val = listData.pop(0))
#         q = collections.deque([root])
        
#         print(listData)
#         while q:
#             curr = q.popleft()
#             if curr is None:
#                 continue
                
#             tempVal = listData.pop(0)
#             curr.left = None if tempVal.isalpha() else TreeNode(val = int(tempVal))
#             tempVal = listData.pop(0)
#             curr.right = None if tempVal.isalpha() else TreeNode(val = int(tempVal))
            
#             q.append(curr.left)
#             q.append(curr.right)
#         return root
        
# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))