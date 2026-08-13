class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next 
            index -= 1
        
        if cur and cur != self.right and index == 0:
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)

        new.next = self.left.next
        new.prev = self.left

        new.next.prev = new
        self.left.next = new
        

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)

        new.prev = self.right.prev 
        new.next = self.right

        new.prev.next = new
        self.right.prev = new
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and index == 0:
            new = ListNode(val)
            new.next = cur
            new.prev = cur.prev
            cur.prev = new
            new.prev.next = new


    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and index == 0 and cur != self.right:
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
        
class ListNode: 
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)