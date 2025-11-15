from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1.sort()
        for num in list1:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next