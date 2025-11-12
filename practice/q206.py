# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None      # 前一个节点
        curr = head      # 当前节点
        
        while curr:      # 遍历整个链表
            next_temp = curr.next  # 暂存下一个节点
            curr.next = prev       # 翻转指针
            prev = curr            # prev前进
            curr = next_temp       # curr前进
            
        return prev  # prev 最终指向新的头节点
# 测试
if __name__ == "__main__":
    s = Solution()
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    new_head = s.reverseList(head)
    
    # 输出新的链表
    cur = new_head
    while cur:
        print(cur.val, end=" -> " if cur.next else "\n")
        cur = cur.next