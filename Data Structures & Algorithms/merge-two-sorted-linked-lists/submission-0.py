# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy list
        # loop through both lists
            # repeat until both lists empty
                # pick greater value from each list
                # merge greater value into dummy list
                # iterate list chosen, not list unchosen 

        tempList = ListNode(-1, None)
        tempListCur = tempList

        curList1 = list1
        curList2 = list2

        while curList1 or curList2:
            smallerValue = 0

            if not curList1:
                smallerValue = curList2.val
                curList2 = curList2.next
            elif not curList2:
                smallerValue = curList1.val
                curList1 = curList1.next
            else:
                if curList1.val <= curList2.val:
                    smallerValue = curList1.val
                    curList1 = curList1.next
                else:
                    smallerValue = curList2.val
                    curList2 = curList2.next
                
            tempListCur.next = ListNode(smallerValue, None)
            tempListCur = tempListCur.next
        
        return tempList.next


