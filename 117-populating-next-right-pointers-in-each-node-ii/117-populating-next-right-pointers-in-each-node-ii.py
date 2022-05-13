"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        
        
        
        
        q = collections.deque([root])
        
        while q:
            numNodes = len(q)
            for level in range(numNodes):
                curr = q.popleft()
                if curr is None:
                    continue
                    
                # print(curr.val)
                
                # if level != numNodes - 1:
                    
                    # temp = q[0]
                    # while not
                for inode in range(numNodes - level - 1):
                    # print(len(q), inode)
                    if q and q[inode] is not None:
                        curr.next = q[inode]
                        break
            
                    
                # curr.next = q[0]
                for child in [curr.left, curr.right]:
                    q.append(child)
            if curr:
                curr.next = None
        
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # level order bfs, prev.next = current
#         # t: o(n)
#         # s: o(n)
            
#         q = collections.deque([root])
#         while q:
#             prev = Node()
#             for _ in range(len(q)):
#                 curr = q.popleft()
#                 if curr is None: continue
#                 prev.next = curr
#                 for child in [curr.left, curr.right]:
#                     q.append(child)
#                 prev = curr
#             prev.next = None
        
#         return root