class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, pre.next = self, head
        
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next