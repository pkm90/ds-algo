# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
        
#         l1 = [2,4,3], 
#         l2 = [5,6,4]
        
#           342 
#         + 465
        
#         iterate through LL
        
#         243
#         564
#         [7,0,8]
        
        
#          50
#          50
#         100
        
#         05
#         05
#         001
        
#           2
#         564
        
#         n1 = 0
#         n2 = 0
        
#         n1 += i1
#         n2 += j2

        
        # store numbers in array
        a1 = []
        a2 = []
        # while l1:
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
            # print(total)
            dummy.next = ListNode(val = total % 10, next = None)
            dummy = dummy.next
            
        if carry:
            dummy.next = ListNode( val = 1, next = None)
            
#         temp = res.next
#         while temp:
#             # print(temp.val)
#             temp = temp.next
        
        
        return res.next