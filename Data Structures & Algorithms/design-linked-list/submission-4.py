class ListNode():
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        if index <= (self.size // 2):
            cur = self.left
            for _ in range(index):
                cur = cur.next
        
        else:
            cur = self.right
            for _ in range(self.size - index + 1):
                cur = cur.prev
        
        return cur


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            return self.getPrev(index).next.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        else:
            prev = self.getPrev(index)
            new = ListNode(val)

            new.prev = prev
            new.next = prev.next

            new.next.prev = new
            new.prev.next = new

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        else:
            prev = self.getPrev(index)
            cur = prev.next

            prev.next = cur.next
            cur.next.prev = prev

            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)