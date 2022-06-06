# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 or list2:
            tail.next = list1 or list2
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = ListNode()
#         tail = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next, list1 = list1, list1.next
#             else:
#                 tail.next, list2 = list2, list2.next
#             tail = tail.next
        
#         if list1 or list2:
#             tail.next = list1 if list1 else list2
        
#         return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        # done this iteratively before, going to try recursively
        # iterative (maybe, check ll ipynb if curious)
        # lists are already sorted
        # we will have 3 currents, 2 for hte lists and 1 for return, also have head for the head of the return list 
        # compare the two currents, set the lesser to the next of the return pointer
        # whichever list is lesser, we iterate, and we always iterate the return
        # continue until one of the lists is None, and then append the other list to the next of return
        
        # recursive
        # base case
        #  when one of the lists is None, return other list
        # recurrence
        #  is there a recurrence relationship?
        #  do we have to return anything? 
        #  can we just make changes and return the head after the recursive function?
        #  if node1<=node2: current.next=node1 and node1=node1.next
        #  else current.next=node2 and iterate node2 
        #  recurse(current=current.next, node1, node2)

        # def recurse(current, node1, node2):
        #     if (not node1 or not node2):
        #         current.next = node1 if node1 else node2
        #         return
        #     if node1.val<=node2.val:
        #         current.next = node1
        #         recurse(current=current.next, node1=node1.next, node2=node2)
        #     else:
        #         current.next = node2
        #         recurse(current=current.next, node1=node1, node2=node2.next)
        # head = ListNode(-1)
        # recurse(head, list1, list2)
        # return head.next

        
##################
        # do this again in future
        # iterative
        # while pointers to both lists exist
        #  set larger to next of smaller
        
        dummy = ListNode()
        res = dummy
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        
        if list1:
            res.next = list1
        if list2:
            res.next = list2
        
        return dummy.next