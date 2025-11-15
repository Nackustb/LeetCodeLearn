class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # key -> node
        self.capacity = capacity
        self.size = 0
        # 使用伪头部和伪尾部节点，减少边界条件判断
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 在头部添加节点
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除节点
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    # 移动节点到头部
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    # 删除尾部节点
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        # 移动到头部表示最近使用
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            # 创建新节点
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                # 删除尾部节点
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # 更新值并移动到头部
            node.value = value
            self._move_to_head(node)