# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        
        
        if not lists:
            return
        
        def merge(left, right):
            dummy = ListNode()
            merged = dummy
            # continue until a node is null
            while left and right:
                if left.val < right.val:
                    merged.next = left
                    left = left.next
                else:
                    merged.next = right
                    right = right.next
                merged = merged.next
            
            if left:
                merged.next = left
            if right:
                merged.next = right
            
            return dummy.next
        
        
        # loop until there is only one list
        while len(lists) > 1:
            
            # grab two lists
            left = lists.pop()
            right = lists.pop()
            
            # merge two lists
            merged = merge(left, right)
            lists.append(merged)
            
        return lists[0]
            
        
        