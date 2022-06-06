# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        
        
        
        
        
        
        
        
        
        while len(lists) > 1:
            dummy = ListNode()
            tail = dummy
            l1, l2 = lists.pop(), lists.pop()
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            lists.append(dummy.next)
        # print(lists)
        return lists[0] if lists else None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ##################
        
        
#         # !! have to decrement len(lists) to avoid index oob errors
#         while len(lists) > 1:
            
#             mergedLists = []
#             for i in range(0, len(lists) - 1, 2): # !! have to decrement len(lists) to avoid index oob errors
#                 dummy = ListNode()
#                 tail = dummy
#                 l1, l2 = lists.pop(), lists.pop()
#                     if l1.val < l2.val:
#                         tail.next = l1
#                         l1 = l1.next
#                     else:
#                         tail.next = l2
#                         l2 = l2.next
#                     tail = tail.next
#                 if l1 or l2:
#                     tail.next = l1 if l1 else l2
#                 mergedLists.append(dummy.next)            
#             lists.extend(mergedLists)

#         return None if len(lists) is 0 else lists[0]
        
        
        #################
                
        
#         # remember, we have to create a new dummy and tail each iteration
#         if len(lists) is 0: return None
        
#         while len(lists) > 1:
            
#             l1 = lists.pop() # E
#             l2 = lists.pop() # D
            
#             dummy = ListNode()
#             tail = dummy
            
#             # merge
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     tail.next = l1
#                     l1 = l1.next
#                 else:
#                     tail.next = l2
#                     l2 = l2.next
#                 tail = tail.next
#             if l1 or l2:
#                 tail.next = l1 if l1 else l2
            
#             # insert into first position of list
#             lists.insert(0, dummy.next)
            
#         return lists[0]
        
        
    
        
        
      ##################  
        
        
        # like merge 1 linked list, but we iterate k times
        
#         if len(lists) is 0: return None
#         if len(lists) is 1: return lists[0]
        
#         dummy = ListNode()
#         tail = dummy
#         prev = lists[0]
        
#         for curr in range(1, len(lists)):
#             tail = dummy
#             curr = lists[curr]
            
#             while prev and curr:
#                 if prev.val < curr.val:
#                     tail.next = prev
#                     prev = prev.next
#                 else:
#                     tail.next = curr
#                     curr = curr.next
#                 tail = tail.next
#             if prev:
#                 tail.next = prev
#             if curr:
#                 tail.next = curr
#             prev = dummy.next
                
#         return dummy.next
    
    
    
    ###################
    
#         # try separating functionality
        
#         # try doing the mergesort/nlogk approach
        
#         if len(lists) == 0: return None
#         dummy = ListNode()
#         tail = dummy
        
#         while len(lists) > 1:
#             l = lists.pop(0)
#             r = lists.pop(-1)
#             tail = dummy
#             while l and r:
#                 if l.val < r.val:
#                     tail.next = l
#                     l = l.next
#                 else:
#                     tail.next = r
#                     r = r.next
#                 tail = tail.next
                
#             if l:
#                 tail.next = l
#             if r:
#                 tail.next = r
#             lists.append(dummy.next)
            
#         return lists[0]