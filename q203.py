# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)      # 创建虚拟头节点
        dummy.next = head
        cur = dummy
        
        while cur.next:           # 遍历链表
            if cur.next.val == val:
                cur.next = cur.next.next   # 删除节点
            else:
                cur = cur.next             # 移动指针
                
        return dummy.next                  # 返回新的头节点

# 测试
if __name__ == "__main__":
    s = Solution()
    # 创建链表 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    
    val = 6
    new_head = s.removeElements(head, val)
    
    # 输出新的链表
    cur = new_head
    while cur:
        print(cur.val, end=" -> " if cur.next else "\n")
        cur = cur.next