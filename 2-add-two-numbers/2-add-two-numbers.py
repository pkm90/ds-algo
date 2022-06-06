# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        

        
        
        dummy = ListNode()
        tail = dummy
        carry = 0
        # main ops
        while l1 and l2:
            num = l1.val + l2.val + carry
            val = num % 10
            carry = num // 10
            tail.next = ListNode(val = val)
            l1, l2, tail = l1.next, l2.next, tail.next
        
        # in case lists are uneven
        l = l1 or l2
        while l:
            num = l.val + carry
            val = num% 10
            carry = num // 10
            tail.next = ListNode(val = val)
            l, tail = l.next, tail.next
        
        # last carry
        if carry:
            tail.next = ListNode(val = carry)
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = ListNode()
#         tail = dummy
#         carry = 0
#         # main operations
#         while l1 and l2:
#             num = l1.val + l2.val + carry
#             carry = num // 10
#             num = num % 10
#             tail.next = ListNode(val = num)
#             l1, l2, tail = l1.next, l2.next, tail.next
        
#         # for uneven lists
#         if l1 or l2:
#             l1 = l1 if l1 else l2
#             while l1:
#                 num = l1.val + carry
#                 carry = num // 10
#                 num = num % 10
#                 tail.next = ListNode(val = num)
#                 l1, tail = l1.next, tail.next
                
#         # add carry if it exists
#         if carry:
#             tail.next = ListNode(val = carry)
            
#         return dummy.next