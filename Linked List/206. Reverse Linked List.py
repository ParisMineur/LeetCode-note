class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, pre = head, None
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        return pre
