# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        
        
        
        
        
        
        dummy = ListNode(next = head)
        slow, fast = dummy, head
        for i in range(n):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        print(slow.val)
        slow.next = slow.next.next
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # 2 pointers, spaced n + 1 nodes apart (0 indexed)
#         # iterate until r is None, then set l.next = l.next.next
        
#         dummy = ListNode(next = head)
#         l, r = dummy, head
        
#         for i in range(n):
#             r = r.next
        
#         while r:
#             l = l.next
#             r = r.next
            
#         l.next = l.next.next
        
#         return dummy.next