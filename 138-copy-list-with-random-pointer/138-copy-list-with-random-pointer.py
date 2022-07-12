"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # populate hashmap { node : newnode }
        # iterate through ll and new ll at same time, populate the pointers
        if head is None: return
        
        nodes = {}
        dummy = Node(x = 0, next = head)
        while head:
            if head not in nodes:
                nodes[head] = Node(x = head.val)
            head = head.next
            
        head = dummy.next
        newHead = nodes[head]
        while head:
            newHead.random = nodes[head.random] if head.random else None
            newHead.next = nodes[head.next] if head.next else None
            newHead, head = newHead.next, head.next
            
        return nodes[dummy.next]
        
        ###################
        
#         # this is okay and handles cycles, but arguably not as clean as below
#         # we will have to create new nodes, with the old nodes as references
#         # we can either create all the nodes first and then move through the list
#         # or we can create the nodes as we move through the list
        
#         newNodes = {}
#         q = collections.deque([(head)])
        
#         while q:
#             curr = q.popleft()
#             if curr is None or curr in newNodes:
#                 continue
                
#             newNodes[curr] = newNodes.get(curr, Node(x = curr.val, next = None, random = None))
#             q.append(curr.next)
#             q.append(curr.random)
            
#         for node in newNodes:
#             curr = newNodes[node]
#             curr.next = None if node.next is None else newNodes[node.next]
#             curr.random = None if node.random is None else newNodes[node.random]
            
#         return None if head is None else newNodes[head]
        
        
        
        ########################
        
#         # this is great but it doesn't handle cycles
#         # store nodes in a hashmap, node: newnode
#         # iterate through list, if an entry exists for a node then we point to it else we add entry and point
#         # time: n
#         # space: n
#         if head is None: return None
        
#         nodes = {head: Node(x = head.val)}
#         res = nodes[head]
#         while head:
#             nodes[head] = nodes.get(head, Node(x = head.val))
#             curr = nodes[head]
            
#             if head.next:
#                 nodes[head.next] = nodes.get(head.next, Node(x = head.next.val))
#                 curr.next = nodes[head.next]
#             else:
#                 curr.next = None
            
#             if head.random:
#                 nodes[head.random] = nodes.get(head.random, Node(x = head.random.val))
#                 curr.random = nodes[head.random]
#             else:
#                 curr.random = None
                
#             # curr.next = None if head.next is None else nodes.get(head.next, Node(x = head.next.val))
#             # curr.random = None if head.random is None else nodes.get(head.random, Node(x = head.random.val))
#             head = head.next
#         return res