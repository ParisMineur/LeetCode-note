
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = next_head = ListNode(0)
        dummy.next = head
        
        pre = curr = head
        
        while True:
            count = 0
            while curr and count < k:  ## find the interval of elements
                count += 1
                curr = curr.next
            
            if count == k:
                l, r = pre, curr
                for _ in range(k):  ## reverse elements in the interval
                    temp = l.next
                    l.next = r
                    r = l
                    l = temp
                next_head.next = r  ## connect this interval with previous interval
                next_head = pre
                pre = curr
            
            else:
                return dummy.next
