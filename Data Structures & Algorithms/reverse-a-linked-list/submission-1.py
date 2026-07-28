# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go to head, set head.next to null
        # go to next, save next pointer then set next pointer to previous
        # go to next, repeat until hit prevous end (null), set to head then next to previous

        cur = head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev

