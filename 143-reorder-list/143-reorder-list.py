#####
# do this a lot since it practices a lot of fundamentals
#####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        lhead = head
        rhead = slow.next
        slow.next = None
        
        # reverse right half
        prev = None
        dummy = rhead
        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp
        rhead = prev

        # merge lists
        while lhead and rhead:
            temp = lhead.next
            lhead.next = rhead
            lhead = temp
            
            temp = rhead.next
            rhead.next = lhead
            rhead = temp
        
        
        
        
        
        
        # find middle
        #  slow and fast pointer, when fast or fast.next is None then slow will be at end of first list
        # reverse second half of ll
        # merge the two halves
                
        # getting to the middle
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         temp = slow.next
#         slow.next = None
        
#         print(temp)
#         # reversing the second half
#         l, r, prev = head, temp, None
#         while r:
#             temp, r.next = r.next, prev
#             prev, r = r, temp
#         r = prev
        
#         # now we merge the two halves
#         # left.next is right, right.next is left.next
#         while l and r:
#             temp = l.next
#             l.next = r
#             l = temp
            
#             temp = r.next
#             r.next = l
#             r = temp
        
#         # return head
            
        
        