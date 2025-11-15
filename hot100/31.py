from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy   # 每组前一个节点

        while True:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            nxt = tail.next     
            cur = pre.next      
            prev = nxt          

            while cur != nxt:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp


            tmp = pre.next 
            pre.next = tail
            pre = tmp

