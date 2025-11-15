class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: list) -> 'ListNode':
        heap = []
        for  node in (lists):
            while node:
                heappush(heap, node.val )  
                node = node.next
        
        dummy = ListNode(0)
        cur = dummy
        
        while heap:
            val = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next