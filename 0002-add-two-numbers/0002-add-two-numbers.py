# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # store numbers in array
        a1 = []
        a2 = []
        dummy = ListNode()
        res = dummy
        
        carry = 0
        while l1 or l2:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
                
            total = num1 + num2 + carry
            carry = total // 10

            dummy.next = ListNode(val = total % 10, next = None)
            dummy = dummy.next
            
        if carry:
            dummy.next = ListNode( val = 1, next = None)
        
        
        return res.next
    
    
    