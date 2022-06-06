# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
    
        
        prev = None
        while head:
            temp, head.next = head.next, prev
            prev, head = head, temp
        return prev
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         prev = None
#         while head:
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
        
#         return prev
        
        
        
        
        
        
        
        # set the current.next to the previous and iterate until current is None
#         # iteratively
#         if head is None: return None
#         prev = None # ListNode(next=head) results in a cycle
        
#         while head:
#             nextnode = head.next
#             head.next = prev
#             prev = head
#             head = nextnode
#         return prev
        
        # recursively
#         if head is None: return None
        
#         def reverse(head, prev):
#             if head is None:
#                 return prev
#             nextnode = head.next
#             head.next = prev
#             return reverse(head=nextnode, prev=head) # !!! remember to return this !!!
#                                                      # otherwise, the base case will return to it's parent
#                                                      # and then the parent won't return anything to the
#                                                      # grandparent and eventually there is no return in
#                                                      # function
            
#         prev = None # ListNode(next=head) results in a cycle
#         prev = reverse(head, prev)
#         return prev
    
        #####################
        
        # iterative
        # time: n, go through ll once
        # space: 1, just a few pointers
        prev = None
        while head:
            temp, head.next = head.next, prev
            prev, head = head, temp
            
        return prev
    
        # recursive
        # try again in future