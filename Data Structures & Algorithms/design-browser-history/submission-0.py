class BrowserHistory:

    def __init__(self, homepage: str):
        node = HistoryItem(homepage)
        self.cur = node
        
    def visit(self, url: str) -> None:
        node = HistoryItem(url)

        self.cur.next = node
        node.prev = self.cur

        self.cur = node

    def back(self, steps: int) -> str:
        cur = self.cur
        while cur and steps > 0:
            prev = cur
            cur = cur.prev
            steps -= 1
        
        if cur:
            self.cur = cur
            return cur.val
        else:
            self.cur = prev
            return prev.val
        

    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur and steps > 0:
            prev = cur
            cur = cur.next
            steps -= 1
        
        if cur:
            self.cur = cur
            return cur.val
        else:
            self.cur = prev
            return prev.val
        
class HistoryItem:
    def __init__(self, page):
        self.next = None
        self.prev = None
        self.val = page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)