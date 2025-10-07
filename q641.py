class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 ) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# 测试
if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)  # 设置容量大小为3
    print(circularDeque.insertLast(1))   # 返回 true
    print(circularDeque.insertLast(2))   # 返回 true
    print(circularDeque.insertFront(3))  # 返回 true
    print(circularDeque.insertFront(4))  # 返回 false，队列已满
    print(circularDeque.getRear())       # 返回 2
    print(circularDeque.isFull())        # 返回 true
    print(circularDeque.deleteLast())    # 返回 true
    print(circularDeque.insertFront(4))  # 返回 true
    print(circularDeque.getFront())      # 返回 4   
