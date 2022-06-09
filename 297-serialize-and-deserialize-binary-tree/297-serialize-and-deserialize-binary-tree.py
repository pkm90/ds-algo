####
# do again
####

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None





# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """

# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
        

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """




# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
        

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """



# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
        

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """


# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
        

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """





























##########################


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # we can do a bfs and store all the nodes including Nones
        res = []
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            if curr:
                res.append(str(curr.val) + ',')
            else:
                res.append('N,')
                continue
            
            q.extend([curr.left, curr.right])
        
        print(res)
        return ''.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        print(data)
        data = data.split(',')
        print(data)
        if data[0].isalpha():
            return
        else:
            root = TreeNode( val = data.pop(0) )
        
        res = []
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            res.append(curr.val if curr else None)

            if curr is None:
                continue
            
            temp = data.pop(0)
            left = None if temp.isalpha() else TreeNode(val = temp)
            temp = data.pop(0)
            right = None if temp.isalpha() else TreeNode(val = temp)
            curr.left = left
            curr.right = right
            q.extend([curr.left, curr.right])
        
        print(res)
        return root


    
############



# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
#         res = []
#         q = collections.deque([root])
        
#         while q:
#             curr = q.popleft()
#             if curr is None:
#                 res.append('N,')
#                 continue
#             res.append(str(curr.val) + ',')
#             for child in [curr.left, curr.right]:
#                 q.append(child)
        
#         print(res)
#         return ''.join(res)
        
#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """
#         print(data)
#         listData = data.split(',')
#         print(listData)
#         if listData[0].isalpha():
#             return None
#         root = TreeNode(val = listData.pop(0))
#         q = collections.deque([root])
        
#         while q:
#             curr = q.popleft()
#             if curr is None:
#                 continue
#             leftVal = listData.pop(0) if listData else 'N'
#             rightVal = listData.pop(0) if listData else 'N'
#             curr.left = None if leftVal.isalpha() else TreeNode(val = leftVal)
#             curr.right = None if rightVal.isalpha() else TreeNode(val = rightVal)
#             for child in [curr.left, curr.right]:
#                 q.append(child)
                
#         return root


#################


# class Codec:

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
#         # we can do a bfs while appending nulls, comma delimiter?
#         q = collections.deque()
#         res = []
#         q.append(root)
#         while q:
#             curr = q.popleft()
#             if curr is None:
#                 res.append('N,')
#                 continue
                
#             res.append(str(curr.val) + ',')
#             for child in [curr.left, curr.right]:
#                 q.append(child)
                
#         print(res)
#         return ''.join(res)

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """
#         print(data)
#         listData = data.split(',')
#         if listData[0] == 'N':
#             return None
#         else:
#             root = TreeNode(val = listData.pop(0))
        
#         q = collections.deque()
#         q.append(root)
#         while q:
#             curr = q.popleft()
#             print(curr)
#             if curr is None:
#                 continue
            
#             lVal, rVal = listData.pop(0), listData.pop(0)
#             curr.left = None if lVal == 'N' else TreeNode(val = lVal)
#             curr.right = None if rVal == 'N' else TreeNode(val = rVal)
#             q.append(curr.left)
#             q.append(curr.right)
            
#         return root

    #######################
        
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