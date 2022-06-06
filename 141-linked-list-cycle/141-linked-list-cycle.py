# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        
        
        
        
#         if head is None: return None
        
#         slow, fast = head, head.next
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False
        
        
        
        
        
        
        # just slow/fast right?
        # gonna do it and then neetcode to learn better methods
        
        if (head is None or head.next is None): return None
        slow, fast = head, head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False